#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""'epyd' - Command line interface for management of pydevd.py

The epyd commandline interface provides a helpers for the
preparation of remote debugging.

**SYNOPSIS**:

  epyd [OPTIONS]

**OPTIONS**:
.

  **epyd-options**:

    --force

      Force selected parameters, ignore standard constraints.

    --package

      Package the current 'pysrc' into a deployment archive
      for remote debugging.

      *REMARK*: current implementation packages the complete
      'pysrc' subdirectory, which actually seems not
      to be required.

    --package-type=(zip|tar.gz)

      Type of archive.

    --package-path=<filepathname-package>

      The file pathname for the package to create.

    --package-print

      Prints the path name of the created package to stdout.

    --no-rdbg

      Suppress the actual start of remote debugging when '--rdbg'
      is set, just scans and reads the rdbg-options for analysis.

  **rdbg-options**:

    --rdbg

      the remote debugging peer for this instance

    --rdbg-fwd

      requested state forwarding to nested subprocess levels

    --rdbg-root

      rootdirectory of eclipse

    --rdbg-sub

      sub directory of PyDev for 'pydevd.py'

  **common options**:

    -d --debug

      Debug entries, does NOT work with 'python -O ...'.
      Developer output, aimed for filtering.

    -h --help

      This help.

    -Version --Version

      Current version - detailed.

    -v --verbose

      Verbose.

    -version --version

      Current version - terse.

**ARGUMENTS**:

  none.

**ENVIRONMENT**:

  * PYTHON OPTIONS:

    -O, -OO: Eliminates '__debug__' code.


**EXAMPLES**:

  Basic calls:

  * epyd --enumerate

**SEE ALSO**:

  * https://pypi.python.org/pypi/epyunit/

  * https://pythonhosted.org/epyunit/

**COPYRIGHT**:
  Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez
  Copyright (C)2015-2017 Arno-Can Uestuensoez

"""
from __future__ import absolute_import
#from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.2.9'
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
    _APPNAME = "epyd"

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

    #
    "enumerate",
    "package","package-type=","package-path=","package-print",
    "force",
    "no-rdbg",

    # misc
    "help","debug","verbose","version","Version",

]
_sopts = "hdv"

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

  epyd

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
# activate remote debug stub call
import epyunit.debug.pydevrdc
if _rdbgthis and not '--no-rdbg' in sys.argv:
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

_package = False
_package_type = 'zip'
"""Package type for remote stub."""
_package_path = None

_package_print = False

_altpat = "org.python.pydev_[0-9]*.[0-9]*.[0-9]*201*/pysrc/pydevd.py"
"""Search pattern for pydevd.py"""

_force = False

for _o,_a in _opts:

    #
    if _o in ("--enumerate",):
        pass

    elif _o in ("--package",):
        _package = True

    elif _o in ("--package-print",):
        _package_print = True

    elif _o in ("--package-type",):
        if _a.lower() in ('zip', 'tar.gz',):
            _package_type = _a.lower()
        else:
            print >>sys.stderr, "ERROR:Unknown package type:"+str(_a)
            sys.exit(1)
        pass

    elif _o in ("--package-path",):
        _package_path = _a

    elif _o in ("--force",):
        _force = True

    elif _o in ("--no-rdbg",):
        _kargs['nordbg'] = True
        _nordbg = 1

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
# normal procedure...
#
if _verbose>0:
    _kargs['verbose'] = _verbose
if _debug > 0:
    _kargs['debug'] = _debug

if _package:
    sx = epyunit.debug.checkRDbg.scanEclipseForPydevd()
    sx = os.path.dirname(sx)

    if not _package_path:
        _package_path = os.path.dirname(sx)
        if _package_type in ('zip',):
            _package_path += '.zip'
        elif _package_type in ('tar.gz',):
            _package_path += '.tar.gz'

    if _verbose:
        print "# Package path name: "+str(_package_path)

    if _verbose:
        print "# Package type: "+str(_package_type)

    if os.path.exists(_package_path):
        if _force:
            if _verbose:
                print "# Package exist, rewrite now."
            pass
        else:
            print >>sys.stderr, "ERROR:Package exists:"+str(_package_path)
            sys.exit(1)

    import errno
    from shutil import copy,copytree

    def copydir(src, dest):
        try:
            copytree(src, dest+os.path.sep+os.path.basename(src))
        except Exception as e:
            # fetch contents too
            if e.errno == errno.ENOTDIR:
                copy(src, dest)
            else:
                print('ERROR:Directory not copied: %s' % e)

    # prep archive
    from shutil import copyfile,rmtree
    _tempbuf = _package_path+'.d' + os.path.sep + os.path.basename(_package_path)
    if _tempbuf.endswith('.zip'):
         _tempbuf = _tempbuf[:-4]
    elif _tempbuf.endswith('.tar.gz'):
         _tempbuf = _tempbuf[:-7]
    else:
        print >>sys.stderr, "ERROR:Supports only archive types: 'zip' or 'tar.gz'"
        sys.exit(1)
    _pkgname_rel = os.path.basename(_tempbuf)
    _tempbuf = os.path.dirname(_tempbuf)

    if _force and os.path.exists(_tempbuf):
        rmtree(_tempbuf)
    os.mkdir(_tempbuf+os.path.sep)
    os.mkdir(_tempbuf+os.path.sep+_pkgname_rel)

    copydir(sx, _tempbuf+os.path.sep+_pkgname_rel)
    _c = os.path.curdir
    os.chdir(_tempbuf)

    if _package_type in ('zip',):
        from zipfile import ZipFile
        with ZipFile(_package_path, 'w') as myarch:
            for root, dirs, files in os.walk(_pkgname_rel):
                for file in files:
                    myarch.write(os.path.join(root, file))
                    #myarch.write(_pkgname_rel)
                pass

    elif _package_type in ('tar.gz',):
        import tarfile

        tar = tarfile.open(_package_path, 'w:gz')
        for root, dirs, files in os.walk(_pkgname_rel):
            for file in files:
                tar.add(os.path.join(root, file))
            pass
        tar.close()
        pass

    if _package_print:
        print "# Output created archive: "+str(os.path.basename(_package_path))
        print _package_path
else:
#    sx = epyunit.debug.pydevrdc.PYDEVD.scanEclipseForPydevd(**{'altpat':_altpat,})
    sx = epyunit.debug.checkRDbg.scanEclipseForPydevd(_rdbgroot, altpat=_rdbgsub)
#_rdbgthis,_rdbg,_rdbgfwd,, = epyunit.debug.checkRDbg.checkAndRemoveRDbgOptions(**{'label':_APPNAME,})
    print sx
