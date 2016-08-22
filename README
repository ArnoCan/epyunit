epyunit
=======

Abstract
--------

The **ePyUnit package** provides extensions for the integrated 
**Testautomation and Debugging** of executables and scipts as subprocesses.

Technically **ePyUnit** provides extensions for the
**PyUnit** and **PyDev**/**Eclipse**  frameworks for blackbox tests 
and seamless integrated debugging of executables and scripts including nested  calls of subprocesses.
The standard frameworks, libraries and IDEs provide components as presented
by the following figure.::

    .                                 :
       +----------------+             :       +---------------------------+
       |    unittest    |             :       |  scripts and executables  |
       +---+------------+---+         :       +---+-----------------------+---+
           |   automation   |         :           |       debugging           |
           +----------------+         :           +---------------------------+
    .                                 :


These are extended by framework features for the
seamless cross-process integration of scripts and programs.::

    .
    +------------------------------+       +-----------------------------+
    |   automation and unittest    |       |   seamless cross-process    |
    |        for arbitrary         | <---> |          debugging          |
    |   scripts and executables    |       |                             |
    +------------------------------+       +-----------------------------+

    |<---                     seamless integration                   --->| 
    .

The included automation extension for the PyDev/Eclipse based debugging of 
- local and remote - Python subprocesses provides simplified support of detailed error analysis
in case of test failures.

Blueprint
---------

The *'ePyUnit' package* provides a minimal but sufficient approach in particular for
the low-effort test automation of scripts and tools suitable for operations of 
large scale application tests as well as for daily and advanced DevOps tasks.

* ePyUnit encapsulates processes and relies on PyUnit for commandline
  based unit and regression tests. The main focus is general blackbox testing
  of executables, for Python in addition the automation of PyDev debugging
  is included , see 'https://pythonhosted.org/epyunit/call_integration.html'.

* ePyUnit integrates into PyDev for the support of the graphical
  Eclipse IDE of unit testing and integrated graphical debugging,
  this is also supported for external processes started independently
  from the commandline, see 'https://pythonhosted.org/epyunit/pydevd_integration.html'.


The ePyUnit components call the wrapped process and read the execution results
from STDOUT, STDERR, and the exit value. The values are cached by Python 
variables either for further processing, or optional pass-through to the caller.

The architecture is based on the packages 'PyUnit' and 'PyDev'::


    
                       +-----------------------+     call      +-----------------------+
                       |                       |    ------>    |                       | 
    Subprocess         |        ePyUnit        |               |  Wrapped-Executable   | 
                       |                       |    <-----     |                       |
                       +-----------------------+     stdin     +-----------------------+
                                   |                 stderr                |
                                   |                 exit                  V
                                   |                           +-----------------------+
    PyDev Remote                   |                           |    PyDevRDC     |      Debug into subprocess
    Debug Server                   |                           +-----------------------+
                                   |                                       |
                   . . . . . . . . | . . . . . . . . . . . . . . . . . . . | . . . . . . . . 
                                   |                                       |
                                   V                                       V
                       +-----------------------+               +-----------------------+
    Python Units       |         PyUnit        |     <--->     |         PyDev         |
                       +-----------------------+               +-----------------------+
                           |               |                              |
                           V               V                             /         
                     +-----------+   +-----------+                      /
    IDE              |    CLI    |   |  Eclipse  |<--------------------/  
                     +-----------+   +-----------+ 
    

The test components collect internally the data of multiple output sources and 
decide based on the selection of the user parameters whether the test was successful or has failed.
Therefore a similar approach to Fuzzy-Logic is applied on mixed results consisting of partial
failures and success.
The provided scenarios are single level subprocesses::

    +----------------+      +------------+
    | Python-Process | <--> | Subprocess |
    +----------------+      +------------+

and nested multilevel scripts and executables as subprocesses::

    +----------------+      +------------+            +------------+
    | Python-Process | <--> | Subprocess | <- ... --> | Subprocess |  
    +----------------+      +------------+            +------------+

Where each level of subprocesses could start an arbitrary number of local and remote
subprocesses itself, and either correlate or pass-through the results.

The provided package comprises functional atoms for various UseCases, as well
as extension classes for the 'unittest' package to be used in combination
with PyUnit and PyDev..

The 'epyunit' package provides in particular:

* Support for unit tests of shell scripts - **bash** - from command line and Eclipse/PyDev

* The simplified reuse of executables as test-dummies within multiple test cases.

* The categorization of structures defined by the directory tree. 

* The support of arbitrary intermixed implementation languages for executables.

The implementation supports Python(>=2.7) and integrates into the Eclipse IDE 
with PyDev, and PyUnit. 

The package 'epyunit' is a spin off from the project 'UnifiedSessionsManager-2.0'.
 
For examples and patterns see subdirectories:

* UseCases

* tests
 
**Downloads**:

* Sourceforge.net: https://sourceforge.net/projects/epyunit/files/

* Github: https://github.com/ArnoCan/epyunit/

**Online documentation**:

* Documentation: https://pythonhosted.org/epyunit/

* API: https://pythonhosted.org/epyunit/epydoc/

* PyPi: https://pypi.python.org/pypi/epyunit/

**setup.py**

The installer adds a few options to the standard setuptools options.

* *build_doc*: Creates the integrated documentation for runtime systems including API in 'epyunit/build/apidoc/epyunit'.

* *install_doc*: Installs documents into source project 'epyunit/doc', and the 'HOME' or 'AppData'. 

* *build_sphinx*: Creates documentation for runtime system by Sphinx, html only. Calls 'callDocSphinx.sh'.

* *build_epydoc*: Creates documentation for runtime system by Epydoc, html only. Calls 'callDocEpydoc.sh'.

* *test*: Runs PyUnit tests by discovery.

* *--help-epyunit*: Displays this help.

* *--no-install-required*: Suppresses installation dependency checks, requires appropriate PYTHONPATH.

* *--offline*: Sets online dependencies to offline, or ignores online dependencies.

* *--exit*: Exit 'setup.py'.

After successful installation the 'selftest' verifies basic checks by:

  *epyunit --selftest*

with the exit value '0' when OK.

The option '-v' raises the degree of verbosity for inspection

  *epyunit --selftest -v -v -v -v*
 

Project Data
------------

* PROJECT: 'epyunit'

* MISSION: Extend the standard PyUnit package for arbitrary ExecUnits.

* VERSION: 00.01

* RELEASE: 00.01

* NICKNAME: 'Dromi'

* STATUS: alpha

* AUTHOR: Arno-Can Uestuensoez

* COPYRIGHT: Copyright (C) 2010,2011,2015-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez

* LICENSE: Artistic-License-2.0 + Forced-Fairplay-Constraints
  Refer to enclose documents:
  
  *  ArtisticLicense20.html - for base license: Artistic-License-2.0 

  *  licenses-amendments.txt - for amendments: Forced-Fairplay-Constraints

Versions and Releases
---------------------

**Planned Releases:**

* RELEASE: 00.00.00x - Pre-Alpha: Extraction of the features from hard-coded application into a reusable package.

* RELEASE: 00.01.00x - Alpha: Completion of basic features. 

* RELEASE: 00.02.00x - Alpha: Completion of features, stable interface. 

* RELEASE: 00.03.00x - Beta: Accomplish test cases for medium to high complexity.

* RELEASE: 00.04.00x - Production: First production release. Estimated number of UnitTests := 100.

* RELEASE: 00.05.00x - Production: Various performance enhancements.

* RELEASE: >         - Production: Stable and compatible continued development.

**Current Release: 00.01.014 - Alpha:**

Major Changes:

* Fixes.

* The most may already work on Mac-OS and MS-Windows and others too, but due to 
  priorities for now tested and released for Linux. Others are following soon.

* The documents are mostly complete, but still in review.

* Adapted structure for debug and unit test of multiple programming languages.

* Added tests.
 
Current test status:

**ATTENTION**: Some of the tests involve the remote debug feature of PyDev/Eclipse,
  thus require a running local RemoteDebugServer, see manuals.

* UnitTests: >590(CLI)/730(Eclipse)

* Use-Cases as UnitTests: >45

**Total**: >770

