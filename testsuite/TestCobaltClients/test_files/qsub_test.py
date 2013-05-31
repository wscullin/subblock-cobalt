import testutils

# ---------------------------------------------------------------------------------
def test_qsub_all_options_1():
    """
    qsub test run: all_options_1
        Old Command Output:
          1
          

    """

    args      = """-v -A myproj --attrs=a=1:b=2 --cwd /tmp -d --debuglog=/tmp/d --dependencies=1:2:3 -e /tmp/e --env v1=1:v2=2 --geometry 198x198x198x198 -h -i /bin/ls -M myemal@gmail.com -n10 -o /tmp/o -O /tmp --proccount 10 -qqueue --run_users user1:user2:user3 --run_project -t 10 --mode smp --kernel kernel -K kopts /bin/ls"""

    cmdout    = \
"""
qsub.py -v -A myproj --attrs=a=1:b=2 --cwd /tmp -d --debuglog=/tmp/d --dependencies=1:2:3 -e /tmp/e --env v1=1:v2=2 --geometry 198x198x198x198 -h -i /bin/ls -M myemal@gmail.com -n10 -o /tmp/o -O /tmp --proccount 10 -qqueue --run_users user1:user2:user3 --run_project -t 10 --mode smp --kernel kernel -K kopts /bin/ls

component: "system.validate_job", defer: False
  validate_job(
     {'kernel': 'kernel', 'verbose': True, 'held': True, 'notify': 'myemal@gmail.com', 'project': 'myproj', 'preemptable': False, 'forcenoval': False, 'umask': False, 'version': False, 'env': 'v1=1:v2=2', 'cwd': '/tmp', 'run_project': True, 'outputprefix': '/tmp', 'kerneloptions': 'kopts', 'time': '10', 'debug': True, 'dependencies': '1:2:3', 'debuglog': '/tmp/d', 'proccount': '10', 'disable_preboot': False, 'geometry': '198x198x198x198', 'queue': 'queue', 'mode': 'smp', 'error': '/tmp/e', 'nodecount': '10', 'output': '/tmp/o', 'attrs': {'a': '1', 'b': '2'}, 'user_list': 'user1:user2:user3', 'inputfile': '/bin/ls'},
     )


component: "queue-manager.add_jobs", defer: False
  add_jobs(
     [{'kernel': 'kernel', 'errorpath': '/tmp/e', 'outputpath': '/tmp/o', 'tag': 'job', 'notify': 'myemal@gmail.com', 'outputdir': '/tmp', 'queue': 'queue', 'envs': {'v1': '1', 'v2': '2'}, 'umask': 18, 'nodes': 10, 'cwd': '/tmp', 'run_project': True, 'kerneloptions': 'kopts', 'args': [], 'cobalt_log_file': '/tmp/d', 'user': 'gooduser', 'path': '/tmp', 'procs': '10', 'walltime': '10', 'geometry': [198, 198, 198, 198, 2], 'user_hold': True, 'jobid': '*', 'project': 'myproj', 'script_preboot': True, 'command': '/bin/ls', 'mode': 'smp', 'all_dependencies': '1:2:3', 'attrs': {'a': '1', 'b': '2'}, 'user_list': ['gooduser', 'user1', 'user2', 'user3'], 'inputfile': '/bin/ls'}],
     )


1
"""

    stubout   = \
"""
GET_JOBS

jobid:1
jobid type: <type 'int'>
jobid:3
jobid type: <type 'int'>
jobid:2
jobid type: <type 'int'>

ADD_JOBS

all_dependencies:1:2:3
all_dependencies type: <type 'str'>
args:[]
args type: <type 'list'>
attrs:{'a': '1', 'b': '2'}
attrs type: <type 'dict'>
cobalt_log_file:/tmp/d
cobalt_log_file type: <type 'str'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
envs:{'v1': '1', 'v2': '2'}
envs type: <type 'dict'>
errorpath:/tmp/e
errorpath type: <type 'str'>
geometry:[198, 198, 198, 198, 2]
geometry type: <type 'list'>
inputfile:/bin/ls
inputfile type: <type 'str'>
jobid:*
jobid type: <type 'str'>
kernel:kernel
kernel type: <type 'str'>
kerneloptions:kopts
kerneloptions type: <type 'str'>
mode:smp
mode type: <type 'str'>
nodes:10
nodes type: <type 'int'>
notify:myemal@gmail.com
notify type: <type 'str'>
outputdir:/tmp
outputdir type: <type 'str'>
outputpath:/tmp/o
outputpath type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:10
procs type: <type 'str'>
project:myproj
project type: <type 'str'>
queue:queue
queue type: <type 'str'>
run_project:True
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_hold:True
user_hold type: <type 'bool'>
user_list:['gooduser', 'user1', 'user2', 'user3']
user_list type: <type 'list'>
walltime:10
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{'a': '1', 'b': '2'}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:True
debug type: <type 'bool'>
debuglog:/tmp/d
debuglog type: <type 'str'>
dependencies:1:2:3
dependencies type: <type 'str'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:v1=1:v2=2
env type: <type 'str'>
error:/tmp/e
error type: <type 'str'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:198x198x198x198
geometry type: <type 'str'>
held:True
held type: <type 'bool'>
inputfile:/bin/ls
inputfile type: <type 'str'>
kernel:kernel
kernel type: <type 'str'>
kerneloptions:kopts
kerneloptions type: <type 'str'>
mode:smp
mode type: <type 'str'>
nodecount:10
nodecount type: <type 'str'>
notify:myemal@gmail.com
notify type: <type 'str'>
output:/tmp/o
output type: <type 'str'>
outputprefix:/tmp
outputprefix type: <type 'str'>
preemptable:False
preemptable type: <type 'bool'>
proccount:10
proccount type: <type 'str'>
project:myproj
project type: <type 'str'>
queue:queue
queue type: <type 'str'>
run_project:True
run_project type: <type 'bool'>
time:10
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:user1:user2:user3
user_list type: <type 'str'>
verbose:True
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_misc_1():
    """
    qsub test run: misc_1
        Old Command Output:
          1
          

    """

    args      = """--mode c1 -n 512 --env BG_COREDUMPDISABLED=1 --proccount 512 -t 30 -q testing /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
envs:{'BG_COREDUMPDISABLED': '1'}
envs type: <type 'dict'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:c1
mode type: <type 'str'>
nodes:512
nodes type: <type 'int'>
outputdir:/tmp
outputdir type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:512
procs type: <type 'str'>
queue:testing
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:30
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:BG_COREDUMPDISABLED=1
env type: <type 'str'>
error:False
error type: <type 'bool'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:False
geometry type: <type 'bool'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:c1
mode type: <type 'str'>
nodecount:512
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:False
output type: <type 'bool'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:512
proccount type: <type 'str'>
project:False
project type: <type 'bool'>
queue:testing
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:30
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_no_options_passed():
    """
    qsub test run: no_options_passed
        Old Command Output:
          Not all required arguments provided: time,nodecount needed
          
          Usage: qsub [-d] [-v] -A <project name> -q <queue> --cwd <working directory>
                       --dependencies <jobid1>:<jobid2> --preemptable
                       --env envvar1=value1:envvar2=value2 --kernel <kernel profile>
                       -K <kernel options> -O <outputprefix> -t time <in minutes>
                       -e <error file path> -o <output file path> -i <input file path>
                       -n <number of nodes> -h --proccount <processor count> -u <umask>
                       --mode <mode> --debuglog <cobaltlog file path> <command> <args>
                       --users <user1>:<user2> --run_project --disable_preboot
          
          

    """

    args      = """/bin/ls"""

    cmdout    = \
"""No required options entered
'time' not provided
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_non_existant_option():
    """
    qsub test run: non_existant_option
        Old Command Output:
          option -z not recognized
          
          Usage: qsub [-d] [-v] -A <project name> -q <queue> --cwd <working directory>
                       --dependencies <jobid1>:<jobid2> --preemptable
                       --env envvar1=value1:envvar2=value2 --kernel <kernel profile>
                       -K <kernel options> -O <outputprefix> -t time <in minutes>
                       -e <error file path> -o <output file path> -i <input file path>
                       -n <number of nodes> -h --proccount <processor count> -u <umask>
                       --mode <mode> --debuglog <cobaltlog file path> <command> <args>
                       --users <user1>:<user2> --run_project --disable_preboot
          
          

    """

    args      = """-z -t10 -n10 /bin/ls"""

    cmdout    = \
"""Usage: qsub.py [options] <executable> [<excutable options>]

qsub.py: error: no such option: -z
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       512, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_debug_flag_only_1():
    """
    qsub test run: debug_flag_only_1
        Old Command Output:
          Command required
          
          Usage: qsub [-d] [-v] -A <project name> -q <queue> --cwd <working directory>
                       --dependencies <jobid1>:<jobid2> --preemptable
                       --env envvar1=value1:envvar2=value2 --kernel <kernel profile>
                       -K <kernel options> -O <outputprefix> -t time <in minutes>
                       -e <error file path> -o <output file path> -i <input file path>
                       -n <number of nodes> -h --proccount <processor count> -u <umask>
                       --mode <mode> --debuglog <cobaltlog file path> <command> <args>
                       --users <user1>:<user2> --run_project --disable_preboot
          
          

    """

    args      = """-d"""

    cmdout    = \
"""
qsub.py -d

No required options entered
'time' not provided
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_debug_flag_only_2():
    """
    qsub test run: debug_flag_only_2

    """

    args      = """-debug"""

    cmdout    = \
"""
qsub.py -debug

'time' not provided
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_verbose_flag_only():
    """
    qsub test run: verbose_flag_only
        Old Command Output:
          Command required
          
          Usage: qsub [-d] [-v] -A <project name> -q <queue> --cwd <working directory>
                       --dependencies <jobid1>:<jobid2> --preemptable
                       --env envvar1=value1:envvar2=value2 --kernel <kernel profile>
                       -K <kernel options> -O <outputprefix> -t time <in minutes>
                       -e <error file path> -o <output file path> -i <input file path>
                       -n <number of nodes> -h --proccount <processor count> -u <umask>
                       --mode <mode> --debuglog <cobaltlog file path> <command> <args>
                       --users <user1>:<user2> --run_project --disable_preboot
          
          

    """

    args      = """-v"""

    cmdout    = \
"""No required options entered
'time' not provided
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_non_integer_nodecount():
    """
    qsub test run: non_integer_nodecount
        Old Command Output:
          Command required
          
          Usage: qsub [-d] [-v] -A <project name> -q <queue> --cwd <working directory>
                       --dependencies <jobid1>:<jobid2> --preemptable
                       --env envvar1=value1:envvar2=value2 --kernel <kernel profile>
                       -K <kernel options> -O <outputprefix> -t time <in minutes>
                       -e <error file path> -o <output file path> -i <input file path>
                       -n <number of nodes> -h --proccount <processor count> -u <umask>
                       --mode <mode> --debuglog <cobaltlog file path> <command> <args>
                       --users <user1>:<user2> --run_project --disable_preboot
          
          

    """

    args      = """--mode smp -t50 -nfive --geometry 40x40x50x50   /bin/ls"""

    cmdout    = \
"""Usage: qsub.py [options] <executable> [<excutable options>]

qsub.py: error: option -n: invalid integer value: 'five'
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       512, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_non_realistic_nodecount():
    """
    qsub test run: non_realistic_nodecount
        Old Command Output:
          Command required
          
          Usage: qsub [-d] [-v] -A <project name> -q <queue> --cwd <working directory>
                       --dependencies <jobid1>:<jobid2> --preemptable
                       --env envvar1=value1:envvar2=value2 --kernel <kernel profile>
                       -K <kernel options> -O <outputprefix> -t time <in minutes>
                       -e <error file path> -o <output file path> -i <input file path>
                       -n <number of nodes> -h --proccount <processor count> -u <umask>
                       --mode <mode> --debuglog <cobaltlog file path> <command> <args>
                       --users <user1>:<user2> --run_project --disable_preboot
          
          

    """

    args      = """--mode smp -t50 -n2048 --geometry 40x40x50x50x1 /bin/ls"""

    cmdout    = \
"""node count out of realistic range
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_invalid_geometry_1():
    """
    qsub test run: invalid_geometry_1
        Old Command Output:
          Traceback (most recent call last):
            File "oldcmds/qsub.py", line 179, in <module>
              jobspec['geometry'] = parse_geometry_string(opts['geometry'])
            File "/Users/georgerojas/p/Cobalt/cobalt/testsuite/TestCobaltClients/Cobalt/Util.py", line 1112, in parse_geometry_string
              raise ValueError, "%s is an invalid geometry specification." % geometry_str
          ValueError: x is an invalid geometry specification.
          

    """

    args      = """--mode smp -t50 -n10 --geometry x /bin/ls"""

    cmdout    = \
"""Invalid geometry entered: 
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_invalid_geometry_2():
    """
    qsub test run: invalid_geometry_2
        Old Command Output:
          1
          

    """

    args      = """--mode smp -t50 -n10 --geometry 1x2x3x4 /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
geometry:[1, 2, 3, 4, 2]
geometry type: <type 'list'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:smp
mode type: <type 'str'>
nodes:10
nodes type: <type 'int'>
outputdir:/tmp
outputdir type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:512
procs type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:50
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:False
error type: <type 'bool'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:1x2x3x4
geometry type: <type 'str'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:smp
mode type: <type 'str'>
nodecount:10
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:False
output type: <type 'bool'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:False
proccount type: <type 'bool'>
project:False
project type: <type 'bool'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:50
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_invalid_geometry_3():
    """
    qsub test run: invalid_geometry_3
        Old Command Output:
          1
          

    """

    args      = """--mode smp -t50 -n10 --geometry 1x2x3x4 /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
geometry:[1, 2, 3, 4, 2]
geometry type: <type 'list'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:smp
mode type: <type 'str'>
nodes:10
nodes type: <type 'int'>
outputdir:/tmp
outputdir type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:512
procs type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:50
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:False
error type: <type 'bool'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:1x2x3x4
geometry type: <type 'str'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:smp
mode type: <type 'str'>
nodecount:10
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:False
output type: <type 'bool'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:False
proccount type: <type 'bool'>
project:False
project type: <type 'bool'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:50
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_invalid_geometry_4():
    """
    qsub test run: invalid_geometry_4
        Old Command Output:
          1
          

    """

    args      = """--mode smp -t50 -n10 --geometry 48x48x48x48x2  /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
geometry:[48, 48, 48, 48, 2]
geometry type: <type 'list'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:smp
mode type: <type 'str'>
nodes:10
nodes type: <type 'int'>
outputdir:/tmp
outputdir type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:512
procs type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:50
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:False
error type: <type 'bool'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:48x48x48x48x2
geometry type: <type 'str'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:smp
mode type: <type 'str'>
nodecount:10
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:False
output type: <type 'bool'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:False
proccount type: <type 'bool'>
project:False
project type: <type 'bool'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:50
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_invalid_geometry_5():
    """
    qsub test run: invalid_geometry_5
        Old Command Output:
          Traceback (most recent call last):
            File "oldcmds/qsub.py", line 179, in <module>
              jobspec['geometry'] = parse_geometry_string(opts['geometry'])
            File "/Users/georgerojas/p/Cobalt/cobalt/testsuite/TestCobaltClients/Cobalt/Util.py", line 1112, in parse_geometry_string
              raise ValueError, "%s is an invalid geometry specification." % geometry_str
          ValueError: 48x48x48x48x3 is an invalid geometry specification.
          

    """

    args      = """--mode smp -t50 -n10 --geometry 48x48x48x48x3  /bin/ls"""

    cmdout    = \
"""Invalid geometry entered: 
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_invalid_geometry_6():
    """
    qsub test run: invalid_geometry_6
        Old Command Output:
          1
          

    """

    args      = """--mode smp -t50 -n10 --geometry 128x64x32x4    /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
geometry:[128, 64, 32, 4, 2]
geometry type: <type 'list'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:smp
mode type: <type 'str'>
nodes:10
nodes type: <type 'int'>
outputdir:/tmp
outputdir type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:512
procs type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:50
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:False
error type: <type 'bool'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:128x64x32x4
geometry type: <type 'str'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:smp
mode type: <type 'str'>
nodecount:10
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:False
output type: <type 'bool'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:False
proccount type: <type 'bool'>
project:False
project type: <type 'bool'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:50
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_no_roject_specified():
    """
    qsub test run: no_roject_specified
        Old Command Output:
          Not all required arguments provided: time needed
          
          Usage: qsub [-d] [-v] -A <project name> -q <queue> --cwd <working directory>
                       --dependencies <jobid1>:<jobid2> --preemptable
                       --env envvar1=value1:envvar2=value2 --kernel <kernel profile>
                       -K <kernel options> -O <outputprefix> -t time <in minutes>
                       -e <error file path> -o <output file path> -i <input file path>
                       -n <number of nodes> -h --proccount <processor count> -u <umask>
                       --mode <mode> --debuglog <cobaltlog file path> <command> <args>
                       --users <user1>:<user2> --run_project --disable_preboot
          
          

    """

    args      = """-A -t50 -n10 /bin/ls"""

    cmdout    = \
"""'time' not provided
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_project_specified():
    """
    qsub test run: project_specified
        Old Command Output:
          1
          

    """

    args      = """-A who -t50 -n10 /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:c1
mode type: <type 'str'>
nodes:10
nodes type: <type 'int'>
outputdir:/tmp
outputdir type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:512
procs type: <type 'str'>
project:who
project type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:50
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:False
error type: <type 'bool'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:False
geometry type: <type 'bool'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:False
mode type: <type 'bool'>
nodecount:10
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:False
output type: <type 'bool'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:False
proccount type: <type 'bool'>
project:who
project type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:50
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_Check_attrs_1():
    """
    qsub test run: Check_attrs_1
        Old Command Output:
          1
          

    """

    args      = """--attrs xxxx -t50 -n10 /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
attrs:{'xxxx': 'true'}
attrs type: <type 'dict'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:c1
mode type: <type 'str'>
nodes:10
nodes type: <type 'int'>
outputdir:/tmp
outputdir type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:512
procs type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:50
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{'xxxx': 'true'}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:False
error type: <type 'bool'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:False
geometry type: <type 'bool'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:False
mode type: <type 'bool'>
nodecount:10
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:False
output type: <type 'bool'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:False
proccount type: <type 'bool'>
project:False
project type: <type 'bool'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:50
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_Check_attrs_2():
    """
    qsub test run: Check_attrs_2
        Old Command Output:
          1
          

    """

    args      = """--attrs 1111 -t50 -n10 /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
attrs:{'1111': 'true'}
attrs type: <type 'dict'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:c1
mode type: <type 'str'>
nodes:10
nodes type: <type 'int'>
outputdir:/tmp
outputdir type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:512
procs type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:50
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{'1111': 'true'}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:False
error type: <type 'bool'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:False
geometry type: <type 'bool'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:False
mode type: <type 'bool'>
nodecount:10
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:False
output type: <type 'bool'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:False
proccount type: <type 'bool'>
project:False
project type: <type 'bool'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:50
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_Check_attrs_3():
    """
    qsub test run: Check_attrs_3
        Old Command Output:
          1
          

    """

    args      = """--attrs xx=:yy -t50 -n10 /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
attrs:{'yy': 'true', 'xx': ''}
attrs type: <type 'dict'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:c1
mode type: <type 'str'>
nodes:10
nodes type: <type 'int'>
outputdir:/tmp
outputdir type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:512
procs type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:50
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{'yy': 'true', 'xx': ''}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:False
error type: <type 'bool'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:False
geometry type: <type 'bool'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:False
mode type: <type 'bool'>
nodecount:10
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:False
output type: <type 'bool'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:False
proccount type: <type 'bool'>
project:False
project type: <type 'bool'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:50
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_Check_attrs_4():
    """
    qsub test run: Check_attrs_4
        Old Command Output:
          1
          

    """

    args      = """--attrs xx=one:yy=1:zz=1one -t50 -n10 /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
attrs:{'yy': '1', 'xx': 'one', 'zz': '1one'}
attrs type: <type 'dict'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:c1
mode type: <type 'str'>
nodes:10
nodes type: <type 'int'>
outputdir:/tmp
outputdir type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:512
procs type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:50
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{'yy': '1', 'xx': 'one', 'zz': '1one'}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:False
error type: <type 'bool'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:False
geometry type: <type 'bool'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:False
mode type: <type 'bool'>
nodecount:10
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:False
output type: <type 'bool'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:False
proccount type: <type 'bool'>
project:False
project type: <type 'bool'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:50
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_cwd_option_1():
    """
    qsub test run: cwd_option_1
        Old Command Output:
          1
          

    """

    args      = """--cwd /tmp/ -t10 -n 10 -e p /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp/
cwd type: <type 'str'>
errorpath:/tmp//p
errorpath type: <type 'str'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:c1
mode type: <type 'str'>
nodes:10
nodes type: <type 'int'>
outputdir:/tmp/
outputdir type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:512
procs type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:10
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{}
attrs type: <type 'dict'>
cwd:/tmp/
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:p
error type: <type 'str'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:False
geometry type: <type 'bool'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:False
mode type: <type 'bool'>
nodecount:10
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:False
output type: <type 'bool'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:False
proccount type: <type 'bool'>
project:False
project type: <type 'bool'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:10
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_cwd_option_2():
    """
    qsub test run: cwd_option_2
        Old Command Output:
          1
          

    """

    args      = """--cwd /tmp -t10 -n 10 -e p /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
errorpath:/tmp/p
errorpath type: <type 'str'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:c1
mode type: <type 'str'>
nodes:10
nodes type: <type 'int'>
outputdir:/tmp
outputdir type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:512
procs type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:10
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:p
error type: <type 'str'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:False
geometry type: <type 'bool'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:False
mode type: <type 'bool'>
nodecount:10
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:False
output type: <type 'bool'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:False
proccount type: <type 'bool'>
project:False
project type: <type 'bool'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:10
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_cwd_option_3():
    """
    qsub test run: cwd_option_3
        Old Command Output:
          Error: dir '/x' is not a directory
          

    """

    args      = """--cwd /x -t10 -n 10 -e p /bin/ls"""

    cmdout    = \
"""directory /x/p does not exist
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_cwd_option_4():
    """
    qsub test run: cwd_option_4
        Old Command Output:
          1
          

    """

    args      = """--cwd /tmp/ -t10 -n 10 -e p -o x /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp/
cwd type: <type 'str'>
errorpath:/tmp//p
errorpath type: <type 'str'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:c1
mode type: <type 'str'>
nodes:10
nodes type: <type 'int'>
outputdir:/tmp/
outputdir type: <type 'str'>
outputpath:/tmp//x
outputpath type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:512
procs type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:10
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{}
attrs type: <type 'dict'>
cwd:/tmp/
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:p
error type: <type 'str'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:False
geometry type: <type 'bool'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:False
mode type: <type 'bool'>
nodecount:10
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:x
output type: <type 'str'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:False
proccount type: <type 'bool'>
project:False
project type: <type 'bool'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:10
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_cwd_option_5():
    """
    qsub test run: cwd_option_5
        Old Command Output:
          1
          

    """

    args      = """--cwd /tmp -t10 -n 10 -e p -o x /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
errorpath:/tmp/p
errorpath type: <type 'str'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:c1
mode type: <type 'str'>
nodes:10
nodes type: <type 'int'>
outputdir:/tmp
outputdir type: <type 'str'>
outputpath:/tmp/x
outputpath type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:512
procs type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:10
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:p
error type: <type 'str'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:False
geometry type: <type 'bool'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:False
mode type: <type 'bool'>
nodecount:10
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:x
output type: <type 'str'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:False
proccount type: <type 'bool'>
project:False
project type: <type 'bool'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:10
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_debuglog_option():
    """
    qsub test run: debuglog_option
        Old Command Output:
          1
          

    """

    args      = """-t10 -n 10 -e p -o x --debuglog y /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
cobalt_log_file:/tmp/y
cobalt_log_file type: <type 'str'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
errorpath:/tmp/p
errorpath type: <type 'str'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:c1
mode type: <type 'str'>
nodes:10
nodes type: <type 'int'>
outputdir:/tmp
outputdir type: <type 'str'>
outputpath:/tmp/x
outputpath type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:512
procs type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:10
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:y
debuglog type: <type 'str'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:p
error type: <type 'str'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:False
geometry type: <type 'bool'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:False
mode type: <type 'bool'>
nodecount:10
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:x
output type: <type 'str'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:False
proccount type: <type 'bool'>
project:False
project type: <type 'bool'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:10
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_inputfile_option_1():
    """
    qsub test run: inputfile_option_1
        Old Command Output:
          file /tmp/none not found, or is not a file
          

    """

    args      = """-i none -t10 -n 10 /bin/ls"""

    cmdout    = \
"""file /tmp/none not found, or is not a file
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_inputfile_option_2():
    """
    qsub test run: inputfile_option_2
        Old Command Output:
          1
          

    """

    args      = """-i y -t10 -n 10 /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
inputfile:/tmp/y
inputfile type: <type 'str'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:c1
mode type: <type 'str'>
nodes:10
nodes type: <type 'int'>
outputdir:/tmp
outputdir type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:512
procs type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:10
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:False
error type: <type 'bool'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:False
geometry type: <type 'bool'>
held:False
held type: <type 'bool'>
inputfile:y
inputfile type: <type 'str'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:False
mode type: <type 'bool'>
nodecount:10
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:False
output type: <type 'bool'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:False
proccount type: <type 'bool'>
project:False
project type: <type 'bool'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:10
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_email_option():
    """
    qsub test run: email_option
        Old Command Output:
          1
          

    """

    args      = """-M g -t10 -n10 /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:c1
mode type: <type 'str'>
nodes:10
nodes type: <type 'int'>
notify:g
notify type: <type 'str'>
outputdir:/tmp
outputdir type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:512
procs type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:10
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:False
error type: <type 'bool'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:False
geometry type: <type 'bool'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:False
mode type: <type 'bool'>
nodecount:10
nodecount type: <type 'str'>
notify:g
notify type: <type 'str'>
output:False
output type: <type 'bool'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:False
proccount type: <type 'bool'>
project:False
project type: <type 'bool'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:10
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_outputprefix():
    """
    qsub test run: outputprefix
        Old Command Output:
          WARNING: failed to create cobalt log file at: /tmp.cobaltlog
                   Permission denied
          1
          

    """

    args      = """-O /tmp -t10 -n10 /bin/ls"""

    cmdout    = \
"""1
WARNING: failed to create cobalt log file at: /tmp.cobaltlog
         Permission denied
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
cobalt_log_file:/tmp.cobaltlog
cobalt_log_file type: <type 'str'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
errorpath:/tmp.error
errorpath type: <type 'str'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:c1
mode type: <type 'str'>
nodes:10
nodes type: <type 'int'>
outputdir:/tmp
outputdir type: <type 'str'>
outputpath:/tmp.output
outputpath type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:512
procs type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:10
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:False
error type: <type 'bool'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:False
geometry type: <type 'bool'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:False
mode type: <type 'bool'>
nodecount:10
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:False
output type: <type 'bool'>
outputprefix:/tmp
outputprefix type: <type 'str'>
preemptable:False
preemptable type: <type 'bool'>
proccount:False
proccount type: <type 'bool'>
project:False
project type: <type 'bool'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:10
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_invalid_user():
    """
    qsub test run: invalid_user
        Old Command Output:
          option -r not recognized
          
          Usage: qsub [-d] [-v] -A <project name> -q <queue> --cwd <working directory>
                       --dependencies <jobid1>:<jobid2> --preemptable
                       --env envvar1=value1:envvar2=value2 --kernel <kernel profile>
                       -K <kernel options> -O <outputprefix> -t time <in minutes>
                       -e <error file path> -o <output file path> -i <input file path>
                       -n <number of nodes> -h --proccount <processor count> -u <umask>
                       --mode <mode> --debuglog <cobaltlog file path> <command> <args>
                       --users <user1>:<user2> --run_project --disable_preboot
          
          

    """

    args      = """-run_users naughtyuser -t10 -n10 /bin/ls"""

    cmdout    = \
"""Usage: qsub.py [options] <executable> [<excutable options>]

qsub.py: error: no such option: -r
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       512, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_mode_option_1():
    """
    qsub test run: mode_option_1
        Old Command Output:
          1
          

    """

    args      = """-t10 -n512 --proccount 1023 --mode dual /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:dual
mode type: <type 'str'>
nodes:512
nodes type: <type 'int'>
outputdir:/tmp
outputdir type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:1023
procs type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:10
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:False
error type: <type 'bool'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:False
geometry type: <type 'bool'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:dual
mode type: <type 'str'>
nodecount:512
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:False
output type: <type 'bool'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:1023
proccount type: <type 'str'>
project:False
project type: <type 'bool'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:10
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_mode_option_2():
    """
    qsub test run: mode_option_2
        Old Command Output:
          1
          

    """

    args      = """-t10 -n512 --proccount 1023 --mode vn /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:vn
mode type: <type 'str'>
nodes:512
nodes type: <type 'int'>
outputdir:/tmp
outputdir type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:1023
procs type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:10
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:False
error type: <type 'bool'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:False
geometry type: <type 'bool'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:vn
mode type: <type 'str'>
nodecount:512
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:False
output type: <type 'bool'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:1023
proccount type: <type 'str'>
project:False
project type: <type 'bool'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:10
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_mode_option_3():
    """
    qsub test run: mode_option_3
        Old Command Output:
          1
          

    """

    args      = """--mode co -t50 -n10 --geometry 40x40x50x50 /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
geometry:[40, 40, 50, 50, 2]
geometry type: <type 'list'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:co
mode type: <type 'str'>
nodes:10
nodes type: <type 'int'>
outputdir:/tmp
outputdir type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:512
procs type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:True
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:50
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:False
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:False
error type: <type 'bool'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:40x40x50x50
geometry type: <type 'str'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:co
mode type: <type 'str'>
nodecount:10
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:False
output type: <type 'bool'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:False
proccount type: <type 'bool'>
project:False
project type: <type 'bool'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:50
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_mode_option_4():
    """
    qsub test run: mode_option_4
        Old Command Output:
          Command required
          
          Usage: qsub [-d] [-v] -A <project name> -q <queue> --cwd <working directory>
                       --dependencies <jobid1>:<jobid2> --preemptable
                       --env envvar1=value1:envvar2=value2 --kernel <kernel profile>
                       -K <kernel options> -O <outputprefix> -t time <in minutes>
                       -e <error file path> -o <output file path> -i <input file path>
                       -n <number of nodes> -h --proccount <processor count> -u <umask>
                       --mode <mode> --debuglog <cobaltlog file path> <command> <args>
                       --users <user1>:<user2> --run_project --disable_preboot
          
          

    """

    args      = """-A Acceptance -q testing -n 49152 -t 60 --mode script /bin/ls"""

    cmdout    = \
"""node count out of realistic range
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qsub_preboot_option():
    """
    qsub test run: preboot_option
        Old Command Output:
          1
          

    """

    args      = """--disable_preboot -t10 -n512 --proccount 1023 --mode dual /bin/ls"""

    cmdout    = \
"""1
"""

    stubout   = \
"""
ADD_JOBS

args:[]
args type: <type 'list'>
command:/bin/ls
command type: <type 'str'>
cwd:/tmp
cwd type: <type 'str'>
jobid:*
jobid type: <type 'str'>
kernel:default
kernel type: <type 'str'>
mode:dual
mode type: <type 'str'>
nodes:512
nodes type: <type 'int'>
outputdir:/tmp
outputdir type: <type 'str'>
path:/tmp
path type: <type 'str'>
procs:1023
procs type: <type 'str'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
script_preboot:False
script_preboot type: <type 'bool'>
tag:job
tag type: <type 'str'>
umask:18
umask type: <type 'int'>
user:gooduser
user type: <type 'str'>
user_list:['gooduser']
user_list type: <type 'list'>
walltime:10
walltime type: <type 'str'>

VALIDATE_JOB

attrs:{}
attrs type: <type 'dict'>
cwd:/tmp
cwd type: <type 'str'>
debug:False
debug type: <type 'bool'>
debuglog:False
debuglog type: <type 'bool'>
dependencies:False
dependencies type: <type 'bool'>
disable_preboot:True
disable_preboot type: <type 'bool'>
env:False
env type: <type 'bool'>
error:False
error type: <type 'bool'>
forcenoval:False
forcenoval type: <type 'bool'>
geometry:False
geometry type: <type 'bool'>
held:False
held type: <type 'bool'>
inputfile:False
inputfile type: <type 'bool'>
kernel:default
kernel type: <type 'str'>
kerneloptions:False
kerneloptions type: <type 'bool'>
mode:dual
mode type: <type 'str'>
nodecount:512
nodecount type: <type 'str'>
notify:False
notify type: <type 'bool'>
output:False
output type: <type 'bool'>
outputprefix:False
outputprefix type: <type 'bool'>
preemptable:False
preemptable type: <type 'bool'>
proccount:1023
proccount type: <type 'str'>
project:False
project type: <type 'bool'>
queue:default
queue type: <type 'str'>
run_project:False
run_project type: <type 'bool'>
time:10
time type: <type 'str'>
umask:False
umask type: <type 'bool'>
user_list:False
user_list type: <type 'bool'>
verbose:False
verbose type: <type 'bool'>
version:False
version type: <type 'bool'>

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qsub.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result

