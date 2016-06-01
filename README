epyunit
=======

The 'epyunit' package provides extensions of the 
PyUnit framework for unit and regression tests of executables written in
arbitrary languages.
In distinction to some more comprising and though complex frameworks the 
'epyunit' provides a minimal but sufficient approach in particular for
the low-effort test automation of scripts and tools.

The reuse of the standard PyUnit in combination with PyDev 
provides out-of-the-box integration into the Eclipse-IDE.
Thus command line based regression tests as well as a graphical 
frontend for test statistics provided by PyDev could be applied. 

The epyunit components call the wrapped process and read the execution results
from STDOUT, STDERR, and the exit value. The values are read into Python 
variables either for further processing, or optional pass-through to the caller.
 
The 'epyunit' package provides in particular:

* Support for unit tests of shell scripts - **bash** - from command line and Eclipse/PyDev

* The simplified reuse of executables as test-dummies within multiple test cases.

* The categorization of structures defined by the directory tree. 

* The support of arbitrary intermixed implementation languages for executables.

The implementation supports Python(>=2.7) and integrates into the Eclipse IDE 
with PyDev, and PyUnit. 

The package 'epyunit' is a spin off from the project 'UnifiedSessionsManager-2.0'.
 
The main interface classes are:

* **FileSysObjectsMin** - A subset of the project PyFileSysObjects.

* **SystemCalls** - Adaptation of sub-process calls for unit tests.


The architecture is based on the packages 'PyDev'::


    
                    +-----------------------+   call    +----------------------+
                    |                       |  ------>  |                      | 
    Subprocess      |        ePyUnit        |           |   Wrapped-Process    | 
                    |                       |  <-----   |                      |
                    +-----------------------+   stdin   +----------------------+
                                |               stderr
                                V               exit
                    +-----------------------+
    Python Units    |         PyUnit        |
                    +-----------------------+  
                                |
                                V
                    +-----------+-----------+
    IDE             |  Eclipse  |    CLI    |    
                    +-----------+-----------+ 
    

For examples and patterns see subdirectories:

* UseCases

* tests
 
**Downloads**:

* Sourceforge.net: https://sourceforge.net/projects/epyunit/files/

* Github: https://github.com/ArnoCan/epyunit/

**Online documentation**:

* https://pypi.python.org/pypi/epyunit/
* https://pythonhosted.org/epyunit/

setup.py
--------

The installer adds a few options to the standard setuptools options.

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

* VERSION: 00.00

* RELEASE: 00.00

* NICKNAME: 'Dromi'

* STATUS: pre-alpha

* AUTHOR: Arno-Can Uestuensoez

* COPYRIGHT: Copyright (C) 2010,2011,2015-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez

* LICENSE: Artistic-License-2.0 + Forced-Fairplay-Constraints
  Refer to enclose documents:
  
  *  ArtisticLicense20.html - for base license: Artistic-License-2.0 

  *  licenses-amendments.txt - for amendments: Forced-Fairplay-Constraints

VERSIONS and RELEASES
---------------------

**Planned Releases:**

* RELEASE: 00.00.00x - Pre-Alpha: Extraction of the features from hard-coded application into a reusable package.

* RELEASE: 00.01.00x - Alpha: Completion of basic features. 

* RELEASE: 00.02.00x - Alpha: Completion of features, stable interface. 

* RELEASE: 00.03.00x - Beta: Accomplish test cases for medium to high complexity.

* RELEASE: 00.04.00x - Production: First production release. Estimated number of UnitTests := 100.

* RELEASE: 00.05.00x - Production: Various performance enhancements.


**Current Release: 00.00.001 - Pre-Alpha:**

Major Changes:

* Introduce initial version.


Current test status:

* UnitTests: >9

* Use-Cases as UnitTests: >70

**Total**: >79

