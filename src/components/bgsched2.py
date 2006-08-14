#!/usr/bin/env python

'''Scheduler for BG/L'''
__revision__ = '$Revision$'

import copy, logging, sys, time, xmlrpclib, ConfigParser
import Cobalt.Component, Cobalt.Data, Cobalt.Logging, Cobalt.Proxy, Cobalt.Util

if '--nodb2' not in sys.argv:
    import DB2

logger = logging.getLogger('bgsched')

comm = Cobalt.Proxy.CommDict()

class FailureMode(object):
    '''FailureModes are used to report (and supress) errors appropriately
    call Pass() on success and Fail() on error'''
    def __init__(self, name):
        self.name = name
        self.status = True

    def Pass(self):
        '''Check if status was previously failure and report OK status if needed'''
        if not self.status:
            logger.error("Failure %s cleared" % (self.name))
            self.status = True

    def Fail(self):
        '''Check if status was previously success and report failed status if needed'''
        if self.status:
            logger.error("Failure %s occured" % (self.name))
            self.status = False

class event:
    '''events describe an event in terms of start and duration'''
    def __init__(self, start, duration, status):
        self.start = start
        self.duration = duration
        self.status = status

class timeData(Cobalt.Data.Data):
    '''timeData is a class that can generate event traces for temporal ops'''
    def __init__(self, element):
        Cobalt.Data.Data.__init__(self, element)

    def getEvents(self):
        '''Return Duration events for self'''
        return []

class Reservation(timeData):
    '''This class represents reservations'''
    def __init__(self, element):
        timeData.__init__(self, element)

    def getEvents(self):
        
        return [event(self.get('start'), float(self.get('duration')), 'hard')]
        
class ReservationSet(Cobalt.Data.DataSet):
    '''This class holds the reservations'''
    __object__ = Reservation

    def __init__(self):
        Cobalt.Data.DataSet.__init__(self)

class Job(timeData):
    '''This class represents User Jobs'''
    def __init__(self, element):
        timeData.__init__(self, element)
        self.partition = 'none'
        logger.info("Job %s/%s: Found new job" % (self.get('jobid'),
                                                       self.get('user')))
        self.start = -1

    def getEvents(self):
        if self.start != -1:
            etype = 'soft'
            if self.status == 'planned':
                etype = 'hard'
            return [event(self.start, float(self.get('walltime')), etype)]
        else:
            return []

    def planRun(self, start):
        if self.start == -1:
            self.start = start
            self.status = 'planned'
        else:
            logger.error("Job %s: Attempted to run multiple times" % (self.get('jobid')))

cqmFailed = FailureMode("QM Connection")

class JobSet(Cobalt.Data.DataSet):
    __object__ = Job
    __syncrate__ = 60
    alljobq = [{'tag':'job', 'nodes':'*', 'location':'*', 'jobid':'*', 'state':'*',
		'walltime':'*', 'queue':'*', 'user':'*'}]

    def __init__(self):
        Cobalt.Data.DataSet.__init__(self)
        self.lastrun = -1

    def Sync(self):
        '''Synchronize with current queue state'''
        since = time.time() - self.lastrun
        if since < self.__syncrate__:
            return
        try:
            jobs = comm['qm'].GetJobs(self.alljobq)
        except xmlrpclib.Fault:
            cqmFailed.Fail()
            return 0
        except:
            logger.error("Unexpected fault during queue fetch", exc_info=1)
            return 0
        cqmFailed.Pass()
        active = [job.get('jobid') for job in jobs]
        for current in jobs:
            if self.Get([current]):
                # job is already registered and matches
                continue
            else:
                if not self.Get([{'tag':'job', 'jobid':current.get('jobid')}]):
                    # job is new
                    self.Add([current])
                    continue
                # job is modified
		# sync data here
                pass
	# find finished jobs
        for job in self:
            if job.get('jobid') not in active:
                logger.info("Job %s has completed" % (job.get("jobid")))
                self.Del([{'tag':'job', 'jobid':job.get('jobid')}])
        self.lastrun = time.time()

class Partition(timeData):
    '''Partitions are allocatable chunks of the machine'''
    def __init__(self, element):
        timeData.__init__(self, element)
        self.set('state', 'idle')
        self.set('reservations', [])
        self.job = 'none'
        self.rcounter = 1
        self.set('db2', 'XX')

    def isIdle(self):
        '''Return True if partition is idle'''
        if '--nodb2' not in sys.argv:
            return self.get('state') == 'idle' and self.get('db2') == 'F'
        else:
            return self.get('state') == 'idle'

    def CanRun(self, job):
        '''Check that job can run on partition with reservation constraints'''
        basic = self.get('scheduled') and self.get('functional')
        queue = job.get('queue') in self.get('queue').split(':')
        jsize = int(job.get('nodes')) # should this be 'size' instead?
        psize = int(self.get('size'))
        size = ((psize >= jsize) and ((psize == 32) or (jsize > psize/2)))
        if not (basic and queue and size):
            return False
        # add a little slack for job cleanup with reservation calculations
        wall = float(job.get('walltime')) + 5.0
        jdur = 60 * wall
        # all times are in seconds
        current = time.time()
        for (_, user, start, rdur) in self.get('reservations'):
            if job.get('user') in user:
                continue
            if current < start:
                # reservation has not started
                if start < (current + jdur):
                    return False
            elif current > (start + rdur):
                # reservation has finished
                continue
            else:
                # reservation is active
                return False
        return True

    def PlaceJob(self, job):
        '''Allocate this partition for Job'''
        logger.info("Job %s/%s: Scheduling job %s on partition %s" % (
            job.get('jobid'), job.get('user'), job.get('jobid'),
            self.get('name')))
        self.job = job.get('jobid')
        self.set('state', 'busy')

    def Free(self):
        '''DeAllocate partition for current job'''
        logger.info("Job %s: Freeing partition %s" % (self.job, self.get('name')))
        self.job = 'none'
        self.set('state', 'idle')

class PartitionSet(Cobalt.Data.DataSet):
    __object__ = Partition

    _configfields = ['db2uid', 'db2dsn', 'db2pwd']
    _config = ConfigParser.ConfigParser()
    if '-C' in sys.argv:
        _config.read(sys.argv[sys.argv.index('-C') + 1])
    else:
        _config.read('/etc/cobalt.conf')
    if not _config._sections.has_key('bgsched'):
        print '''"bgsched" section missing from cobalt config file'''
        raise SystemExit, 1
    config = _config._sections['bgsched']
    mfields = [field for field in _configfields if not config.has_key(field)]
    if mfields:
        print "Missing option(s) in cobalt config file: %s" % (" ".join(mfields))
        raise SystemExit, 1
    if not _config._sections.has_key('bgsched-queue'):
        print '''bgsched-queue section missing from config file'''
        raise SystemExit, 1
    qconfig = _config._sections['bgsched-queue']
    qpolicy = {'default':'PlaceFIFO', 'scavenger':'PlaceScavenger'}

    def __init__(self):
        Cobalt.Data.DataSet.__init__(self)
        if '--nodb2' not in sys.argv:
            try:
                import DB2
                conn = DB2.connect(uid=self.config.get('db2uid'), pwd=self.config.get('db2pwd'),
                                   dsn=self.config.get('db2dsn'))
                self.db2 = conn.cursor()
            except:
                print "Failed to connect to DB2"
                raise SystemExit, 1
        self.jobs = []
        self.qmconnect = FailureMode("QM Connection")

    def __getstate__(self):
        return {'data':copy.deepcopy(self.data), 'jobs':copy.deepcopy(self.jobs)}

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.qmconnect = FailureMode("QM Connection")
        if '--nodb2' not in sys.argv:
            import DB2
            self.db2 = DB2.connect(uid=self.config.get('db2uid'), pwd=self.config.get('db2pwd'),
                                   dsn=self.config.get('db2dsn')).cursor()

    def isFree(self, partname, starttime, duration):
        '''checks if partition is active/enabled for time specified'''
        for part in self.data:
            if part.get('name') == partname and part.get('scheduled') and part.get('functional') and part.get('state') == 'idle':
                return True
                
        return False

class BGSched(Cobalt.Component.Component):
    '''This scheduler implements a fifo policy'''
    __implementation__ = 'bgsched'
    __name__ = 'scheduler'
    __statefields__ = ['partitions', 'jobs']
    __schedcycle__ = 10
    async_funcs = ['assert_location', 'RunQueue']

    def __init__(self, setup):
        self.partitions = PartitionSet()
        self.jobs = JobSet()
        self.reservations = ReservationSet()
        Cobalt.Component.Component.__init__(self, setup)
        self.executed = []
        self.qmconnect = FailureMode("QM Connection")
        self.lastrun = 0
        self.register_function(lambda  address, data:self.partitions.Get(data), "GetPartition")
        self.register_function(lambda  address, data:self.partitions.Add(data), "AddPartition")
        self.register_function(lambda  address, data:self.partitions.Del(data), "DelPartition")
        self.register_function(lambda address, data, updates:
                               self.partitions.Get(data, lambda part, newattr:part.update(newattr), updates),
                               'Set')  
        self.register_function(self.AddReservation, "AddReservation")
        self.register_function(self.ReleaseReservation, "DelReservation")

    def AddReservation(self, _, spec, name, user, start, duration):
        '''Add a reservation to matching partitions'''
        reservation = (name, user, start, duration)
        return self.partitions.Get(spec, callback=lambda x, y:x.get('reservations').append(reservation))

    def ReleaseReservation(self, _, spec, name):
        '''Release specified reservation'''
        return self.partitions.Get(spec, callback=lambda x, y:[x.get('reservations').remove(rsv)
                                                              for rsv in x.get('reservations') if rsv[0] == name])

    def SupressDuplicates(self, provisional):
        '''Prevent duplicate job start requests from being generated'''
        for (jobid, location) in provisional:
            if jobid in self.executed:
                logger.error("Tried to execute job %s multiple times" % (jobid))
                provisional.remove((jobid, location))
                [partition.Free() for partition in self.partitions if partition.get('name') == location]
            else:
                self.executed.append(jobid)

    def CanRun(self, nodes, duration, queue, user, location, starttime):
        '''
        nodes - size of job
        duration - walltime of job
        queue - 
        user - 
        location - 
        starttime - time that job is intended to be started
        '''
        family = [location] + self.partitions.GetParents(location) + self.partitions.GetChildren(location)
        # check location
        if not self.partitions.isFree(location, starttime, duration):
            return False
        # check queues
        
        # check reservations
        for res in self.reservations:
            if not ((float(starttime) > float(res.get('start')) + float(res.get('duration')))
                    or
                    ((float(starttime) + float(duration) < float(res.get('start'))))):
                
                if location in res.get('location').split(':') and user not in res.get('user').split(':'):
                    return False
        # check for conflicts with running jobs
        for rjob in [job for job in self.jobs if job.status == 'running']:
            if rjob.get('location') in family:
                if not ((float(starttime) > float(rjob.get('starttime')) + float(rjob.get('walltime')))
                        or
                        ((float(starttime) + float(duration) < float(rjob.get('starttime'))))):
                    return False

        return True

if __name__ == '__main__':
    from getopt import getopt, GetoptError
    try:
        (OPTS, ARGS) = getopt(sys.argv[1:], 'C:dD:t', ['nodb2'])
    except GetoptError, msg:
        print "%s\nUsage:\nbgsched.py [-t] [-C configfile] [-d] [-D <pidfile>] [--nodb2]" % (msg)
        raise SystemExit, 1
    try:
        DAEMON = [x[1] for x in OPTS if x[0] == '-D'][0]
    except:
        DAEMON = False
    if len([x for x in opts if x[0] == '-d']):
        DLEVEL = logging.DEBUG
    else:
        DLEVEL = logging.INFO
    Cobalt.Logging.setup_logging('bgsched', level=DLEVEL)
    SERVER = BGSched({'configfile':'/etc/cobalt.conf', 'daemon':DAEMON})
    SERVER.serve_forever()
    
