"""
This module defines the test argument information list for schedctl.py and will 
dynamically be imported by testutils.py to generate the tests for schedctl.py.

Refer to the TESTUTILS_README.txt for more information about the usage of this module and testutils.py

test_argslist - is a list of dictionaries, each dictionary has all the necessary info for a test.

"""

test_argslist = [
    { "tc_name" : "args_1", "args" : "", },
    { "tc_name" : "args_2", "args" : """1""", },
    { "tc_name" : "combo_1", "args" : """--start --stop""", "old_args" : "", },
    { "tc_name" : "combo_2", "args" : """--stop --status""", "old_args" : "", },
    { "tc_name" : "combo_3", "args" : """--start --status""", "old_args" : "", },
    { "tc_name" : "combo_4", "args" : """--reread-policy --status""", "old_args" : "", },
    { "tc_name" : "combo_5", "args" : """--score 1.1 --stop""", "old_args" : "", },
    { "tc_name" : "combo_6", "args" : """--inherit 1.1 --start""", "old_args" : "", },
    { "tc_name" : "combo_7", "args" : """--start --savestate /tmp/s""", "old_args" : "", },
    { "tc_name" : "start_1", "args" : """--start 1""", },
    { "tc_name" : "start_2", "args" : """--start""", },
    { "tc_name" : "stop_1", "args" : """--stop  1""", },
    { "tc_name" : "stop_2", "args" : """--stop""", },
    { "tc_name" : "stop_3", "args" : """-d --stop""", "new_only" : True,},
    { "tc_name" : "reread_1", "args" : """--reread-policy 1""", },
    { "tc_name" : "reread_2", "args" : """--reread-policy""", },
    { "tc_name" : "save_1", "args" : """--savestate /tmp/s""", },
    { "tc_name" : "save_2", "args" : """--savestate s""", },
    ]
