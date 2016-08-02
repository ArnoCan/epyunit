# -*- coding: utf-8 -*-
"""Selftest for the package 'epyunit'.

"""
from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"


import sys,os

from epyunit.SubprocUnit import SubprocessUnit,SProcUnitRules

def selftest(**kargs):
    """Calls some interfaces for basic operational checks.  
    """
    _appname = "selftest"
    
    _out = kargs.get('out',None)
    _verbose = kargs.get('verbose',0)
    _debug = kargs.get('debug',0)
    
    if _verbose>0:
        kargs['verbose'] = _verbose 
    if kargs.get('debug') > 0:
        kargs['debug'] = _debug 

    # create a complete subprocess unit test controller with configuration data
    sx = SubprocessUnit()
    import epyunit #for path to mymodule.sh
    cx = epyunit.__path__[0]+os.sep+"myscript.sh"
    
    
    # add rules to be applied ont the subprocesses
    _myRules = SProcUnitRules()


    #
    # perform the tests for defined filter
    #
    
    #
    #*******
    #
    _myParams = {'exitval':123,'stdoutok':["arbitrary output"],'stderrok':[],}
    _myRules.setrules(_myRules.rules_reset)
    _myrx = { 'exit_chk': True, 'exit_val': 123, 'exit_type':'VAL',}
    _myRules.setrules(_myrx)
    
    _myRules.setkargs(**_myParams)
    if _verbose >1:
        print _myRules 
    sx.setkargs(**{'rules':_myRules,})
    ret = sx.callit(cx)
    if ret[0] == 126:
        print >>sys.stderr ,"check exec permissions of 'myscript.sh'"
    if _out:
        if _verbose:
            print "\n#*** epyunit/myscript.sh DEFAULT ***" 
        if _verbose>1:
            sx.displayit(ret)                   
    assert ret == [123,["arbitrary output"],[]]
    assert sx.apply(ret)


    #
    #*******
    #
    _myParams = {'exitval':0,'stdoutok':["fromA", "arbitrary output","arbitrary signalling OK string","arbitrary output"],'stderrok':[],}
    _myRules.setrules(_myRules.rules_reset)
    _myrx = { 'exit_chk': True, 'exit_type':'OK','stdoutok_val':["arbitrary output","arbitrary signalling OK string","arbitrary output"]}
    _myRules.setrules(_myrx)

    _myRules.setkargs(**_myParams)
    if _verbose>1:
        print _myRules 
    sx.setkargs(**{'rules':_myRules,})
    ret = sx.callit(cx+' OK')
    if _out:
        if _verbose:
            print "\n#*** epyunit/myscript.sh OK ***" 
        if _verbose>1:
            sx.displayit(ret)                   
    assert ret == [0,["fromA", "arbitrary output","arbitrary signalling OK string","arbitrary output"],[]]
    assert sx.apply(ret)



    #
    #*******
    #
    _myParams = {'exitval':0,'stdoutok':["fromC", "arbitrary output","arbitrary signalling OK string","arbitrary output"],'stderrok':[],}
    _myRules.setrules(_myRules.rules_reset)
    _myrx = { 'exit_chk': True, 'exit_type':'OK','stdoutok_val':["arbitrary output","arbitrary signalling OK string","arbitrary output"]}
    _myRules.setrules(_myrx)

    _myRules.setkargs(**_myParams)
    if _verbose>1:
        print _myRules 
    sx.setkargs(**{'rules':_myRules,})
    ret = sx.callit(cx+' PRIO')
    if _out:
        if _verbose:
            print "\n#*** epyunit/myscript.sh PRIO ***" 
        if _verbose>1:
            sx.displayit(ret)                   
    assert ret == [0,["fromC", "arbitrary output","arbitrary signalling OK string","arbitrary output"],["arbitrary signalling ERROR string"]]
    assert sx.apply(ret)



    #
    #*******
    #
    _myParams = {'exitval':0,'stdoutok':["fromD", "arbitrary output","arbitrary signalling OK string","arbitrary output"],'stderrok':[],}
    _myRules.setrules(_myRules.rules_reset)
    _myrx = { 'exit_chk': True, 'exit_type':'OK','stdoutok_val':["arbitrary output","arbitrary signalling OK string","arbitrary output"]}
    _myRules.setrules(_myrx)

    _myRules.setkargs(**_myParams)
    if _verbose>1:
        print _myRules 
    sx.setkargs(**{'rules':_myRules,})
    ret = sx.callit(cx+' EXITOK')
    if _out:
        if _verbose:
            print "\n#*** epyunit/myscript.sh EXITOK ***" 
        if _verbose>1:
            sx.displayit(ret)                   
    assert ret == [0,["fromD", "arbitrary output","arbitrary signalling OK string","arbitrary output"],[]]
    assert sx.apply(ret)



    #
    #*******
    #
    _myParams = {'exitval':1,'stdoutok':["fromD", "arbitrary output","arbitrary signalling OK string","arbitrary output"],'stderrok':[],}
    _myRules.setrules(_myRules.rules_reset)
    _myrx = { 'exit_chk': True, 'exit_type':'NOK','stdoutok_val':["arbitrary output","arbitrary signalling OK string","arbitrary output"]}
    _myRules.setrules(_myrx)

    _myRules.setkargs(**_myParams)
    if _verbose>1:
        print _myRules 
    sx.setkargs(**{'rules':_myRules,})
    ret = sx.callit(cx+' EXITNOK')
    if _out:
        if _verbose:
            print "\n#*** epyunit/myscript.sh EXITNOK ***" 
        if _verbose>1:
            sx.displayit(ret)                   
    assert ret == [1,["fromE", "arbitrary output","arbitrary signalling OK string","arbitrary output"],[]]
    assert sx.apply(ret)



    #
    #*******
    #
    _myParams = {'exitval':7,'stdoutok':["fromF", "arbitrary output","arbitrary signalling NOK string","arbitrary output"],'stderrok':[],}
    _myRules.setrules(_myRules.rules_reset)
    _myrx = { 'exit_chk': True, 'exit_type':'VAL','exit_val':7,'stdoutok_val':["arbitrary output","arbitrary signalling OK string","arbitrary output"]}
    _myRules.setrules(_myrx)

    _myRules.setkargs(**_myParams)
    if _verbose>1:
        print _myRules 
    sx.setkargs(**{'rules':_myRules,})
    ret = sx.callit(cx+' EXIT7')
    if _out:
        if _verbose:
            print "\n#*** epyunit/myscript.sh EXIT7 ***" 
        if _verbose>1:
            sx.displayit(ret)                   
    assert ret == [7,["fromF", "arbitrary output","arbitrary signalling NOK string","arbitrary output"],[]]
    assert sx.apply(ret)



    #
    #*******
    #
    _myParams = {'exitval':8,'stdoutok':["fromG", 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'],'stderrok': ['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output'],}
    _myRules.setrules(_myRules.rules_reset)
    _myrx = { 'exit_chk': True, 'exit_type':'VAL','exit_val':8,'stdoutok_val':["arbitrary output","arbitrary signalling OK string","arbitrary output"]}
    _myRules.setrules(_myrx)

    _myRules.setkargs(**_myParams)
    if _verbose>1:
        print _myRules 
    ret = sx.callit(cx+' EXIT8')
    if _out:
        if _verbose:
            print "\n#*** epyunit/myscript.sh EXIT8 ***" 
        if _verbose>1:
            sx.displayit(ret)                   
    assert ret == [8,["fromG", 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], ['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']]
    assert sx.apply(ret)


    #
    #*******
    #
    _myParams = {'exitval':123,'stdoutok':["arbitrary output"],'stderrok': [],}
    _myRules.setrules(_myRules.rules_reset)
    _myrx = { 'exit_chk': True, 'exit_type':'NOK','stdoutok_val':["arbitrary output","arbitrary signalling OK string","arbitrary output"]}
    _myRules.setrules(_myrx)

    _myRules.setkargs(**_myParams)
    if _verbose>1:
        print _myRules 
    ret = sx.callit(cx)
    if _out:
        if _verbose:
            print "\n#*** epyunit/myscript.sh DEFAULT ***" 
        if _verbose>1:
            sx.displayit(ret)                   
    assert ret == [123,["arbitrary output"],[]]
    assert sx.apply(ret)

    pass
