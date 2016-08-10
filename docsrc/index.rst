Abstract
========

The **'ePyUnit' package** provides extensions for the 
**PyUnit** framework for blackbox tests of executables
including nested  calls of subprocesses.
The included automation extension for the **PyDev** based debugging of 
- local and remote - Python subprocesses provides simplified support of detailed error analysis.
The coming versions are going to support the full scope of features on arbitrary local and 
remote distributed processes.


The *'ePyUnit' package* provides a minimal but sufficient approach in particular for
the low-effort test automation of scripts and tools.

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
    Subprocess         |        epyunit        |               |  Wrapped-Executable   | 
                       |                       |    <-----     |                       |
                       +-----------------------+     stdin     +-----------------------+
                                   |                 stderr                |
                                   |                 exit                  V
                                   |                           +-----------------------+
    PyDev Remote                   |                           |    PyDevRemoteDBG     |      Cross-Process Debugging into 
    Debug Server                   |                           +-----------------------+      local and remote subprocesses
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

and nested multilevel subprocesses
  ::

    +----------------+      +------------+            +------------+
    | Python-Process | <--> | Subprocess | <- ... --> | Subprocess |  
    +----------------+      +------------+            +------------+

Where each level of subprocesses could start an arbitrary number of local and remote
subprocesses itself, and either correlate or pass-through the results.
The provided package comprises functional atoms for various UseCases, as well
as extension classes for the 'unittest' package to be used in combination
with PyUnit and PyDev..

* `Test Syntax, Rules, and Correlation <rules_logic.html>`_

* `Common call integration of subprocess units <call_integration.html>`_ 

* `Integration into the  Class Hierarchy of PyUnit <unittest_subprocesses.html>`_ 

* `Automation of Subprocess Debugging and Test-Integration by 'pydevd.py' <pydevd_integration.html>`_ 

For the implementation and architecture refer to

* `Software design <software_design.html>`_ 

* `Python library functions <call_integration.html>`_ 

* `spUnittest module <unittest_subprocesses.html>`_ 

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

`Shortcuts <shortcuts.html>`_
=============================

* `Rules and Combination Logic <rules_shortcuts.html>`_

* `Commandline Interface <shortcuts.html>`_

* `Programming Interface <shortcuts.html>`_

* `Selected Common UsesCases <usecases.html>`_

* `Integration of PyDev Remote Debug Server - 'pydevd.py' <pydevd_integration.html>`_

Table of Contents
=================

.. toctree::
   :maxdepth: 3

   shortcuts
   usecases

   call_integration
   pydevd_integration

   epyunit
   rules_logic
   rules_shortcuts
   subprocessunit
   systemcalls
   selftest
   pydeverdbg
   UseCases
   tests
   testdata
   clioptutils_syntax
   commandline_tools
   epyunit_cli
   epyunit_example_cli
   epyunit_example_eclipse_executable
   epyunit_example_eclipse_python
   eclipse_integration
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

