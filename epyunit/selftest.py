# -*- coding: utf-8 -*-
"""Selftest for the package 'epyunit'.

"""
from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.2.0'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"


import sys,os

from epyunit.SubprocUnit import SubprocessUnit,SProcUnitRules
from filesysobjects.FileSysObjects import findRelPathInSearchPath

_appname = "selftest" #: application name

def _subcall_myscript(slang,**kargs):
    """Calls the operational checks provided by 'myscript' for language variant.

    Args:
        slang: Programming language of called script, current supported are:

            bash

            python


        **kargs:

            out:

            verbose:

            debug:

    Returns:
        None.

    Raises:
        In case of assertion errors.

    """
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

    if slang.lower() in ('bash', 'sh', 'shell',):
        _sx = "myscript.sh"
        cx = epyunit.__path__[0]+os.sep+_sx
        if "win32" in sys.platform:
            p = os.environ.get('PATH')
            fp = findRelPathInSearchPath('bash.exe',p,subsplit=True)
            if not fp:
                fp = findRelPathInSearchPath('bash.exe',p,subsplit=True)
            if not fp:
                fp = findRelPathInSearchPath('bin/bash.exe',p,subsplit=True)
            if not fp:
                fp = findRelPathInSearchPath('bin\\bash.exe',p,subsplit=True)
            if not fp:
                fp = findRelPathInSearchPath('bash',p,subsplit=True)
            if not fp:
                raise Exception("Missing:bash")
            cx = fp + ' ' + cx
        else:
            if not findRelPathInSearchPath('bash',os.environ.get('PATH'),subsplit=True):
                raise Exception("Missing:bash")
            cx = ' bash ' + cx

    elif slang.lower() == 'python':
        _sx = "myscript.py"
        cx = epyunit.__path__[0]+os.sep+_sx
        if "win32" in sys.platform:
            p = os.environ.get('PATH')
            fp = findRelPathInSearchPath('python.exe',p,subsplit=True)
            if not fp:
                fp = findRelPathInSearchPath('python.exe',p,subsplit=True)
            if not fp:
                fp = findRelPathInSearchPath('bin/python.exe',p,subsplit=True)
            if not fp:
                fp = findRelPathInSearchPath('bin\\python.exe',p,subsplit=True)
            if not fp:
                fp = findRelPathInSearchPath('python',p,subsplit=True)
            if not fp:
                raise Exception("Missing:python")
            cx = fp + ' ' + cx
        else:
            if not findRelPathInSearchPath('python',os.environ['PATH'],subsplit=True):
                raise Exception("\nPATH="+str(os.environ['PATH'])+"\nMissing:python")
            cx = ' python ' + cx # + " --rdbg "

    elif slang.lower() == 'perl':
        _sx = "myscript.pl"
        cx = epyunit.__path__[0]+os.sep+_sx
        if "win32" in sys.platform:
            p = os.environ.get('PATH')
            fp = findRelPathInSearchPath('perl.exe',p,subsplit=True)
            if not fp:
                fp = findRelPathInSearchPath('perl.exe',p,subsplit=True)
            if not fp:
                fp = findRelPathInSearchPath('bin/perl.exe',p,subsplit=True)
            if not fp:
                fp = findRelPathInSearchPath('bin\\perl.exe',p,subsplit=True)
            if not fp:
                fp = findRelPathInSearchPath('perl',p,subsplit=True)
            if not fp:
                raise Exception("Missing:perl")
            cx = fp + ' ' + cx
        else:
            if not findRelPathInSearchPath('perl',os.environ['PATH'],subsplit=True):
                raise Exception("Missing:perl")
            cx = ' perl ' + cx

    else:
        raise Exception("Unknown language type:"+str(slang))

    # add rules to be applied ont the subprocesses
    _myRules = SProcUnitRules()


    #
    # perform the tests for defined filter
    #

    #
    #*** DEFAULT ***
    #
    _myParams = {'exitval':123,'stdoutok':["arbitrary output"],'stderrok':[],}
    _myrx = {'reset':True, 'exitign': False, 'exitval': 123, 'exittype':'VAL',}
    _myRules.setrules(**_myrx)
    _myRules.setkargs(**_myParams)
    if _verbose >1:
        print _myRules
    sx.setkargs(**{'rules':_myRules, 'env': os.environ})
    ret = sx.callit(cx)
    if ret[0] == 126:
        print >>sys.stderr ,"check exec permissions of 'myscript.*'"
    if _out:
        if _verbose:
            print "\n#*** epyunit/"+str(_sx)+" DEFAULT ***"
        if _verbose>1:
            sx.displayit(ret)

    retX = [123,["arbitrary output"],[]]
    try:
        if ret[1]: ret[1] = map(lambda x: x.replace('\r',''),ret[1])
        if ret[2]: ret[2] = map(lambda x: x.replace('\r',''),ret[2])
        assert ret ==retX
    except:
        print >>sys.stderr, ""
        print >>sys.stderr, "retX="+str(retX)
        print >>sys.stderr, "ret= "+str(ret)
    assert sx.apply(ret)


    #
    #*** A-OK ***
    #
    _myParams = {'exitval':0,'stdoutok':["fromA", "arbitrary output","arbitrary signalling OK string","arbitrary output"],'stderrok':[],}
    _myrx = {'reset':True, 'exitign': False, 'exitval': 0, 'exittype':'OK', 'stdoutok_val':["arbitrary output","arbitrary signalling OK string","arbitrary output"]}
    _myRules.setrules(**_myrx)
    _myRules.setkargs(**_myParams)
    if _verbose>1:
        print _myRules
    sx.setkargs(**{'rules':_myRules,})
    ret = sx.callit(cx+' -- OK')
    if _out:
        if _verbose:
            print "\n#*** epyunit/"+str(_sx)+" OK ***"
        if _verbose>1:
            sx.displayit(ret)
    retX = [0,["fromA", "arbitrary output","arbitrary signalling OK string","arbitrary output"],[]]
    try:
        if ret[1]: ret[1] = map(lambda x: x.replace('\r',''),ret[1])
        if ret[2]: ret[2] = map(lambda x: x.replace('\r',''),ret[2])
        assert ret ==retX
    except:
        print >>sys.stderr, ""
        print >>sys.stderr, "retX="+str(retX)
        print >>sys.stderr, "ret= "+str(ret)
    assert sx.apply(ret)



    #
    #*** C-OK ***
    #
    _myParams = {'exitval':0,'stdoutok':["fromC", "arbitrary output","arbitrary signalling OK string","arbitrary output"],'stderrok':[],}
    _myrx = {'reset':True, 'exitign': False, 'exittype':'OK','stdoutok':["arbitrary output","arbitrary signalling OK string","arbitrary output"]}
    _myRules.setrules(**_myrx)
    _myRules.setkargs(**_myParams)
    if _verbose>1:
        print _myRules
    sx.setkargs(**{'rules':_myRules,})
    ret = sx.callit(cx+' -- PRIO')
    if _out:
        if _verbose:
            print "\n#*** epyunit/"+str(_sx)+" PRIO ***"
        if _verbose>1:
            sx.displayit(ret)
    retX = [0,["fromC", "arbitrary output","arbitrary signalling OK string","arbitrary output"],["arbitrary signalling ERROR string"]]
    try:
        if ret[1]: ret[1] = map(lambda x: x.replace('\r',''),ret[1])
        if ret[2]: ret[2] = map(lambda x: x.replace('\r',''),ret[2])
        assert ret ==retX
    except:
        print >>sys.stderr, ""
        print >>sys.stderr, "retX="+str(retX)
        print >>sys.stderr, "ret= "+str(ret)
    assert sx.apply(ret)



    #
    #*** D-OK ***
    #
    _myParams = {'exitval':0,'stdoutok':["fromD", "arbitrary output","arbitrary signalling OK string","arbitrary output"],'stderrok':[],}
    _myrx = {'reset':True, 'exitign': False, 'exittype':'OK','stdoutok':["arbitrary output","arbitrary signalling OK string","arbitrary output"]}
    _myRules.setrules(**_myrx)
    _myRules.setkargs(**_myParams)
    if _verbose>1:
        print _myRules
    sx.setkargs(**{'rules':_myRules,})
    ret = sx.callit(cx+' -- EXITOK')
    if _out:
        if _verbose:
            print "\n#*** epyunit/"+str(_sx)+" EXITOK ***"
        if _verbose>1:
            sx.displayit(ret)
    retX = [0,["fromD", "arbitrary output","arbitrary signalling OK string","arbitrary output"],[]]
    try:
        if ret[1]: ret[1] = map(lambda x: x.replace('\r',''),ret[1])
        if ret[2]: ret[2] = map(lambda x: x.replace('\r',''),ret[2])
        assert ret ==retX
    except:
        print >>sys.stderr, ""
        print >>sys.stderr, "retX="+str(retX)
        print >>sys.stderr, "ret= "+str(ret)
    assert sx.apply(ret)



    #
    #*** E-NOK ***
    #
    _myParams = {'exitval':1,'stdoutok':["fromE", "arbitrary output","arbitrary signalling OK string","arbitrary output"],'stderrok':[],}
    _myrx = {'reset':True, 'multiline':True, 'exitign': False, 'exittype':'NOK','stdoutok':["arbitrary output","arbitrary signalling OK string","arbitrary output"]}
    _myRules.setrules(**_myrx)
    _myRules.setkargs(**_myParams)
    if _verbose>1:
        print _myRules
    sx.setkargs(**{'rules':_myRules,})
    ret = sx.callit(cx+' -- EXITNOK')
    if _out:
        if _verbose:
            print "\n#*** epyunit/"+str(_sx)+" EXITNOK ***"
        if _verbose>1:
            sx.displayit(ret)
    retX = [1,["fromE", "arbitrary output","arbitrary signalling OK string","arbitrary output"],[]]
    try:
        if ret[1]: ret[1] = map(lambda x: x.replace('\r',''),ret[1])
        if ret[2]: ret[2] = map(lambda x: x.replace('\r',''),ret[2])
        assert ret ==retX
    except:
        print >>sys.stderr, ""
        print >>sys.stderr, "retX="+str(retX)
        print >>sys.stderr, "ret= "+str(ret)
    assert sx.apply(ret)



    #
    #*** F-NOK7 ***
    #
    _myParams = {'exitval':7,'stdoutok':["fromF", "arbitrary output","arbitrary signalling NOK string","arbitrary output"],'stderrok':[],}
    _myrx = {'reset':True, 'exitign': False, 'exittype':'VAL','exitval':7,'stdoutok':["arbitrary output","arbitrary signalling OK string","arbitrary output"]}
    _myRules.setrules(**_myrx)
    _myRules.setkargs(**_myParams)
    if _verbose>1:
        print _myRules
    sx.setkargs(**{'rules':_myRules,})
    ret = sx.callit(cx+' -- EXIT7')
    if _out:
        if _verbose:
            print "\n#*** epyunit/"+str(_sx)+" EXIT7 ***"
        if _verbose>1:
            sx.displayit(ret)
    retX = [7,["fromF", "arbitrary output","arbitrary signalling NOK string","arbitrary output"],[]]
    try:
        if ret[1]: ret[1] = map(lambda x: x.replace('\r',''),ret[1])
        if ret[2]: ret[2] = map(lambda x: x.replace('\r',''),ret[2])
        assert ret ==retX
    except:
        print >>sys.stderr, ""
        print >>sys.stderr, "retX="+str(retX)
        print >>sys.stderr, "ret= "+str(ret)
    assert sx.apply(ret)



    #
    #*** G-NOK8 ***
    #
    _myParams = {'exitval':8,'stdoutok':["fromG", 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'],'stderrok': ['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output'],}
    _myrx = {'reset':True, 'exitign': False, 'exittype':'VAL','exitval':8,'stdoutok':["arbitrary output","arbitrary signalling OK string","arbitrary output"]}
    _myRules.setrules(**_myrx)
    _myRules.setkargs(**_myParams)
    if _verbose>1:
        print _myRules
    ret = sx.callit(cx+' -- EXIT8')
    if _out:
        if _verbose:
            print "\n#*** epyunit/"+str(_sx)+" EXIT8 ***"
        if _verbose>1:
            sx.displayit(ret)
    retX = [8,["fromG", 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], ['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']]
    try:
        if ret[1]: ret[1] = map(lambda x: x.replace('\r',''),ret[1])
        if ret[2]: ret[2] = map(lambda x: x.replace('\r',''),ret[2])
        assert ret ==retX
    except:
        print >>sys.stderr, ""
        print >>sys.stderr, "retX="+str(retX)
        print >>sys.stderr, "ret= "+str(ret)
    assert sx.apply(ret)


    #
    #***H-NOK9 ***
    #
    _myParams = {'exitval':9,'stdoutok':["fromH", 'OK', 'OK', 'OK'],'stderrok': ['NOK', 'NOK',],}
    _myrx = {'reset':True, 'exitign': False, 'exittype':'VAL','exitval':9,'stdoutok':["NOK","NOK","NOK"]}
    _myRules.setrules(**_myrx)
    _myRules.setkargs(**_myParams)
    if _verbose>1:
        print _myRules
    ret = sx.callit(cx+' -- EXIT9OK3NOK2')
    if _out:
        if _verbose:
            print "\n#*** epyunit/"+str(_sx)+" EXIT9OK3NOK2 ***"
        if _verbose>1:
            sx.displayit(ret)
    retX = [9,["fromH", 'OK', 'OK', 'OK'], ['NOK', 'NOK']]
    try:
        if ret[1]: ret[1] = map(lambda x: x.replace('\r',''),ret[1])
        if ret[2]: ret[2] = map(lambda x: x.replace('\r',''),ret[2])
        assert ret ==retX
    except:
        print >>sys.stderr, ""
        print >>sys.stderr, "retX="+str(retX)
        print >>sys.stderr, "ret= "+str(ret)
    assert sx.apply(ret)


    #
    #*** I-OK0 ***
    #
    _myParams = {'exitval':0,'stdoutok':[],'stderrok': ['fromI', 'NOK', 'NOK'],}
    _myrx = {'reset':True, 'exitign': False, 'exittype':'VAL','exitval':0,'stdoutok':[]}
    _myRules.setrules(**_myrx)
    _myRules.setkargs(**_myParams)
    if _verbose>1:
        print _myRules
    ret = sx.callit(cx+' -- STDERRONLY')
    if _out:
        if _verbose:
            print "\n#*** epyunit/"+str(_sx)+" STDERRONLY ***"
        if _verbose>1:
            sx.displayit(ret)
    retX = [0,[], ['fromI', 'NOK', 'NOK']]
    try:
        if ret[1]: ret[1] = map(lambda x: x.replace('\r',''),ret[1])
        if ret[2]: ret[2] = map(lambda x: x.replace('\r',''),ret[2])
        assert ret ==retX
    except:
        print >>sys.stderr, ""
        print >>sys.stderr, "retX="+str(retX)
        print >>sys.stderr, "ret= "+str(ret)
    assert sx.apply(ret)


    #
    #*** DEFAULT-123 ***
    #
    _myParams = {'exitval':123,'stdoutok':["arbitrary output"],'stderrok': [],}
    _myrx = {'reset':True, 'exitign': False, 'exittype':'NOK','stdoutok':["arbitrary output","arbitrary signalling OK string","arbitrary output"]}
    _myRules.setrules(**_myrx)
    _myRules.setkargs(**_myParams)
    if _verbose>1:
        print _myRules
    ret = sx.callit(cx)
    if _out:
        if _verbose:
            print "\n#*** epyunit/"+str(_sx)+" DEFAULT ***"
        if _verbose>1:
            sx.displayit(ret)
    retX = [123,["arbitrary output"],[]]
    try:
        if ret[1]: ret[1] = map(lambda x: x.replace('\r',''),ret[1])
        if ret[2]: ret[2] = map(lambda x: x.replace('\r',''),ret[2])
        assert ret ==retX
    except:
        print >>sys.stderr, ""
        print >>sys.stderr, "retX="+str(retX)
        print >>sys.stderr, "ret= "+str(ret)
    assert sx.apply(ret)

    pass

def selftest(slang=None,**kargs):
    """Calls some interfaces for basic operational checks.

    Args:
        slang: The language type of the testscript,
        current availble:

            perl

            python

            bash

        **kargs:

            out:

            verbose:

            debug:

    Returns:
        None.

    Raises:
        In case of assertion errors.

    """
#     for k,v in kargs.items():
#         if k == 'bash':
#             _subcall_myscript('bash',**kargs)
#             return
#         elif k == 'python':
#             _subcall_myscript('python',**kargs)
#             return

    if not slang:
        if sys.platform == 'Windows':
            _subcall_myscript('python',**kargs)
        else:
            _subcall_myscript('python',**kargs)
#             _subcall_myscript('bash',**kargs)
#             _subcall_myscript('perl',**kargs)
    else:

        _subcall_myscript(slang,**kargs)
    pass
