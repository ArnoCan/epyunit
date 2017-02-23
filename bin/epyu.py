#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""'epyunit' - Command line interface

The epyunit commandline interface provides a call wrapper
for unit and regression tests of arbitrary executables.
This also includes the management of seammless cross-process
debugging based on PyDev/Eclipse.

The wrapper internally relies on the standard packages 'PyUnit'
and integrates into Eclipse by 'PyDev'. Thus unit tests could
be applied in particular for shell scripts and intermixed
application processes implemented in multiple programming
languages. Automation of remote debugging by PyDev is
supported.

The call is simply a prefix to the actual testee including
it's options. The wrapper itself provides various criteria
for the indication of the success and/or failure of the test
case. Therefore correlation of stdout, stderr, and exit
values is provided.


**SYNOPSIS**:

  epyunit [OPTIONS] [--] <testee> [<testee-options>]

The following categories of options are provided:

  rulesets:

    --exitign,  --exittype,  --exitval, --priotype
    --redebug, --redotall, --reignorecase, --remultiline,
    --result, --resultnok, --resultok, --reunicode,
    --stderrnok, --stderrok, --stdoutnok, --stdoutok,


  output and format:

    --csv, --pass, --passall, --raw, --repr, --str, --xml

    --appname, --test-id, --timestamp

  process wrapper:

    --cp, --cp-prepend, --cp-append

    --debug, --environment, --help, -Version, --Version,
    --verbose, -version, --version

    --selftest, --slang, --subproc, --subunit,

    --exit-unit-ok, --exit-unit-failed

  subprocess debugging:

    --pydev-remote-debug, --rdbg, --rdbg-forward
    --rdbg-env

**OPTIONS**:
.

  --appname=<arbitrary-name-of-app>

    An arbitrary application name to be inserted into record
    headers.

  --cp=<path-list>

    Classpath for module search, replaces sys.path.

  --cp-prepend=<path-list>

    Classpath for module search, inserted at the beginning of
    sys.path.

  --cp-append=<path-list>

    Classpath for module search, appended at the end of
    sys.path.

  --csv

    Prints complete test result CSV format including header.

  -d --debug

     Debug entries, does NOT work with 'python -O ...'.
     Developer output, aimed for filtering.

  --environment

    Include platform info into header.

  --exitign=(True|False)

    Ignore exit value.

  --exittype=(True|False)

    Exit value 'True' indicates success for '0',
    'False' indicates success for '!=0'.

  --exit-unit-failed=<exit-value>

    Exit value to be emitted in case of failure of unittest.

    default := 1

  --exit-unit-ok=<exit-value>

    Exit value to be emitted in case of success of unittest.

    default := 0

  --exitval=<exit-value>

    Indicates success when exit value is equal to the provided
    value.

  -h --help

     This help.

  --pass

    Pass through the testee results on STDOUT and STDERR.
    The exit value is interpreted by rules, else the
    execution state of the framework defines the exit
    value.

  --passall

    Pass through the testee result on STDOUT and STDERR
    including transparently the received exit value.

  --priotype

    In case of present failure and success conditions,

      TRUE:  the success condition dominates.

      FALSE: the failure condition dominates.

  --pydev-remote-debug[=host[:port]]

    Activates remote debugging with PyDev plugin of Eclipse.

  --raw

    Same as '--passall'

  --rdbg[=host[:port]]

    Activate remode debug, optionally the host and port number
    of the server process could be changed.

    default:=localhost:5678

  --rdbg-env

    Enables the readout of RDBG environment variables:
      ::

        RDBGROOT, RDBGSUB

  --rdbg-forward=(<forwarding-levels>|all|label)

    Forward the '--rdbg' option to subprocesses for nested debugging
    of process chains.

        <forwarding-levels>: Number of levels to be forwarded, 0==None.

        all: all nested subprocesses

        label: An arbitrary label defined at initialization of the
        debug instance. Debugging is enabled when these match.

    default:=0: No forwarding.

  --redebug

    Enables 're.DEBUG'

  --redotall:

    Enables 're.DOTALL'

  --reignorecase:

    Enables 're.IGNORECASE'.

  --remultiline:

    Enables 're.MULTILINE'.

  --repr

    Prints complete test result by Python call of 'repr()'.

  --result=#total-results

    The treshold of the total matched results for changing
    the overall state to success.

  --resultnok=#total-failure-results

    The treshold of the total matched failure results for
    changing the overall state to success.

  --resultok=#total-success-results

    The treshold of the total matched success results for
    changing the overall state to success.

  --reunicode:

    Enables 're.UNICODE'.

  --selftest

     Performs a basic functional selftest by executing the
     basic examples based on 'myscript.<postfix>', see '--slang'.

  --slang[=(bash|perl|python|<file-path-name>)

     Sets the subprocess script by it's programming language for
     the '--selftest' resource simulator. The following postfixes
     are currently available:

         slang=bash        -> postfix=sh

         slang=perl        -> postfix=pl

         slang=python      -> postfix=py

         <file-path-name>  -> "calls the provided executable"

     default:=python

  --stderrnok=<nok-string>

    Error string on stderr indicates success.

  --stderrok=<ok-string>

    OK string on stderr indicates success.

  --stdoutnok=<nok-string>

    Error string on stdout indicates success.

  --stdoutok=<ok-string>

    OK string on stdout indicates success.

  --str

    Prints complete test result by Python call of 'str()'.

  --subproc

    Starts the subprocess by: 'epyunit.SystemCalls'
    This mode also switches the output to '--passall' by
    default, when another output mode is required, set
    the required option after the '--subproc' option.

  --subunit

    Starts the subprocess by the default: 'epyunit.SubprocessUnit'

  --test-id=<arbitrary-identifier-for-record-header>

    Prints the test-id with the formats 'csv', and 'xml'.
    Too be applied in case of multiple test case calls.

  --timestamp

    Includes date and time into record header.

  -Version --Version

     Current version - detailed.

  -v --verbose

     Verbose, some relevant states for basic analysis.
     When '--selftest' is set, repetition raises the display
     level.

  -version --version

     Current version - terse.

  --xml

    Prints complete test result XML format.


**ARGUMENTS**:

  [--]

     The double hyphen terminates the options of the call,
     thus the remaining part of the call is treated as the
     subcall of the testee.

  <testee>

     The wrapped testee.

  [<testee-options>]

     Options of the testee.


**ENVIRONMENT**:

  * PYTHON OPTIONS:

    -O, -OO: Eliminates '__debug__' code.


**EXAMPLES**:

  Basic call examples are provided:

  * `CLI: command line interface <epyunit_example_cli.html>`_

  * `Eclipse: PyDev integration <epyunit_example_eclipse.html>`_

  For detailed examples refer to the subdirectories of the
  source package for:

  * Unit tests

  * UseCases

**SEE ALSO**:

  * https://pypi.python.org/pypi/epyunit/

  * https://pythonhosted.org/epyunit/

**COPYRIGHT**:
  Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez
  Copyright (C)2015-2016 Arno-Can Uestuensoez

"""
from __future__ import absolute_import
#from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.2.0'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'
__release__ = 'alpha2'
__docformat__ = "restructuredtext en"

import os, sys, platform, getopt

#
#--- early fetch of CLI options
#

# name of application, used for several filenames as default
if '--appname' in sys.argv:
    _ai = sys.argv.index('--appname')
    _APPNAME = sys.argv[_ai]
else:
    _APPNAME = "epyunit"

# runtime environment
_host = platform.node()
_user = "testuser"
_osu = platform.uname()
_os = _osu[0]
_osver = _osu[2]
_arch = _osu[-1]
_dist, _distver,_x = platform.dist()


# just to assure PYTHONPATH...
try:
    from epyunit.SystemCalls import SystemCalls
    from epyunit.SubprocUnit import SubprocessUnit
except Exception as e:
    print "\n#\n#*** Set 'PYTHONPATH' ("+str(e)+")\n#\n"
    sys.exit(1)

class  EPyUnitException(Exception):
    pass

def usage():
    if __name__ == '__main__':
        import pydoc
        #FIXME: literally displayed '__main__'
        print pydoc.help(__name__)
    else:
        help(str(os.path.basename(sys.argv[0]).split('.')[0]))

_longopts = [

    # result type and decision process
    "priotype=", "result=", "resultnok=", "resultok=",

    # exit values
    "exitval=","exitign=","exittype=",

    # output and error streams
    "stderrnok=","stdoutnok=","stderrok=","stdoutok=",
    "redebug","redotall","reignorecase","remultiline",
    "reunicode",


    # format
    "repr", "xml", "csv", "str", "pass", "passall", "raw",

    # runtime environent
    "appname=", "test-id=", "timestamp", "environment",
    "subproc", "subunit",

    "exit-unit-failed", "exit-unit-ok",

    # misc
    "help","debug","verbose","version","Version",
    "selftest", "slang=",
    #
    #-----
    #FIXME: 4DEL
    "default-nok", "default-ok",
]
_sopts = "a:hdv"

def usagemin():
    print "\nAvailable options:"
    slst = ""
    nl = 0
    print "\nshortopts:"
    for s in _sopts:
        if nl == 10:
            print "  "+slst
            nl = -1
            slst = ""
        if s == ':':
            continue
        slst += "-%s "%(s)
    if slst:
        print "  "+slst

    ilst = ""
    nl = 0
    print "\nlongopts:"
    for i in sorted(_longopts):
        if nl == 2  or nl>=len(_longopts):
            print "  "+ilst
            nl = -1
            ilst = ""
        ilst += "--%-20s "%(i)
        nl += 1
    if ilst:
        print "  "+ilst
    print """
Examples:

  epyu -v --selftest
  epyu -v -v --selftest
  epyu -v -v -v --selftest
  epyu -v --selftest --slang=bash     # use bash:   myscript.sh
  epyu -v --selftest --slang=python   # use perl:   myscript.pl
  epyu -v --selftest --slang=perl     # use python: myscript.py
  epyu -v myscript.py NOK
  epyu -v --exit=8 myscript.py EXIT8
  epyu -v --exit=8 myscript.pl EXIT8
  epyu -v --exit=8 myscript.py EXIT8


Reminder:

  * set PYTHONPATH
  * set PATH for 'epyu' to 'bin' directory
  * on Windows prefer to use 'epyu.py' with PATHEXT
  * set PATH for 'myscript.EXT'<EXT:=(sh|py|pl)> to 'epyunit' directory
  * use 'myscript.EXT -h'<EXT:=(sh|py|pl)> for all response pattern
  * use '--help' for complete help
  * start Eclipse and RemoteDebugServer of PyDev for cross-process debugging
  * consider using '--'(double-hyphen), which makes nested commands handy
    partially required mandatory

"""

#
# using for now getopt, thus help here as an extra handling...
#
if "--help" in sys.argv or "-help" in sys.argv:
    usage()
    sys.exit()

if "-h" in sys.argv:
    usagemin()
    sys.exit()


#
# Remote debugging
#
# but first eliminate callers default-dir because epyunit(bin) == epyunit(pkg)
#FIXME: print "4TEST:"+str(sys.path)
#FIXME: print "4TEST:"+str(sys.argv)
_tmp = sys.path.pop(0)
import epyunit.debug.checkRDbg
_rdbgthis,_rdbg,_rdbgfwd,_rdbgroot,_rdbgsub = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(**{'label':_APPNAME,})
"""
pydev remote debug options:
  _rdbgthis: requested debugging status for this process instance
  _rdbg: the remote debugging peer for this instance
  _rdbgfwd: requested state forwarding to nested subprocess levels
  _rdbgroot: rootdirectory of eclipse
  _rdbgsub: sub directory of PyDev for 'pydevd.py'
"""
# put it in-place again, who knows...
sys.path.insert(0,_tmp)
if _rdbgthis:
    # activate remote debug stub call
    import epyunit.debug.pydevrdc
    epyunit.debug.pydevrdc.PYDEVD.startDebug() # start debugging here...
    #
    # remote breakpoints could be set from here on...
    #
    pass

_kargs={}
try:
    _opts, _args = getopt.getopt(sys.argv[1:], _sopts, _longopts)
except getopt.GetoptError, err:
    print str(err)
    usagemin()
    sys.exit(2)


#
# defaults
#

# name of tested application
_appname = None

# test id, to be printed with result data records
_testid = 0

# perform hard-coded basic selftest
_selftest = False
_slang = 'python'

# verbose output
_verbose = 0

# debug output
_debug = 0

#
_default = 'OK'

# when OK and NOK conditions met the "NOK" defines the result
_prio = "NOK"

# exit value defined as success, or ignored: OK(0) | NOK(!=0) | IGNORE
_exit = "OK"
_exitokval = 0
_exitnok = "NOK"
_exitnokval = 1


# activate check of exit code: OK(0) else NOK(>0)
_chk_exit = True

# a strings to be checked in stderr stream
_chk_stderr = False
_CHK_STDERR_OK = [] # list of provided strings: OK condition
_CHK_STDERR_NOK = [] # list of provided strings: NOK condition

# a strings to be checked in stdout stream
_chk_stdout = False
_CHK_STDOUT_OK = [] # list of provided strings: OK condition
_CHK_STDOUT_NOK = [] # list of provided strings: NOK condition

# counter values for occured matches
_result = 0 # overall

# full result value display
_out = None
_timestamp = False
_environment = False

#
# for now one of each, last wins
_myRulesMap = {}

_O_REPR   = 0
_O_XML    = 1
_O_CSV    = 2
_O_PASS   = 3
_O_PASSA  = 4

#
# start wrapper for subprocess
_CALL_SUBPROC = SubprocessUnit

for _o,_a in _opts:

    #-------------------------------------------------------------
    #
    # *** rules - stored in _myRulesMap ***
    #

    #
    # *** result types ***
    #
    if _o in ("--priotype",):
        if _a.lower() in ('true','1','ok',):
            _myRulesMap['priotype'] = True
        else:
            _myRulesMap['priotype'] = False

    #
    # *** result thresholds ***
    #
    elif _o in ("--result",):
        if type(_a) is int:
            _myRulesMap['result'] = _a
        else:
            raise EPyUnitException("Integer required:"+str(_a))
        
    elif _o in ("--resultnok",):
        if type(_a) is int:
            _myRulesMap['resultnok'] = _a
        else:
            raise EPyUnitException("Integer required:"+str(_a))
    elif _o in ("--resultok",):
        if type(_a) is int:
            _myRulesMap['resultok'] = _a
        else:
            raise EPyUnitException("Integer required:"+str(_a))

    #
    # *** exit ***
    #
    elif _o in ("--exitval",):
        _myRulesMap['exitval'] = int(_a)
    elif _o in ("--exitign",):
        if _a.lower() in ('true','1','ok',):
            _myRulesMap['exitign'] = True
        else:
            _myRulesMap['exitign'] = False
    elif _o in ("--exittype",):
        if _a.lower() in ('true','1','ok',):
            _myRulesMap['exittype'] = True
        else:
            _myRulesMap['exittype'] = False


    #
    # *** stderr ***
    #
    elif _o in ("--stderrnok",):
        _CHK_STDERR_NOK.append(_a)
    elif _o in ("--stderrok",):
        _CHK_STDERR_OK.append(_a)

    #
    # *** stdout ***
    #
    elif _o in ("--stdoutnok",):
        _CHK_STDOUT_NOK.append(_a)
    elif _o in ("--stdoutok",):
        _CHK_STDOUT_OK.append(_a)

#     elif _o in ("--default-ok",):
#         _myRulesMap['default'] = 'OK'
#     elif _o in ("--default-nok",):
#         _myRulesMap['default'] = 'NOK'

    #
    # flags for re
    #
    elif _o in ("--redebug",):
        _myRulesMap['redebug'] = True
    elif _o in ("--redotall",):
        _myRulesMap['dotall'] = True
    elif _o in ("--reignorecase",):
        _myRulesMap['ignorecase'] = True
    elif _o in ("--remultiline",):
        _myRulesMap['multiline'] = True
    elif _o in ("--reunicode",):
        _myRulesMap['unicode'] = True

    #-------------------------------------------------------------
    #
    # ** output format ***
    #
    elif _o in ("--str",):
        _kargs['out'] = 'str'
        _out = _O_REPR
    elif _o in ("--repr",):
        _kargs['out'] = 'repr'
        _out = _O_REPR
    elif _o in ("--xml",):
        _kargs['out'] = 'xml'
        _out = _O_XML
    elif _o in ("--csv",):
        _kargs['out'] = 'csv'
        _out = _O_CSV
    elif _o in ("--pass",):
        _kargs['out'] = 'pass'
        _out = _O_PASS
    elif _o in ("--passall",):
        _kargs['out'] = 'pass'
        _out = _O_PASSA
    elif _o in ("--raw",):
        _kargs['raw'] = True
        _kargs['out'] = 'pass'
        _out = _O_PASSA



    #-------------------------------------------------------------
    #
    # *** framework misc - passed by kargs ***
    #

    elif _o in ("-a","--appname",):
        _appname = _a
    elif _o in ("--test-id",):
        _testid = _a
    elif _o in ("--timestamp",):
        _timestamp = True
    elif _o in ("--environment",):
        _environment = True

    elif _o == "--selftest":
        _selftest = True

    elif _o == "--slang":
        _slang = _a

    elif _o == "--subproc":
        _CALL_SUBPROC = SystemCalls
        _kargs['out'] = 'pass'
        _out = _O_PASSA

    elif _o == "--subunit":
        _CALL_SUBPROC = SubprocessUnit

    elif _o == "--exit-unit-failed":
        _exitokval = _a

    elif _o == "--exit-unit-ok":
        _exitnokval = _a

    # change classpath
    elif _o == "--cp":
        sys.path = _a
    elif _o == "--cp-prepend":
        sys.path.insert(0,_a+os.pathsep)
    elif _o == "--cp-append":
        sys.path.append(os.pathsep+_a)

    #
    # debug and trace
    #
    elif _o in ("-d","--debug",):
        _kargs['debug'] = True
        _debug += 1
    elif _o in ("-v","--verbose",):
        _verbose += 1


    elif _o in ("--version",):
        print str(__version__)
        sys.exit()

    elif _o in ("--Version",):
        print "app:      "+str(_APPNAME)
        print "version:  "+str(__version__)
        print "author:   "+str(__author__)
        print "copyright:"+str(__copyright__)
        print "license:  "+str(__license__)
        print "file:     "+str(os.path.basename(__file__))
        sys.exit()

    else:
        assert False, "unhandled option"+str(_o)


#
# assembled collections for rules
#
if _CHK_STDERR_NOK:
    _myRulesMap["stderrnok"] = _CHK_STDERR_NOK
if _CHK_STDERR_OK:
    _myRulesMap["stderrok"] = _CHK_STDERR_OK
if _CHK_STDOUT_NOK:
    _myRulesMap["stdoutnok"] = _CHK_STDOUT_NOK
if _CHK_STDOUT_OK:
    _myRulesMap["stdoutok"] = _CHK_STDOUT_OK


if _selftest: # do predefined selftest only
    import epyunit.selftest

    _myargs = {}
    if _out == _O_REPR:
        _myargs['out'] = 'repr'
    elif _out == _O_XML:
        _myargs['out'] = 'xml'
    elif _out == _O_PASS:
        _myargs['out'] = 'pass'
    elif _out == _O_PASSA:
        _myargs['out'] = 'pass-all'
    elif _out == _O_CSV:
        _myargs['out'] = 'csv'
    elif _verbose and not _out:
        _myargs['out'] = 'str'

    if _verbose:
        _myargs['verbose'] = _verbose
    if _debug:
        _myargs['debug'] = _debug

    if _rdbgfwd: # forward debugging status
        _myargs['rdbgforward'] = _rdbgfwd
        _myargs['rdbg'] = _rdbg

    if not _slang:
        if sys.platform == 'Windows':
            epyunit.selftest.selftest('python',**_myargs)
        else:
            epyunit.selftest.selftest('python',**_myargs)
    else:
        epyunit.selftest.selftest(_slang,**_myargs)

    sys.exit(0)


#
# on-demand passed through
#
if _rdbgfwd: # forward debugging status
    _mi = 0
    for x in _args:
        if x.startswith('-'):
            break
        _mi += 1
    if _mi == 0:
        _args.append('--rdbg')
        _args.append('--rdbgforward='+str(_rdbgfwd))
    else:
        _args.insert(_mi, '--rdbgforward='+str(_rdbgfwd))
        _args.insert(_mi, '--rdbg')

#
# normal procedure...
#
if _verbose>0:
    _kargs['verbose'] = _verbose
if _debug > 0:
    _kargs['debug'] = _debug

if _out in (_O_PASS,_O_PASSA,):
    _kargs['raw'] = True

_kargs.update(_myRulesMap)
sx = _CALL_SUBPROC(**_kargs)
if _debug > 0:
    print str(sx)+"\n"
ret = sx.callit(' '.join(_args))
if ret[0] == 126:
    print >>sys.stderr ,"check exec permissions of:"+str(' '.join(_args))
if _verbose+_debug > 0:
    print ret

# apply unittest filters
_unit_status = sx.apply(ret)

# display data
sx.displayit(ret)

# reply exit value
if _out in (_O_PASSA,): # pass all - including exit value of callee
    sys.exit(ret[0])

if _verbose or _debug:
    print "epyunit => "+str(_result)

if _unit_status:
    sys.exit(_exitokval)
else:
    sys.exit(_exitnokval)

#sys.exit(_result) # the exit value for the state of the wrapper itself
