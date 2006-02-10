'''Data builds up datatype definitions on top of XML-RPC serializable python types'''
__revision__ = '$Revision:$'

import time, types, xmlrpclib, random

class DataCreationError(Exception):
    '''Used when a new object cannot be created'''
    pass

class IncrID(object):
    '''Autoincrementing id generator'''
    def __init__(self):
        self.idnum = 0

    def get(self):
        '''Return new ID'''
        self.idnum += 1
        return self.idnum

class RandomID(object):
    '''Somewhat randomly selected unique ID pool'''
    def __init__(self):
        self.used = []
        self.rand = random.Random(int(time.time()))

    def get(self):
        '''Return new random id'''
        idnum = str(self.rand.randrange(0, 2147483639)) + str(self.rand.randrange(0, 2147483639))
        while idnum in self.used:
            idnum = str(self.rand.randrange(0, 2147483639)) + \
            str(self.rand.randrange(0, 2147483639))
        self.used.append(idnum)
        return idnum

class Data(object):
    '''Data takes nested dictionaries and builds objects analogous to sss.restriction.data objects'''
    required_fields = []

    def __init__(self, info):
        self.tag = info['tag']
        del info['tag']
        missing = [field for field in self.required_fields if not info.has_key(field)]
        if missing:
            raise DataCreationError, missing
        self._attrib = {}
        self.set('stamp', time.time())
        self._attrib.update(info)

    def get(self, field, default=None):
        '''return attribute'''
        if self._attrib.has_key(field):
            return self._attrib[field]
        if default != None:
            return default
        raise KeyError, field

    def set(self, field, value):
        '''set attribute'''
        self._attrib[field] = value
        self._attrib['stamp'] = time.time()

    def update(self, attrdict):
        '''update attributes based on attrdict'''
        for item in attrdict.iteritems():
            self.set(item[0], item[1])
            
    def match(self, spec):
        '''Implement datatype matching'''
        fields = [field for field in spec if field != 'tag']
        return self.tag == spec['tag'] and not [field for field in fields if spec[field] != '*' and (self.get(field) != spec[field])]
        
    def to_rx(self, spec):
        '''return transmittable version of instance'''
        rxval = {'tag':self.tag}
        for field in [field for field in spec.keys() if field != 'tag' and self._attrib.has_key(field)]:
            rxval[field] = self.get(field)
        return rxval

class DataSet(object):
    '''DataSet provides storage, iteration, and matching across sets of Data instances'''
    __object__ = Data
    __id__ = None
    __unique__ = False

    def __init__(self):
        self.data = []

    def __iter__(self):
        return iter(self.data)

    def append(self, x):
        '''add a new element to the set'''
        return self.data.append(x)

    def remove(self, x):
        '''remove an element from the set'''
        return self.data.remove(x)

    def Add(self, cdata, callback=None, cargs=()):
        '''Implement semantics of operations that add new item(s) to the DataSet'''
        retval = []
        if type(cdata) != types.ListType:
            cdata = [cdata]
        for item in cdata:
            try:
                if self.__id__:
                    iobj = self.__object__(item, self.__id__.get())
                else:
                    iobj = self.__object__(item)
            except DataCreationError, missing:
                print "returning fault"
                raise xmlrpclib.Fault(8, str(missing))
            #return xmlrpclib.dumps(xmlrpclib.Fault(8, str(missing)))
            # uniqueness test goes here
            self.data.append(iobj)
            if callback:
                apply(callback, (iobj, ) + cargs)
            retval.append(iobj.to_rx(item))
        return retval

    def Get(self, cdata, callback=None, cargs={}):
        '''Implement semantics of operations that get item(s) from the DataSet'''
        retval = []
        for spec in cdata:
            for item in [datum for datum in self.data if datum.match(spec)]:
                if callback:
                    callback(item, cargs)
                retval.append(item.to_rx(spec))
        return retval

    def Del(self, cdata, callback=None, cargs={}):
        '''Implement semantics of operations that delete item(s) from the DataSet'''
        retval = []
        for spec in cdata:
            for item in [datum for datum in self.data if datum.match(spec)]:
                self.data.remove(item)
                if callback:
                    callback(item, cargs)
                retval.append(item.to_rx(spec))
        return retval
