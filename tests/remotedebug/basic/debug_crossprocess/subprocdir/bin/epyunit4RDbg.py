#!/usr/bin/env python
"""
A selftest dummy for the verification and test of remote debugging by PyDev/Eclipse.
Calls a subprocess by starting a bash script 'myscript.sh'.
Uses:

* epyunit.SystemCalls()

* epyunit.callit()

"""
from __future__ import absolute_import
#from __future__ import print_function

import getopt, sys

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.0'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"


_kargs={}
_intst = False

class MySubProcessLevel01(object):

    def __init__(self,appname):
        pass
    
    def execute(self,appname):
        global _kargs
        global _intst
        
        #
        #--- fetch options
        #
        try:
            from epyunit.SystemCalls import SystemCalls
        except Exception as e:
            print "\n#\n#*** Set 'PYTHONPATH' ("+str(e)+")\n#\n"
            sys.exit(1)
        
        try:
            _longopts = [
                "ignore-pydevd-loaded","ignore-pydevd-syspath","ignore-pydevd-callparam",
                "pderd_inTestMode_suppress_init",
            ]
            _opts, _args = getopt.getopt(sys.argv[1:], "lsc", _longopts)
        except getopt.GetoptError, err:
            print str(err)
            sys.exit(2)
    
    
        _ipdl = False
        _ipds = False
        _ipdc = False

        for _o,_a in _opts:
            
            if _o in ("--ignore-pydevd-loaded", '-l'):
                _ipdl = True
            elif _o in ("--ignore-pydevd-syspath", '-s'):
                _ipds = True
            elif _o in ("--ignore-pydevd-callparam", '-c'):
                _ipdc = True
            elif _o in ("--pderd_inTestMode_suppress_init", '-s'):
                _intst = True
            else:
                assert False, "unhandled option"
        
        if _ipdl or _ipds or _ipdc:
            _tf = ''
            if _ipdl:
                _tf += 'ignorePydevd,'
            if _ipds:
                _tf += 'ignorePydevdSysPath,'
            if _ipdc:
                _tf += 'ignorePydevdCallParam,'
            _kargs['testflags'] = _tf

        sx = SystemCalls(**_kargs)
        call = ' '.join(_args)
        ret = sx.callit(call)
        
        #
        # ** adapt required forwarded output for test dummy ***
        #
        if ret[0] == 126: 
            print >>sys.stderr ,"ERROR:check exec permissions of 'myscript.sh'"
        elif ret[0] == 0:
            print "STDOUT:OK"
            print >>sys.stderr , "STDERR:OK"
        else:
            print ret[1]
            print >>sys.stderr , ret[2]
        sys.exit(ret[0])

if __name__ == '__main__': 
    # name of application, used for several filenames as default
    _APPNAME = "epyunit4RDbg"
    
    # for debug of loader
    if _intst:
        sys.argv.append('--pderd_inTestMode_suppress_init')
    import epyunit.debug.pydevrdc
    if _intst:
        sys.argv.pop()
        epyunit.debug.pydevrdc.PYDEVD = epyunit.debug.pydevrdc.PyDevRDC(**_kargs)

    epyunit.debug.pydevrdc.PYDEVD.startDebug()

    myproc = MySubProcessLevel01(_APPNAME)
    myproc.execute(_APPNAME)
