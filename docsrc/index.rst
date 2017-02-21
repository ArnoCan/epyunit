Abstract
========

The **ePyUnit package** provides extensions for the integrated 
**Testautomation and Debugging** of executables and scipts as subprocesses.
 
Technically **ePyUnit** provides extensions for the
**PyUnit** and **PyDev**/**Eclipse**  frameworks for blackbox tests 
and seamless integrated debugging of executables and scripts including nested  calls of subprocesses.
The standard frameworks, libraries and IDEs provide components as presented
by the following figure. 
::

    .                                 :
       +----------------+             :       +---------------------------+
       |    unittest    |             :       |  scripts and executables  |
       +---+------------+---+         :       +---+-----------------------+---+
           |   automation   |         :           |       debugging           |
           +----------------+         :           +---------------------------+
    .                                 :


These are extended by framework features for the
seamless cross-process integration of scripts and programs.
::

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


REMARK - Release
================

Current release seems to be quite good and stable on Linux, Windows too with a few required enhancements.
Mac-OS may work too, wil be tested soon together with BSD and Solaris.

Blueprint
=========
The *'ePyUnit' package* provides a minimal but sufficient approach in particular for
the low-effort test automation of scripts and tools suitable for operations of 
large scale application tests as well as for daily and advanced DevOps tasks.

* ePyUnit encapsulates processes and relies on PyUnit for commandline
  based unit and regression tests. The main focus is general blackbox testing
  of executables, for Python in addition the automation of PyDev debugging
  is included  
  `[details] <call_integration.html>`_ .

* ePyUnit integrates into PyDev for the support of the graphical
  Eclipse IDE of unit testing and integrated graphical debugging,
  this is also supported for external processes started independently
  from the commandline
  `[details] <pydevd_integration.html>`_ .


The ePyUnit components call the wrapped process and read the execution results
from STDOUT, STDERR, and the exit value. The values are cached by Python 
variables either for further processing, or optional pass-through to the caller.
  ::

    
                       +-----------------------+     call      +-----------------------+
                       |                       |    ------>    |                       | 
    Unit tests for     |        epyunit        |               |  Wrapped-Executable   | 
    Subprocess         |                       |    <-----     |                       |
                       +-----------------------+     stdin     +-----------------------+
                                   |                 stderr                |
                                   |                 exit                  V
                                   |                           +-----------------------+      Cross-Process Debugging into
    PyDev Remote                   |                           |        PyDevRDC       |      local and remote subprocesses 
    Debug Server                   |                           +-----------------------+      by the PyDev Remote Debug Client
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

The automation of the subprocess debug integration into the PyDev/Eclipse debugging framework
provides for seamless debugging of cross-process unittest.
For an integrated example refer to `sequences of control flow [Design details] <pydevd_integration.html#design>`_,
for the analysing logic and rules of test results refer to is provided by 
`Test Syntax, Rules, and Correlation [details] <rules_logic.html#>`_.
The provided scenarios are single level subprocesses
::

    +----------------+      +------------+
    | Python-Process | <--> | Subprocess |
    +----------------+      +------------+

and nested multilevel scripts and executables as subprocesses
::

    +----------------+      +------------+            +------------+
    | Python-Process | <--> | Subprocess | <- ... --> | Subprocess |  
    +----------------+      +------------+            +------------+

Where each level of subprocesses could start an arbitrary number of local and remote
subprocesses itself, and either correlate or pass-through the results.

The provided extension class 'epyunit.unittest.subprocess.TestProcesss' extends the standard class
'unittest.case.TestCase'
::

    .                                                                      :
                                      +------------------------------+     :     +-----------------------------------+
    standard unittest                 |                              |     :     |                                   |
    automation and alternative        |   Automation and Unittest    |     :     |              Debug                |
    debugging                         |   unittest.case.TestCase     |     :     |          by PyDev - pdb           |
                                      |                              |     :     |                                   |
                                      +------------------------------+     :     +-----------------------------------+
                                                                           :
                                      |<---     Eclipse / CLI   --->|      :     |<---    Eclipse+PyDev / pdg    --->|
    .

by framework features for the
integrated seamless unittest and debugging of scripts and programs as subprocesses.
::

    .
                            +-----------------------------------------+           +-----------------------------------+
                            |                                         |           |                                   |
    integrated subprocess   |           Scripts and Programs          |           |    seamless debug automation      |
    automation for          | epyunit.unittest.subprocess.TestProcess |   <--->   |  epyunit.debug.pydevrdc.PyDevRDC  |
    unittest with seamless  |                                         |           |                                   |
    debugging               +-----------------------------------------+           +-----------------------------------+
    
                            |<---                          Eclipse / PyDev / PyUnit / CLI                         --->|
    .


The provided package comprises functional atoms for various UseCases, as well
as extension classes for the 'unittest' package to be used in combination
with PyUnit and PyDev.

* `Test Syntax, Rules, and Correlation <rules_logic.html>`_

* `Common call integration of subprocess units <call_integration.html>`_ 

* `Integration into the  Class Hierarchy of PyUnit <unittest_subprocesses.html>`_ 

* `Automation of Subprocess Debugging and Test-Integration by 'pydevd.py' <pydevd_integration.html>`_ 

For the implementation and architecture refer to

* `Software design <software_design.html>`_ 

* `Python library functions <call_integration.html>`_ 

* `unittest.subprocess module <unittest_subprocesses.html>`_ 

Application examples for ePyUnit see the multiplatform bash extensions:

.. hlist::
   :columns: 4

   * `bash-core <https://sourceforge.net/projects/bash-core/>`_ 
   * `bash-core-lib <https://sourceforge.net/projects/bashcorelib/>`_ 
   * `bash-core-autotools <https://sourceforge.net/projects/bash-core-autotools/>`_ 
   * `bash-core-batch <https://sourceforge.net/projects/bash-core-batch/>`_ 
   * `bash-core-completion <https://sourceforge.net/projects/bash-core-completion/>`_ 
   * `bash-core-env <https://sourceforge.net/projects/bash-core-env/>`_ 
   * `bash-core-install <https://sourceforge.net/projects/bash-core-install/>`_ 
   * `bash-core-extmods <https://sourceforge.net/projects/bash-core-extmods/>`_ 
   * `bash-core-lang <https://sourceforge.net/projects/bash-core-lang/>`_ 

Install
=======

* **Supported Platforms**:

  The following platforms are in general fully supported, see remarks for some exceptions.

  * OS:

    * Linux: Fedora, CentOS, RHEL, Debian

      Any other should work too!
      Try - same for generic by sources on all:
        ::

          python setup.py install --user
          python setup.py install --user --offline
          python setup.py install --help-epyunit

      Distribution: source, tar.gz, rpm

    * MS-Windows: Windows7 

      Bash is deactivated by default, document creation not yet supported, requires Linux and bash.

      Distribution: source, tar.gz, MSI

    * CygWin

      Defaults are adapted to MS-Windows mode.

      Distribution: source, tar.gz

    * Apple-MacOS: SnowLeopard(10.6.2)

      Requires Python(>=2.7) and bash(>4.1) update
  
      Distribution: source, tar.gz

    * OpenBSD

      Distribution: source

    * Solaris

      Distribution: source

  * bash: Requires bash for document creation >= 4.1

  * Perl: Currently basics only, recommended Perl5

  * Python: Requires Python 2 >= 2.7

  * Test simulators:

    These require an appropriate simulation with minimal common language standard.

      bash, Perl, Python, 

* **Install**:

  Required packages:

  * pysourceinfo >=0.1.9 - `<https://pypi.python.org/pypi/pysourceinfo>`_

  * pyfilesysobjects >= 0.1.11 - `<https://pypi.python.org/pypi/pyfilesysobjects>`_

  Standard procedure online local install by sources::

    python setup.py install --user

  Custom procedure offline by::

    python setup.py install --user --offline

  Documents, requires Sphinx and Epydoc::

    python setup.py build_doc install_doc

* **Introduction**:

  For now refer to the listed API and subdocument collection in section 
  :ref:`'Shortcuts' <shortcuts>`

HowTo
=====

* `Remote Debug <howtodebug.html>`_

`Shortcuts <shortcuts.html>`_
=============================

Concepts and workflows:

* Rules and Combination Logic 
  `[details] <rules_logic.html>`_

* Integration of PyDev Remote Debug Server 'pydevd.py'
  `[shortcuts] <shortcuts.html#epyunit.pydeverdbg>`_
  `[example] <UseCases.remote_debug.html>`_
  `[details] <pydevd_integration.html>`_
  `[PyDev-Online-Manual] <http://pydev.org/manual_adv_remote_debugger.html>`_

Use-Cases `[usecases] <usecases.html>`_

* Types of Call Interfaces `[usecases] <usecases.html#binaries-and-selftest>`_
* Selected Use-Cases `[usecases] <usecases.html#selected-use-cases>`_

  * Types of Simulator Responses `[usecases] <usecases.html#types-of-simulator-responses>`_
  * Types of Expected Test Results `[usecases] <usecases.html#types-of-expected-test-results>`_

* Subprocess Debugging `[usecases] <usecases.html#subprocess-debugging>`_
* Project Applications¶ `[usecases] <usecases.html#project-applications>`_


Interfaces:

* Commandline Interface `[call-interface] <shortcuts.html#epyunit-cli>`_

* Programming Interface `[API-Selection] <shortcuts.html#epyunit-spunittest>`_

* Test data generators `[myscript.<prog-language>] <shortcuts.html#epyunit-myscript>`_

Technical API:

* Interface in javadoc-style `[API] <epydoc/index.html>`_

Table of Contents
=================

.. toctree::
   :maxdepth: 3

   shortcuts
   usecases

   call_integration
   pydevd_integration
   eclipse_integration

   epyunit_cli
   epyd_cli
   epyunit
   rules_logic
   rules_shortcuts
   subprocessunit
   systemcalls
   selftest
   pydeverdbgchk
   pydeverdbg
   myscript-py
   UseCases
   tests
   testdata
   clioptutils_syntax
   commandline_tools
   epyunit_example_cli
   epyunit_example_eclipse_executable
   epyunit_example_eclipse_python
   commandline_scripting

   software_design

* setup.py

  For help on extensions to standard options call onlinehelp:: 

    python setup.py --help-epyunit



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Resources
=========

For available downloads refer to:

* Python Package Index: https://pypi.python.org/pypi/epyunit

* Sourceforge.net: https://sourceforge.net/projects/epyunit/

* github.com: https://github.com/ArnoCan/epyunit/

For Licenses refer to enclosed documents:

* Artistic-License-2.0(base license): `ArtisticLicense20.html <_static/ArtisticLicense20.html>`_

* Forced-Fairplay-Constraints(amendments): `licenses-amendments.txt <_static/licenses-amendments.txt>`_ / `Protect OpenSource Authors <http://xkcd.com/1303/>`_

