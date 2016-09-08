"""
Common test data
================
Common data for 'UseCases' and 'tests'. Refer to the package by PYTHONPATH.
The global variable 'testdata.mypath' provides the pathname into 'testdata'.
This includes also some common basic references to test utilities.
"""
__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.2.0'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

import os,sys
import filesysobjects.FileSysObjects
mypath = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))


#
# Python interpreter
#
_callpy = sys.executable
"""The standard 'Python' interpreter for current platform."""
if not _callpy:
    _callpy = 'python ' # should not be required


#
# bash interpreter
#
_callsh = os.environ.get("BASH")
"""The standard 'bash' interpreter for current platform."""
_sp = [ os.environ.get("PATH") ]
_sp.extend(sys.path)
if not _callsh and sys.platform in ('cygwin',):
    _callsh = filesysobjects.FileSysObjects.findRelPathInSearchPath('bash',['/usr/bin'])
    if not os.path.exists(_callsh):
        _callsh = None
if not _callsh:
    _callsh = filesysobjects.FileSysObjects.findRelPathInSearchPath('bash')
if not _callsh:
    _callsh = filesysobjects.FileSysObjects.findRelPathInSearchPath('bash.exe', _sp, subsplit=True)
if not _callsh:
    _callsh = 'bash ' # should not be required

#
# Perl interpreter
#
_callpl = os.environ.get("PERL", "perl")
"""The standard 'perl' interpreter for current platform."""
_sp = [ os.environ.get("PATH") ]
_sp.extend(sys.path)
if not _callsh and sys.platform in ('cygwin',):
    _callpl = filesysobjects.FileSysObjects.findRelPathInSearchPath('perl',['/usr/bin'])
    if not os.path.exists(_callpl):
        _callsh = None
if not _callpl:
    _callpl = filesysobjects.FileSysObjects.findRelPathInSearchPath('perl')
if not _callsh:
    _callpl = filesysobjects.FileSysObjects.findRelPathInSearchPath('perl.exe', _sp, subsplit=True)
if not _callpl:
    _callpl = 'perl ' # should not be required

#
# ---------------------------
#

scrish = os.path.abspath(os.path.normpath(mypath+"/../epyunit/myscript.sh"))
"""The projects test simulator as bash script"""

scripy = os.path.abspath(os.path.normpath(mypath+"/../epyunit/myscript.py"))
"""The projects test simulator as Python script"""

scripl = os.path.abspath(os.path.normpath(mypath+"/../epyunit/myscript.pl"))
"""The projects test simulator as Perl script"""

#
# ---------------------------
#

epyu = _callpy + " " + os.path.abspath(os.path.normpath(mypath+"/../bin/epyu.py"))
"""The projects commandline interface epyu.py"""


if _callsh:
    call_scrish = _callsh + " " + scrish
else:
    call_scrish = None
if _callpy:
    call_scripy = _callpy + " " + scripy
else:
    call_scripy = None
if _callpl:
    call_scripl = _callpl + " " + scripl
else:
    call_scripl = None

#
# ---------------------------
#

#
# for now hardcoded
#
_available_bash    = False
_available_perl    = False
_available_python  = False

if sys.platform.startswith('linux'): # Linux
    _available_bash    = True
    _available_perl    = True
    _available_python  = True
elif 'win32' in sys.platform : # Windows
    _available_bash    = False
    _available_perl    = False # for now by default not
    _available_python  = True
elif sys.platform in ('cygwin',): # Cygwin
    _available_bash    = True
    _available_perl    = True
    _available_python  = True
elif sys.platform in ('darwin'): # Mac-OS
    _available_bash    = True
    _available_perl    = True
    _available_python  = True # reminder: requires 2 with >=2.7
else: # Else: Unix, BSD
    _available_bash    = True
    _available_perl    = True
    _available_python  = True



# __all__ = [
#     "TestHelper",
# ]
