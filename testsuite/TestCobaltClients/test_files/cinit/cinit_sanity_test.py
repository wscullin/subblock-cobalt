import testutils

# ---------------------------------------------------------------------------------
def test_partadm_delete_partions():
    """
    partadm test run: delete_partions

        Command Output:
        []
        
        Command Error/Debug:
        
    """

    args      = """-d '*'"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_add_partition_ANL_R00_R01_2048():
    """
    partadm test run: add_partition_ANL_R00_R01_2048

        Command Output:
        [{'scheduled': False, 'name': 'ANL-R00-R01-2048', 'functional': False, 'queue': 'default', 'tag': 'partition', 'deps': None, 'size': 2048}]
        
        Command Error/Debug:
        
    """

    args      = """-a ANL-R00-R01-2048"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_enable_partition_ANL_R00_R01_2048():
    """
    partadm test run: enable_partition_ANL_R00_R01_2048

        Command Output:
        [{'tag': 'partition', 'name': 'ANL-R00-R01-2048'}]
        
        Command Error/Debug:
        
    """

    args      = """--enable ANL-R00-R01-2048"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_activate_partition_ANL_R00_R01_2048():
    """
    partadm test run: activate_partition_ANL_R00_R01_2048

        Command Output:
        [{'tag': 'partition', 'name': 'ANL-R00-R01-2048'}]
        
        Command Error/Debug:
        
    """

    args      = """--activate ANL-R00-R01-2048"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_add_partition_ANL_R00_1024():
    """
    partadm test run: add_partition_ANL_R00_1024

        Command Output:
        [{'scheduled': False, 'name': 'ANL-R00-1024', 'functional': False, 'queue': 'default', 'tag': 'partition', 'deps': None, 'size': 1024}]
        
        Command Error/Debug:
        
    """

    args      = """-a ANL-R00-1024"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_enable_partition_ANL_R00_1024():
    """
    partadm test run: enable_partition_ANL_R00_1024

        Command Output:
        [{'tag': 'partition', 'name': 'ANL-R00-1024'}]
        
        Command Error/Debug:
        
    """

    args      = """--enable ANL-R00-1024"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_activate_partition_ANL_R00_1024():
    """
    partadm test run: activate_partition_ANL_R00_1024

        Command Output:
        [{'tag': 'partition', 'name': 'ANL-R00-1024'}]
        
        Command Error/Debug:
        
    """

    args      = """--activate ANL-R00-1024"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_add_partition_ANL_R01_1024():
    """
    partadm test run: add_partition_ANL_R01_1024

        Command Output:
        [{'scheduled': False, 'name': 'ANL-R01-1024', 'functional': False, 'queue': 'default', 'tag': 'partition', 'deps': None, 'size': 1024}]
        
        Command Error/Debug:
        
    """

    args      = """-a ANL-R01-1024"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_enable_partition_ANL_R01_1024():
    """
    partadm test run: enable_partition_ANL_R01_1024

        Command Output:
        [{'tag': 'partition', 'name': 'ANL-R01-1024'}]
        
        Command Error/Debug:
        
    """

    args      = """--enable ANL-R01-1024"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_activate_partition_ANL_R01_1024():
    """
    partadm test run: activate_partition_ANL_R01_1024

        Command Output:
        [{'tag': 'partition', 'name': 'ANL-R01-1024'}]
        
        Command Error/Debug:
        
    """

    args      = """--activate ANL-R01-1024"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_add_partition_ANL_R00_M0_512():
    """
    partadm test run: add_partition_ANL_R00_M0_512

        Command Output:
        [{'scheduled': False, 'name': 'ANL-R00-M0-512', 'functional': False, 'queue': 'default', 'tag': 'partition', 'deps': None, 'size': 512}]
        
        Command Error/Debug:
        
    """

    args      = """-a ANL-R00-M0-512"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_enable_partition_ANL_R00_M0_512():
    """
    partadm test run: enable_partition_ANL_R00_M0_512

        Command Output:
        [{'tag': 'partition', 'name': 'ANL-R00-M0-512'}]
        
        Command Error/Debug:
        
    """

    args      = """--enable ANL-R00-M0-512"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_activate_partition_ANL_R00_M0_512():
    """
    partadm test run: activate_partition_ANL_R00_M0_512

        Command Output:
        [{'tag': 'partition', 'name': 'ANL-R00-M0-512'}]
        
        Command Error/Debug:
        
    """

    args      = """--activate ANL-R00-M0-512"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_add_partition_ANL_R00_M1_512():
    """
    partadm test run: add_partition_ANL_R00_M1_512

        Command Output:
        [{'scheduled': False, 'name': 'ANL-R00-M1-512', 'functional': False, 'queue': 'default', 'tag': 'partition', 'deps': None, 'size': 512}]
        
        Command Error/Debug:
        
    """

    args      = """-a ANL-R00-M1-512"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_enable_partition_ANL_R00_M1_512():
    """
    partadm test run: enable_partition_ANL_R00_M1_512

        Command Output:
        [{'tag': 'partition', 'name': 'ANL-R00-M1-512'}]
        
        Command Error/Debug:
        
    """

    args      = """--enable ANL-R00-M1-512"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_activate_partition_ANL_R00_M1_512():
    """
    partadm test run: activate_partition_ANL_R00_M1_512

        Command Output:
        [{'tag': 'partition', 'name': 'ANL-R00-M1-512'}]
        
        Command Error/Debug:
        
    """

    args      = """--activate ANL-R00-M1-512"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_add_partition_ANL_R01_M0_512():
    """
    partadm test run: add_partition_ANL_R01_M0_512

        Command Output:
        [{'scheduled': False, 'name': 'ANL-R01-M0-512', 'functional': False, 'queue': 'default', 'tag': 'partition', 'deps': None, 'size': 512}]
        
        Command Error/Debug:
        
    """

    args      = """-a ANL-R01-M0-512"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_enable_partition_ANL_R01_M0_512():
    """
    partadm test run: enable_partition_ANL_R01_M0_512

        Command Output:
        [{'tag': 'partition', 'name': 'ANL-R01-M0-512'}]
        
        Command Error/Debug:
        
    """

    args      = """--enable ANL-R01-M0-512"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_activate_partition_ANL_R01_M0_512():
    """
    partadm test run: activate_partition_ANL_R01_M0_512

        Command Output:
        [{'tag': 'partition', 'name': 'ANL-R01-M0-512'}]
        
        Command Error/Debug:
        
    """

    args      = """--activate ANL-R01-M0-512"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_list_1():
    """
    partadm test run: list_1

        Command Output:
        Name              Queue    Size  Functional  Scheduled  State  Dependencies
        =============================================================================
        ANL-R00-R01-2048  default  2048      X           X      idle               
        ANL-R00-1024      default  1024      X           X      idle               
        ANL-R01-1024      default  1024      X           X      idle               
        ANL-R00-M0-512    default  512       X           X      idle               
        ANL-R00-M1-512    default  512       X           X      idle               
        ANL-R01-M0-512    default  512       X           X      idle               
        
        Command Error/Debug:
        
    """

    args      = """-l"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_delete_default_que():
    """
    cqadm test run: delete_default_que

        Command Output:
        Deleted Queues  
        ================
        
        Command Error/Debug:Failed to match any jobs or queues
        
        
    """

    args      = """--delq default"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_add_queues():
    """
    cqadm test run: add_queues

        Command Output:
        Added Queues  
        ==============
        default       
        q_4           
        q_3           
        q_2           
        q_1           
        
        Command Error/Debug:
        
    """

    args      = """--addq default q_1 q_2 q_3 q_4"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_start_default():
    """
    cqadm test run: start_default

        Command Output:
        
        Command Error/Debug:
        
    """

    args      = """--start default q_1 q_2 q_3 q_4"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_get_queues():
    """
    cqadm test run: get_queues

        Command Output:
        Queue    Users  MinTime  MaxTime  MaxRunning  MaxQueued  MaxUserNodes  MaxNodeHours  TotalNodes  AdminEmail  State    Cron  Policy   Priority  
        ===============================================================================================================================================
        default  None   None     None     None        None       None          None          None        None        running  None  default  0         
        q_1      None   None     None     None        None       None          None          None        None        running  None  default  0         
        q_2      None   None     None     None        None       None          None          None        None        running  None  default  0         
        q_3      None   None     None     None        None       None          None          None        None        running  None  default  0         
        q_4      None   None     None     None        None       None          None          None        None        running  None  default  0         
        
        Command Error/Debug:
        
    """

    args      = """--getq"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qstat_qstat_1():
    """
    qstat test run: qstat_1

        Command Output:
        Name     Users  MinTime  MaxTime  MaxRunning  MaxQueued  MaxUserNodes  MaxNodeHours  TotalNodes  State    
        ==========================================================================================================
        default  None   None     None     None        None       None          None          None        running  
        q_1      None   None     None     None        None       None          None          None        running  
        q_2      None   None     None     None        None       None          None          None        running  
        q_3      None   None     None     None        None       None          None          None        running  
        q_4      None   None     None     None        None       None          None          None        running  
        
        Command Error/Debug:
        
    """

    args      = """-Q"""
    exp_rs    = 0

    results = testutils.run_cmd('qstat.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_add_que_associations_1():
    """
    partadm test run: add_que_associations_1

        Command Output:
        [{'tag': 'partition', 'name': 'ANL-R00-1024'}, {'tag': 'partition', 'name': 'ANL-R00-R01-2048'}]
        
        Command Error/Debug:
        
    """

    args      = """--queue q_1:q_2:q_3:q_4 ANL-R00-R01-2048 ANL-R00-1024"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_list_3():
    """
    partadm test run: list_3

        Command Output:
        Name              Queue            Size  Functional  Scheduled  State  Dependencies
        =====================================================================================
        ANL-R00-R01-2048  q_1:q_2:q_3:q_4  2048      X           X      idle               
        ANL-R00-1024      q_1:q_2:q_3:q_4  1024      X           X      idle               
        ANL-R01-1024      default          1024      X           X      idle               
        ANL-R00-M0-512    default          512       X           X      idle               
        ANL-R00-M1-512    default          512       X           X      idle               
        ANL-R01-M0-512    default          512       X           X      idle               
        
        Command Error/Debug:
        
    """

    args      = """-l"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_add_que_associations_2():
    """
    partadm test run: add_que_associations_2

        Command Output:
        [{'tag': 'partition', 'name': 'ANL-R00-M1-512'}, {'tag': 'partition', 'name': 'ANL-R01-1024'}]
        
        Command Error/Debug:
        
    """

    args      = """--queue q_1:q_2:q_3:q_4 ANL-R01-1024 ANL-R00-M1-512"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_list_4():
    """
    partadm test run: list_4

        Command Output:
        Name              Queue            Size  Functional  Scheduled  State  Dependencies
        =====================================================================================
        ANL-R00-R01-2048  q_1:q_2:q_3:q_4  2048      X           X      idle               
        ANL-R00-1024      q_1:q_2:q_3:q_4  1024      X           X      idle               
        ANL-R01-1024      q_1:q_2:q_3:q_4  1024      X           X      idle               
        ANL-R00-M0-512    default          512       X           X      idle               
        ANL-R00-M1-512    q_1:q_2:q_3:q_4  512       X           X      idle               
        ANL-R01-M0-512    default          512       X           X      idle               
        
        Command Error/Debug:
        
    """

    args      = """-l"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_add_que_associations_3():
    """
    partadm test run: add_que_associations_3

        Command Output:
        [{'tag': 'partition', 'name': 'ANL-R00-M0-512'}]
        
        Command Error/Debug:
        
    """

    args      = """--queue default:q_1 ANL-R00-M0-512"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_list_5():
    """
    partadm test run: list_5

        Command Output:
        Name              Queue            Size  Functional  Scheduled  State  Dependencies
        =====================================================================================
        ANL-R00-R01-2048  q_1:q_2:q_3:q_4  2048      X           X      idle               
        ANL-R00-1024      q_1:q_2:q_3:q_4  1024      X           X      idle               
        ANL-R01-1024      q_1:q_2:q_3:q_4  1024      X           X      idle               
        ANL-R00-M0-512    default:q_1      512       X           X      idle               
        ANL-R00-M1-512    q_1:q_2:q_3:q_4  512       X           X      idle               
        ANL-R01-M0-512    default          512       X           X      idle               
        
        Command Error/Debug:
        
    """

    args      = """-l"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_rmq_1():
    """
    partadm test run: rmq_1

        Command Output:
        [[{'tag': 'partition', 'name': 'ANL-R00-R01-2048'}], [{'tag': 'partition', 'name': 'ANL-R00-1024'}]]
        
        Command Error/Debug:
        
    """

    args      = """--queue q_3 --rmq ANL-R00-R01-2048 ANL-R00-1024"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_list_6():
    """
    partadm test run: list_6

        Command Output:
        Name              Queue            Size  Functional  Scheduled  State  Dependencies
        =====================================================================================
        ANL-R00-R01-2048  q_1:q_2:q_4      2048      X           X      idle               
        ANL-R00-1024      q_1:q_2:q_4      1024      X           X      idle               
        ANL-R01-1024      q_1:q_2:q_3:q_4  1024      X           X      idle               
        ANL-R00-M0-512    default:q_1      512       X           X      idle               
        ANL-R00-M1-512    q_1:q_2:q_3:q_4  512       X           X      idle               
        ANL-R01-M0-512    default          512       X           X      idle               
        
        Command Error/Debug:
        
    """

    args      = """-l"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_rmq_2():
    """
    partadm test run: rmq_2

        Command Output:
        [[{'tag': 'partition', 'name': 'ANL-R00-R01-2048'}]]
        
        Command Error/Debug:
        
    """

    args      = """--queue q_2 --rmq ANL-R00-R01-2048"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_list_7():
    """
    partadm test run: list_7

        Command Output:
        Name              Queue            Size  Functional  Scheduled  State  Dependencies
        =====================================================================================
        ANL-R00-R01-2048  q_1:q_4          2048      X           X      idle               
        ANL-R00-1024      q_1:q_2:q_4      1024      X           X      idle               
        ANL-R01-1024      q_1:q_2:q_3:q_4  1024      X           X      idle               
        ANL-R00-M0-512    default:q_1      512       X           X      idle               
        ANL-R00-M1-512    q_1:q_2:q_3:q_4  512       X           X      idle               
        ANL-R01-M0-512    default          512       X           X      idle               
        
        Command Error/Debug:
        
    """

    args      = """-l"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_appq_1():
    """
    partadm test run: appq_1

        Command Output:
        [[{'tag': 'partition', 'name': 'ANL-R00-R01-2048'}], [{'tag': 'partition', 'name': 'ANL-R00-1024'}]]
        
        Command Error/Debug:
        
    """

    args      = """--queue q_3 --appq ANL-R00-R01-2048 ANL-R00-1024"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_list_8():
    """
    partadm test run: list_8

        Command Output:
        Name              Queue            Size  Functional  Scheduled  State  Dependencies
        =====================================================================================
        ANL-R00-R01-2048  q_1:q_4:q_3      2048      X           X      idle               
        ANL-R00-1024      q_1:q_2:q_4:q_3  1024      X           X      idle               
        ANL-R01-1024      q_1:q_2:q_3:q_4  1024      X           X      idle               
        ANL-R00-M0-512    default:q_1      512       X           X      idle               
        ANL-R00-M1-512    q_1:q_2:q_3:q_4  512       X           X      idle               
        ANL-R01-M0-512    default          512       X           X      idle               
        
        Command Error/Debug:
        
    """

    args      = """-l"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_appq_2():
    """
    partadm test run: appq_2

        Command Output:
        [[{'tag': 'partition', 'name': 'ANL-R00-R01-2048'}]]
        
        Command Error/Debug:
        
    """

    args      = """--queue q_2 --appq ANL-R00-R01-2048"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_partadm_list_9():
    """
    partadm test run: list_9

        Command Output:
        Name              Queue            Size  Functional  Scheduled  State  Dependencies
        =====================================================================================
        ANL-R00-R01-2048  q_1:q_4:q_3:q_2  2048      X           X      idle               
        ANL-R00-1024      q_1:q_2:q_4:q_3  1024      X           X      idle               
        ANL-R01-1024      q_1:q_2:q_3:q_4  1024      X           X      idle               
        ANL-R00-M0-512    default:q_1      512       X           X      idle               
        ANL-R00-M1-512    q_1:q_2:q_3:q_4  512       X           X      idle               
        ANL-R01-M0-512    default          512       X           X      idle               
        
        Command Error/Debug:
        
    """

    args      = """-l"""
    exp_rs    = 0

    results = testutils.run_cmd('partadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qstat_qstat_2():
    """
    qstat test run: qstat_2

        Command Output:
        Name     Users  MinTime  MaxTime  MaxRunning  MaxQueued  MaxUserNodes  MaxNodeHours  TotalNodes  State    
        ==========================================================================================================
        default  None   None     None     None        None       None          None          None        running  
        q_1      None   None     None     None        None       None          None          None        running  
        q_2      None   None     None     None        None       None          None          None        running  
        q_3      None   None     None     None        None       None          None          None        running  
        q_4      None   None     None     None        None       None          None          None        running  
        
        Command Error/Debug:
        
    """

    args      = """-Q"""
    exp_rs    = 0

    results = testutils.run_cmd('qstat.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_setres_setres_1():
    """
    setres test run: setres_1

        Command Output:
        Got starttime Wed Jun  7 02:32:00 2023 +0000 (UTC)
        [{'project': None, 'users': None, 'block_passthrough': False, 'name': 'george', 'queue': 'q_1', 'start': 1686105120.0, 'duration': 3000, 'cycle': None, 'res_id': 1, 'partitions': 'ANL-R00-R01-2048'}]
        
        
        Command Error/Debug:
        
    """

    args      = """-n george -s 2023_6_6-21:32 -d 50  -q q_1 ANL-R00-R01-2048"""
    exp_rs    = 0

    results = testutils.run_cmd('setres.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_showres_showres_1():
    """
    showres test run: showres_1

        Command Output:
        Reservation  Queue  User  Start                                 Duration  End Time                              Cycle Time  Passthrough  Partitions        Project  ResID  CycleID  
        ====================================================================================================================================================================================
        george       q_1    None  Wed Jun  7 02:32:00 2023 +0000 (UTC)  00:50     Wed Jun  7 03:22:00 2023 +0000 (UTC)  None        Allowed      ANL-R00-R01-2048  None     1      -        
        
        Command Error/Debug:
        
    """

    args      = """-x"""
    exp_rs    = 0

    results = testutils.run_cmd('showres.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_setres_setres_2():
    """
    setres test run: setres_2

        Command Output:
        
        
        Command Error/Debug:
        
    """

    args      = """-n george -m -d 300"""
    exp_rs    = 0

    results = testutils.run_cmd('setres.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_showres_showres_2():
    """
    showres test run: showres_2

        Command Output:
        Reservation  Queue  User  Start                                 Duration  End Time                              Cycle Time  Passthrough  Partitions        Project  ResID  CycleID  
        ====================================================================================================================================================================================
        george       q_1    None  Wed Jun  7 02:32:00 2023 +0000 (UTC)  05:00     Wed Jun  7 07:32:00 2023 +0000 (UTC)  None        Allowed      ANL-R00-R01-2048  None     1      -        
        
        Command Error/Debug:
        
    """

    args      = """-x"""
    exp_rs    = 0

    results = testutils.run_cmd('showres.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_setres_setres_3():
    """
    setres test run: setres_3

        Command Output:
        Got starttime Wed Dec  1 16:30:00 2010 +0000 (UTC)
        [{'project': None, 'users': None, 'block_passthrough': False, 'name': 'res_passed', 'queue': 'q_1', 'start': 1291221000.0, 'duration': 3000, 'cycle': None, 'res_id': 2, 'partitions': 'ANL-R00-R01-2048'}]
        
        
        Command Error/Debug:
        
    """

    args      = """-n res_passed -s 2010_12_1-10:30 -d 50  -q q_1 ANL-R00-R01-2048"""
    exp_rs    = 0

    results = testutils.run_cmd('setres.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_showres_showres_3():
    """
    showres test run: showres_3

        Command Output:
        Reservation  Queue  User  Start                                 Duration  End Time                              Cycle Time  Passthrough  Partitions        Project  ResID  CycleID  
        ====================================================================================================================================================================================
        res_passed   q_1    None  Wed Dec  1 16:30:00 2010 +0000 (UTC)  00:50     Wed Dec  1 17:20:00 2010 +0000 (UTC)  None        Allowed      ANL-R00-R01-2048  None     2      -        
        george       q_1    None  Wed Jun  7 02:32:00 2023 +0000 (UTC)  05:00     Wed Jun  7 07:32:00 2023 +0000 (UTC)  None        Allowed      ANL-R00-R01-2048  None     1      -        
        
        Command Error/Debug:
        
    """

    args      = """-x"""
    exp_rs    = 0

    results = testutils.run_cmd('showres.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qsub_qsub_1():
    """
    qsub test run: qsub_1

        Command Output:
        1
        
        Command Error/Debug:
        
    """

    args      = """-h -t 50  -n 30 /bin/ls"""
    exp_rs    = 0

    results = testutils.run_cmd('qsub.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qsub_qsub_2():
    """
    qsub test run: qsub_2

        Command Output:
        2
        
        Command Error/Debug:
        
    """

    args      = """-h -t 100 -n 30 /bin/ls"""
    exp_rs    = 0

    results = testutils.run_cmd('qsub.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qsub_qsub_3():
    """
    qsub test run: qsub_3

        Command Output:
        3
        
        Command Error/Debug:
        
    """

    args      = """-h -t 150 -n 30 /bin/ls"""
    exp_rs    = 0

    results = testutils.run_cmd('qsub.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qsub_qsub_4():
    """
    qsub test run: qsub_4

        Command Output:
        4
        
        Command Error/Debug:
        
    """

    args      = """--dep 1:2:3 -t 150 -n 30 /bin/ls"""
    exp_rs    = 0

    results = testutils.run_cmd('qsub.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qsub_qsub_5():
    """
    qsub test run: qsub_5

        Command Output:
        5
        
        Command Error/Debug:WARNING: dependencies 60 do not match jobs currently in the queue
        
        
    """

    args      = """--dep 1:2:3:4:60 -t 150 -n 30 /bin/ls"""
    exp_rs    = 0

    results = testutils.run_cmd('qsub.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qstat_qstat_3():
    """
    qstat test run: qstat_3

        Command Output:
        JobID  User         WallTime  Nodes  State      Location  
        ==========================================================
        1      georgerojas  00:50:00  30     user_hold  None      
        2      georgerojas  01:40:00  30     user_hold  None      
        3      georgerojas  02:30:00  30     user_hold  None      
        4      georgerojas  02:30:00  30     dep_hold   None      
        5      georgerojas  02:30:00  30     dep_hold   None      
        
        Command Error/Debug:
        
    """

    args      = ''
    exp_rs    = 0

    results = testutils.run_cmd('qstat.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qalter_qalter_1():
    """
    qalter test run: qalter_1

        Command Output:
        walltime changed from 50 to 60.0
        walltime changed from 100 to 110.0
        walltime changed from 150 to 160.0
        walltime changed from 150 to 160.0
        walltime changed from 150 to 160.0
        
        Command Error/Debug:
        qalter.py --debug -t +10 1 2 3 4 5
        
        component: "queue-manager.get_jobs", defer: False
          get_jobs(
             [{'is_active': '*', 'tag': 'job', 'notify': '*', 'procs': '*', 'walltime': '*', 'queue': '*', 'jobid': 1, 'project': '*', 'mode': '*', 'nodes': '*', 'user': 'georgerojas'}, {'is_active': '*', 'tag': 'job', 'notify': '*', 'procs': '*', 'walltime': '*', 'queue': '*', 'jobid': 2, 'project': '*', 'mode': '*', 'nodes': '*', 'user': 'georgerojas'}, {'is_active': '*', 'tag': 'job', 'notify': '*', 'procs': '*', 'walltime': '*', 'queue': '*', 'jobid': 3, 'project': '*', 'mode': '*', 'nodes': '*', 'user': 'georgerojas'}, {'is_active': '*', 'tag': 'job', 'notify': '*', 'procs': '*', 'walltime': '*', 'queue': '*', 'jobid': 4, 'project': '*', 'mode': '*', 'nodes': '*', 'user': 'georgerojas'}, {'is_active': '*', 'tag': 'job', 'notify': '*', 'procs': '*', 'walltime': '*', 'queue': '*', 'jobid': 5, 'project': '*', 'mode': '*', 'nodes': '*', 'user': 'georgerojas'}],
             )
        
        
        component: "queue-manager.set_jobs", defer: False
          set_jobs(
             [{'project': None, 'user': 'georgerojas', 'jobid': 1, 'queue': 'default', 'tag': 'job', 'mode': 'smp', 'nodes': 30, 'walltime': 50, 'procs': 30, 'notify': None}],
             {'queue': 'default', 'mode': 'smp', 'jobid': 1, 'project': None, 'tag': 'job', 'notify': None, 'nodes': 30, 'walltime': '60.0', 'procs': 30, 'user': 'georgerojas'},
             georgerojas,
             )
        
        
        component: "queue-manager.set_jobs", defer: False
          set_jobs(
             [{'project': None, 'user': 'georgerojas', 'jobid': 2, 'queue': 'default', 'tag': 'job', 'mode': 'smp', 'nodes': 30, 'walltime': 100, 'procs': 30, 'notify': None}],
             {'queue': 'default', 'mode': 'smp', 'jobid': 2, 'project': None, 'tag': 'job', 'notify': None, 'nodes': 30, 'walltime': '110.0', 'procs': 30, 'user': 'georgerojas'},
             georgerojas,
             )
        
        
        component: "queue-manager.set_jobs", defer: False
          set_jobs(
             [{'project': None, 'user': 'georgerojas', 'jobid': 4, 'queue': 'default', 'tag': 'job', 'mode': 'smp', 'nodes': 30, 'walltime': 150, 'procs': 30, 'notify': None}],
             {'queue': 'default', 'mode': 'smp', 'jobid': 4, 'project': None, 'tag': 'job', 'notify': None, 'nodes': 30, 'walltime': '160.0', 'procs': 30, 'user': 'georgerojas'},
             georgerojas,
             )
        
        
        component: "queue-manager.set_jobs", defer: False
          set_jobs(
             [{'project': None, 'user': 'georgerojas', 'jobid': 5, 'queue': 'default', 'tag': 'job', 'mode': 'smp', 'nodes': 30, 'walltime': 150, 'procs': 30, 'notify': None}],
             {'queue': 'default', 'mode': 'smp', 'jobid': 5, 'project': None, 'tag': 'job', 'notify': None, 'nodes': 30, 'walltime': '160.0', 'procs': 30, 'user': 'georgerojas'},
             georgerojas,
             )
        
        
        component: "queue-manager.set_jobs", defer: False
          set_jobs(
             [{'project': None, 'user': 'georgerojas', 'jobid': 3, 'queue': 'default', 'tag': 'job', 'mode': 'smp', 'nodes': 30, 'walltime': 150, 'procs': 30, 'notify': None}],
             {'queue': 'default', 'mode': 'smp', 'jobid': 3, 'project': None, 'tag': 'job', 'notify': None, 'nodes': 30, 'walltime': '160.0', 'procs': 30, 'user': 'georgerojas'},
             georgerojas,
             )
        
        
        [{'project': None, 'user': 'georgerojas', 'jobid': 3, 'queue': 'default', 'tag': 'job', 'mode': 'smp', 'nodes': 30, 'walltime': 160, 'procs': 30, 'notify': None}]
        
        
    """

    args      = """--debug  -t +10 1 2 3 4 5"""
    exp_rs    = 0

    results = testutils.run_cmd('qalter.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qstat_qstat_4():
    """
    qstat test run: qstat_4

        Command Output:
        JobID  User         WallTime  Nodes  State      Location  
        ==========================================================
        1      georgerojas  01:00:00  30     user_hold  None      
        2      georgerojas  01:50:00  30     user_hold  None      
        3      georgerojas  02:40:00  30     user_hold  None      
        4      georgerojas  02:40:00  30     dep_hold   None      
        5      georgerojas  02:40:00  30     dep_fail   None      
        
        Command Error/Debug:
        
    """

    args      = ''
    exp_rs    = 0

    results = testutils.run_cmd('qstat.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qalter_qalter_2():
    """
    qalter test run: qalter_2

        Command Output:
        walltime changed from 60 to 55.0
        walltime changed from 110 to 105.0
        walltime changed from 160 to 155.0
        walltime changed from 160 to 155.0
        walltime changed from 160 to 155.0
        
        Command Error/Debug:
        qalter.py --debug -t -5 1 2 3 4 5
        
        component: "queue-manager.get_jobs", defer: False
          get_jobs(
             [{'is_active': '*', 'tag': 'job', 'notify': '*', 'procs': '*', 'walltime': '*', 'queue': '*', 'jobid': 1, 'project': '*', 'mode': '*', 'nodes': '*', 'user': 'georgerojas'}, {'is_active': '*', 'tag': 'job', 'notify': '*', 'procs': '*', 'walltime': '*', 'queue': '*', 'jobid': 2, 'project': '*', 'mode': '*', 'nodes': '*', 'user': 'georgerojas'}, {'is_active': '*', 'tag': 'job', 'notify': '*', 'procs': '*', 'walltime': '*', 'queue': '*', 'jobid': 3, 'project': '*', 'mode': '*', 'nodes': '*', 'user': 'georgerojas'}, {'is_active': '*', 'tag': 'job', 'notify': '*', 'procs': '*', 'walltime': '*', 'queue': '*', 'jobid': 4, 'project': '*', 'mode': '*', 'nodes': '*', 'user': 'georgerojas'}, {'is_active': '*', 'tag': 'job', 'notify': '*', 'procs': '*', 'walltime': '*', 'queue': '*', 'jobid': 5, 'project': '*', 'mode': '*', 'nodes': '*', 'user': 'georgerojas'}],
             )
        
        
        component: "queue-manager.set_jobs", defer: False
          set_jobs(
             [{'project': None, 'user': 'georgerojas', 'jobid': 1, 'queue': 'default', 'tag': 'job', 'mode': 'smp', 'nodes': 30, 'walltime': 60, 'procs': 30, 'notify': None}],
             {'queue': 'default', 'mode': 'smp', 'jobid': 1, 'project': None, 'tag': 'job', 'notify': None, 'nodes': 30, 'walltime': '55.0', 'procs': 30, 'user': 'georgerojas'},
             georgerojas,
             )
        
        
        component: "queue-manager.set_jobs", defer: False
          set_jobs(
             [{'project': None, 'user': 'georgerojas', 'jobid': 2, 'queue': 'default', 'tag': 'job', 'mode': 'smp', 'nodes': 30, 'walltime': 110, 'procs': 30, 'notify': None}],
             {'queue': 'default', 'mode': 'smp', 'jobid': 2, 'project': None, 'tag': 'job', 'notify': None, 'nodes': 30, 'walltime': '105.0', 'procs': 30, 'user': 'georgerojas'},
             georgerojas,
             )
        
        
        component: "queue-manager.set_jobs", defer: False
          set_jobs(
             [{'project': None, 'user': 'georgerojas', 'jobid': 4, 'queue': 'default', 'tag': 'job', 'mode': 'smp', 'nodes': 30, 'walltime': 160, 'procs': 30, 'notify': None}],
             {'queue': 'default', 'mode': 'smp', 'jobid': 4, 'project': None, 'tag': 'job', 'notify': None, 'nodes': 30, 'walltime': '155.0', 'procs': 30, 'user': 'georgerojas'},
             georgerojas,
             )
        
        
        component: "queue-manager.set_jobs", defer: False
          set_jobs(
             [{'project': None, 'user': 'georgerojas', 'jobid': 3, 'queue': 'default', 'tag': 'job', 'mode': 'smp', 'nodes': 30, 'walltime': 160, 'procs': 30, 'notify': None}],
             {'queue': 'default', 'mode': 'smp', 'jobid': 3, 'project': None, 'tag': 'job', 'notify': None, 'nodes': 30, 'walltime': '155.0', 'procs': 30, 'user': 'georgerojas'},
             georgerojas,
             )
        
        
        component: "queue-manager.set_jobs", defer: False
          set_jobs(
             [{'project': None, 'user': 'georgerojas', 'jobid': 5, 'queue': 'default', 'tag': 'job', 'mode': 'smp', 'nodes': 30, 'walltime': 160, 'procs': 30, 'notify': None}],
             {'queue': 'default', 'mode': 'smp', 'jobid': 5, 'project': None, 'tag': 'job', 'notify': None, 'nodes': 30, 'walltime': '155.0', 'procs': 30, 'user': 'georgerojas'},
             georgerojas,
             )
        
        
        [{'project': None, 'user': 'georgerojas', 'jobid': 5, 'queue': 'default', 'tag': 'job', 'mode': 'smp', 'nodes': 30, 'walltime': 155, 'procs': 30, 'notify': None}]
        
        
    """

    args      = """--debug  -t -5 1 2 3 4 5"""
    exp_rs    = 0

    results = testutils.run_cmd('qalter.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qstat_qstat_5():
    """
    qstat test run: qstat_5

        Command Output:
        JobID  User         WallTime  Nodes  State      Location  
        ==========================================================
        1      georgerojas  00:55:00  30     user_hold  None      
        2      georgerojas  01:45:00  30     user_hold  None      
        3      georgerojas  02:35:00  30     user_hold  None      
        4      georgerojas  02:35:00  30     dep_hold   None      
        5      georgerojas  02:35:00  30     dep_fail   None      
        
        Command Error/Debug:
        
    """

    args      = ''
    exp_rs    = 0

    results = testutils.run_cmd('qstat.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qalter_qalter_3():
    """
    qalter test run: qalter_3

        Command Output:
        walltime changed from 55 to 65.0
        walltime changed from 105 to 115.0
        walltime changed from 155 to 165.0
        walltime changed from 155 to 165.0
        walltime changed from 155 to 165.0
        
        Command Error/Debug:
        qalter.py --debug -t +10 1 2 3 4 5
        
        component: "queue-manager.get_jobs", defer: False
          get_jobs(
             [{'is_active': '*', 'tag': 'job', 'notify': '*', 'procs': '*', 'walltime': '*', 'queue': '*', 'jobid': 1, 'project': '*', 'mode': '*', 'nodes': '*', 'user': 'georgerojas'}, {'is_active': '*', 'tag': 'job', 'notify': '*', 'procs': '*', 'walltime': '*', 'queue': '*', 'jobid': 2, 'project': '*', 'mode': '*', 'nodes': '*', 'user': 'georgerojas'}, {'is_active': '*', 'tag': 'job', 'notify': '*', 'procs': '*', 'walltime': '*', 'queue': '*', 'jobid': 3, 'project': '*', 'mode': '*', 'nodes': '*', 'user': 'georgerojas'}, {'is_active': '*', 'tag': 'job', 'notify': '*', 'procs': '*', 'walltime': '*', 'queue': '*', 'jobid': 4, 'project': '*', 'mode': '*', 'nodes': '*', 'user': 'georgerojas'}, {'is_active': '*', 'tag': 'job', 'notify': '*', 'procs': '*', 'walltime': '*', 'queue': '*', 'jobid': 5, 'project': '*', 'mode': '*', 'nodes': '*', 'user': 'georgerojas'}],
             )
        
        
        component: "queue-manager.set_jobs", defer: False
          set_jobs(
             [{'project': None, 'user': 'georgerojas', 'jobid': 1, 'queue': 'default', 'tag': 'job', 'mode': 'smp', 'nodes': 30, 'walltime': 55, 'procs': 30, 'notify': None}],
             {'queue': 'default', 'mode': 'smp', 'jobid': 1, 'project': None, 'tag': 'job', 'notify': None, 'nodes': 30, 'walltime': '65.0', 'procs': 30, 'user': 'georgerojas'},
             georgerojas,
             )
        
        
        component: "queue-manager.set_jobs", defer: False
          set_jobs(
             [{'project': None, 'user': 'georgerojas', 'jobid': 2, 'queue': 'default', 'tag': 'job', 'mode': 'smp', 'nodes': 30, 'walltime': 105, 'procs': 30, 'notify': None}],
             {'queue': 'default', 'mode': 'smp', 'jobid': 2, 'project': None, 'tag': 'job', 'notify': None, 'nodes': 30, 'walltime': '115.0', 'procs': 30, 'user': 'georgerojas'},
             georgerojas,
             )
        
        
        component: "queue-manager.set_jobs", defer: False
          set_jobs(
             [{'project': None, 'user': 'georgerojas', 'jobid': 4, 'queue': 'default', 'tag': 'job', 'mode': 'smp', 'nodes': 30, 'walltime': 155, 'procs': 30, 'notify': None}],
             {'queue': 'default', 'mode': 'smp', 'jobid': 4, 'project': None, 'tag': 'job', 'notify': None, 'nodes': 30, 'walltime': '165.0', 'procs': 30, 'user': 'georgerojas'},
             georgerojas,
             )
        
        
        component: "queue-manager.set_jobs", defer: False
          set_jobs(
             [{'project': None, 'user': 'georgerojas', 'jobid': 5, 'queue': 'default', 'tag': 'job', 'mode': 'smp', 'nodes': 30, 'walltime': 155, 'procs': 30, 'notify': None}],
             {'queue': 'default', 'mode': 'smp', 'jobid': 5, 'project': None, 'tag': 'job', 'notify': None, 'nodes': 30, 'walltime': '165.0', 'procs': 30, 'user': 'georgerojas'},
             georgerojas,
             )
        
        
        component: "queue-manager.set_jobs", defer: False
          set_jobs(
             [{'project': None, 'user': 'georgerojas', 'jobid': 3, 'queue': 'default', 'tag': 'job', 'mode': 'smp', 'nodes': 30, 'walltime': 155, 'procs': 30, 'notify': None}],
             {'queue': 'default', 'mode': 'smp', 'jobid': 3, 'project': None, 'tag': 'job', 'notify': None, 'nodes': 30, 'walltime': '165.0', 'procs': 30, 'user': 'georgerojas'},
             georgerojas,
             )
        
        
        [{'project': None, 'user': 'georgerojas', 'jobid': 3, 'queue': 'default', 'tag': 'job', 'mode': 'smp', 'nodes': 30, 'walltime': 165, 'procs': 30, 'notify': None}]
        
        
    """

    args      = """--debug  -t +10 1 2 3 4 5"""
    exp_rs    = 0

    results = testutils.run_cmd('qalter.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qstat_qstat_6():
    """
    qstat test run: qstat_6

        Command Output:
        JobID  User         WallTime  Nodes  State      Location  
        ==========================================================
        1      georgerojas  01:05:00  30     user_hold  None      
        2      georgerojas  01:55:00  30     user_hold  None      
        3      georgerojas  02:45:00  30     user_hold  None      
        4      georgerojas  02:45:00  30     dep_hold   None      
        5      georgerojas  02:45:00  30     dep_fail   None      
        
        Command Error/Debug:
        
    """

    args      = ''
    exp_rs    = 0

    results = testutils.run_cmd('qstat.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qrls_qrls_1():
    """
    qrls test run: qrls_1

        Command Output:
           Failed to remove user hold on jobs: 
              job 4 does not have a 'user hold'
              job 5 does not have a 'user hold'
           Removed user hold on jobs: 
              1
              2
              3
        
        Command Error/Debug:
        qrls.py -d 1 2 3 4 5
        
        component: "queue-manager.get_jobs", defer: False
          get_jobs(
             [{'user_hold': '*', 'tag': 'job', 'user': 'georgerojas', 'jobid': 1}, {'user_hold': '*', 'tag': 'job', 'user': 'georgerojas', 'jobid': 2}, {'user_hold': '*', 'tag': 'job', 'user': 'georgerojas', 'jobid': 3}, {'user_hold': '*', 'tag': 'job', 'user': 'georgerojas', 'jobid': 4}, {'user_hold': '*', 'tag': 'job', 'user': 'georgerojas', 'jobid': 5}],
             )
        
        
        component: "queue-manager.set_jobs", defer: False
          set_jobs(
             [{'user_hold': '*', 'tag': 'job', 'is_active': '*', 'user': 'georgerojas', 'jobid': 1}, {'user_hold': '*', 'tag': 'job', 'is_active': '*', 'user': 'georgerojas', 'jobid': 2}, {'user_hold': '*', 'tag': 'job', 'is_active': '*', 'user': 'georgerojas', 'jobid': 4}, {'user_hold': '*', 'tag': 'job', 'is_active': '*', 'user': 'georgerojas', 'jobid': 3}, {'user_hold': '*', 'tag': 'job', 'is_active': '*', 'user': 'georgerojas', 'jobid': 5}],
             {'user_hold': False},
             georgerojas,
             )
        
        
        Response: [{'user_hold': False, 'tag': 'job', 'is_active': False, 'user': 'georgerojas', 'jobid': 1}, {'user_hold': False, 'tag': 'job', 'is_active': False, 'user': 'georgerojas', 'jobid': 2}, {'user_hold': False, 'tag': 'job', 'is_active': False, 'user': 'georgerojas', 'jobid': 4}, {'user_hold': False, 'tag': 'job', 'is_active': False, 'user': 'georgerojas', 'jobid': 3}, {'user_hold': False, 'tag': 'job', 'is_active': False, 'user': 'georgerojas', 'jobid': 5}]
        
        
    """

    args      = """-d 1 2 3 4 5"""
    exp_rs    = 0

    results = testutils.run_cmd('qrls.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qstat_qstat_7():
    """
    qstat test run: qstat_7

        Command Output:
        JobID  User         WallTime  Nodes  State     Location  
        =========================================================
        1      georgerojas  01:05:00  30     queued    None      
        2      georgerojas  01:55:00  30     queued    None      
        3      georgerojas  02:45:00  30     queued    None      
        4      georgerojas  02:45:00  30     dep_hold  None      
        5      georgerojas  02:45:00  30     dep_fail  None      
        
        Command Error/Debug:
        
    """

    args      = ''
    exp_rs    = 0

    results = testutils.run_cmd('qstat.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qrls_qrls_2():
    """
    qrls test run: qrls_2

        Command Output:
           Removed dependencies from jobs: 
              4
              5
        
        Command Error/Debug:
        qrls.py -d --dep 4 5
        
        component: "queue-manager.get_jobs", defer: False
          get_jobs(
             [{'user_hold': '*', 'tag': 'job', 'user': 'georgerojas', 'jobid': 4}, {'user_hold': '*', 'tag': 'job', 'user': 'georgerojas', 'jobid': 5}],
             )
        
        
        component: "queue-manager.set_jobs", defer: False
          set_jobs(
             [{'user_hold': '*', 'tag': 'job', 'is_active': '*', 'user': 'georgerojas', 'jobid': 4}, {'user_hold': '*', 'tag': 'job', 'is_active': '*', 'user': 'georgerojas', 'jobid': 5}],
             {'all_dependencies': []},
             georgerojas,
             )
        
        
        
        
    """

    args      = """-d --dep 4 5"""
    exp_rs    = 0

    results = testutils.run_cmd('qrls.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qstat_qstat_8():
    """
    qstat test run: qstat_8

        Command Output:
        JobID  User         WallTime  Nodes  State   Location  
        =======================================================
        1      georgerojas  01:05:00  30     queued  None      
        2      georgerojas  01:55:00  30     queued  None      
        3      georgerojas  02:45:00  30     queued  None      
        4      georgerojas  02:45:00  30     queued  None      
        5      georgerojas  02:45:00  30     queued  None      
        
        Command Error/Debug:
        
    """

    args      = ''
    exp_rs    = 0

    results = testutils.run_cmd('qstat.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qsub_qsub_6():
    """
    qsub test run: qsub_6

        Command Output:
        6
        
        Command Error/Debug:
        qsub.py --debug -t 150 -n 30 /bin/ls
        
        component: "system.validate_job", defer: False
          validate_job(
             {'kernel': 'default', 'verbose': False, 'held': False, 'notify': False, 'project': False, 'preemptable': False, 'outputprefix': False, 'umask': False, 'version': False, 'env': False, 'cwd': '/Users/georgerojas/p/Cobalt/cobalt/testsuite/TestCobaltClients', 'run_project': False, 'forcenoval': False, 'kerneloptions': False, 'time': '150', 'debug': True, 'dependencies': False, 'debuglog': False, 'proccount': False, 'disable_preboot': False, 'geometry': False, 'queue': 'default', 'mode': False, 'error': False, 'nodecount': '30', 'output': False, 'attrs': {}, 'user_list': False, 'inputfile': False},
             )
        
        
        component: "queue-manager.add_jobs", defer: False
          add_jobs(
             [{'cwd': '/Users/georgerojas/p/Cobalt/cobalt/testsuite/TestCobaltClients', 'args': [], 'kernel': 'default', 'user_list': ['georgerojas'], 'umask': 18, 'jobid': '*', 'queue': 'default', 'script_preboot': True, 'tag': 'job', 'command': '/bin/ls', 'mode': 'smp', 'path': '/Users/georgerojas/p/Cobalt/cobalt/src/clients:/Users/georgerojas/p/Cobalt/cobalt/src/clients/POSIX:/opt/local/bin:/opt/local/sbin:/Library/Frameworks/Python.framework/Versions/2.6/bin:/Users/georgerojas/p/Cobalt/cobalt/src/clients:/Users/georgerojas/p/Cobalt/cobalt/src/clients/POSIX:/opt/local/bin:/opt/local/sbin:/Library/Frameworks/Python.framework/Versions/2.6/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/X11/bin:/usr/local/git/bin:~/bin:~/bin', 'nodes': 30, 'walltime': '150', 'procs': 30, 'outputdir': '/Users/georgerojas/p/Cobalt/cobalt/testsuite/TestCobaltClients', 'run_project': False, 'user': 'georgerojas'}],
             )
        
        
        
        
    """

    args      = """--debug -t 150 -n 30 /bin/ls"""
    exp_rs    = 0

    results = testutils.run_cmd('qsub.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qsub_qsub_7():
    """
    qsub test run: qsub_7

        Command Output:
        7
        
        Command Error/Debug:
        qsub.py --debug -t 150 -n 30 /bin/ls
        
        component: "system.validate_job", defer: False
          validate_job(
             {'kernel': 'default', 'verbose': False, 'held': False, 'notify': False, 'project': False, 'preemptable': False, 'outputprefix': False, 'umask': False, 'version': False, 'env': False, 'cwd': '/Users/georgerojas/p/Cobalt/cobalt/testsuite/TestCobaltClients', 'run_project': False, 'forcenoval': False, 'kerneloptions': False, 'time': '150', 'debug': True, 'dependencies': False, 'debuglog': False, 'proccount': False, 'disable_preboot': False, 'geometry': False, 'queue': 'default', 'mode': False, 'error': False, 'nodecount': '30', 'output': False, 'attrs': {}, 'user_list': False, 'inputfile': False},
             )
        
        
        component: "queue-manager.add_jobs", defer: False
          add_jobs(
             [{'cwd': '/Users/georgerojas/p/Cobalt/cobalt/testsuite/TestCobaltClients', 'args': [], 'kernel': 'default', 'user_list': ['georgerojas'], 'umask': 18, 'jobid': '*', 'queue': 'default', 'script_preboot': True, 'tag': 'job', 'command': '/bin/ls', 'mode': 'smp', 'path': '/Users/georgerojas/p/Cobalt/cobalt/src/clients:/Users/georgerojas/p/Cobalt/cobalt/src/clients/POSIX:/opt/local/bin:/opt/local/sbin:/Library/Frameworks/Python.framework/Versions/2.6/bin:/Users/georgerojas/p/Cobalt/cobalt/src/clients:/Users/georgerojas/p/Cobalt/cobalt/src/clients/POSIX:/opt/local/bin:/opt/local/sbin:/Library/Frameworks/Python.framework/Versions/2.6/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/X11/bin:/usr/local/git/bin:~/bin:~/bin', 'nodes': 30, 'walltime': '150', 'procs': 30, 'outputdir': '/Users/georgerojas/p/Cobalt/cobalt/testsuite/TestCobaltClients', 'run_project': False, 'user': 'georgerojas'}],
             )
        
        
        
        
    """

    args      = """--debug -t 150 -n 30 /bin/ls"""
    exp_rs    = 0

    results = testutils.run_cmd('qsub.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qstat_qstat_9():
    """
    qstat test run: qstat_9

        Command Output:
        JobID  User         WallTime  Nodes  State   Location  
        =======================================================
        1      georgerojas  01:05:00  30     queued  None      
        2      georgerojas  01:55:00  30     queued  None      
        3      georgerojas  02:45:00  30     queued  None      
        4      georgerojas  02:45:00  30     queued  None      
        5      georgerojas  02:45:00  30     queued  None      
        6      georgerojas  02:30:00  30     queued  None      
        7      georgerojas  02:30:00  30     queued  None      
        
        Command Error/Debug:
        
    """

    args      = ''
    exp_rs    = 0

    results = testutils.run_cmd('qstat.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qalter_qalter_4():
    """
    qalter test run: qalter_4

        Command Output:
        updating scores for jobs: 6, 7
        
        Command Error/Debug:
        qalter.py --debug --defer 6 7
        
        component: "queue-manager.get_jobs", defer: False
          get_jobs(
             [{'is_active': '*', 'tag': 'job', 'notify': '*', 'procs': '*', 'walltime': '*', 'queue': '*', 'jobid': 6, 'project': '*', 'mode': '*', 'nodes': '*', 'user': 'georgerojas'}, {'is_active': '*', 'tag': 'job', 'notify': '*', 'procs': '*', 'walltime': '*', 'queue': '*', 'jobid': 7, 'project': '*', 'mode': '*', 'nodes': '*', 'user': 'georgerojas'}],
             )
        
        
        component: "queue-manager.adjust_job_scores", defer: True
          adjust_job_scores(
             [{'jobid': 6}, {'jobid': 7}],
             0,
             georgerojas,
             )
        
        
        
        
    """

    args      = """--debug  --defer 6 7"""
    exp_rs    = 0

    results = testutils.run_cmd('qalter.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_qstat_qstat_10():
    """
    qstat test run: qstat_10

        Command Output:
        JobID  User         WallTime  Nodes  State   Location  
        =======================================================
        1      georgerojas  01:05:00  30     queued  None      
        2      georgerojas  01:55:00  30     queued  None      
        3      georgerojas  02:45:00  30     queued  None      
        4      georgerojas  02:45:00  30     queued  None      
        5      georgerojas  02:45:00  30     queued  None      
        6      georgerojas  02:30:00  30     queued  None      
        7      georgerojas  02:30:00  30     queued  None      
        
        Command Error/Debug:
        
    """

    args      = ''
    exp_rs    = 0

    results = testutils.run_cmd('qstat.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]
    cmd_err = results[3]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Command Error:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), str(cmd_err), args)

    assert result, errmsg