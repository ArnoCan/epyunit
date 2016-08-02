Software Design
***************

PyUnit Integration
==================

The provided features for blackbox testst of subprocess calls are based standard Python packages with 
the following additional components.
::

                                        +------------------------+
    Python Units                        |        ePyUnit         |            a minimalistic inerface for arbitrary executables 
                                        +------------------------+            for unit tests and integrated remote debugging
                                                    |
                                        +------------------------+
    Advanced filesystem search          |    PyFilesysObjects    |            generates and manages multiple sys.path
                                        +------------------------+            provides search for branches
                                                    |                         provides search by combined regexpr+glob+literals
                                                    |                         provides extended normpath, replaces 
                                                    |                            'os.path.normpath',
                                                    |                         cross-platform escape+unescape, integrates 
                                                    |                             with 're' and 'glob' expressions 
                                        +------------------------+
    Python file RTTI                    |      PySourceInfo      |            locates actual sources, modules, and calls
                                        +------------------------+            identifies actual search paths
                                                    |
                                                    |
                                 . . . . . . . . . . . . . . . . . . . .
                                                    |
                                       +------------+-------------+
    Unit Tests                         |          PyUnit          |           provides the Unit Library for CLI and GUI
                                       +------------+-------------+
                                               |             |
                                               V             |
                                       +---------------+     V
    IDE                                | Eclipse+PyDev |                      provides the framework for the GUI
                                       +---------------+



PyDev Subprocess Debugging for Eclipse
======================================

The provided features are based standard Python packages with 
the following additional components.
::

                                        +------------------------+
    Subprocess debugging                |        ePyUnit         |            auto localization and load of the 
                                        +------------------------+               PyDev stub 'pydevd.py'
                                                    |                         exec-wrapper for PyUnit
                                        +------------------------+
    Advanced filesystem search          |    PyFilesysObjects    |            search for Eclipse and PyDev release,
                                        +------------------------+               'pydevd.py'
                                                    |                         
                                        +------------------------+
    Python file RTTI                    |      PySourceInfo      |            identifies actual search path
                                        +------------------------+            
                                                    |
                                 . . . . . . . . . . . . . . . . . . . .
                                                    |
                                       +------------+-------------+
    Unit Tests                         |          PyDev           |           provides the Integration into Eclipse
                                       +------------+-------------+              and 'pdb'
                                                    |
                                       +------------+-------------+     
    IDE                                |   Eclipse  |      pdb    |           provides the framework for Python debug
                                       +------------+-------------+               and GUI



Components and Interfaces
=========================

* `epyunit <epyunit_cli.html>`_  : Command line and batch interface.

* `SubprocUnit <subprocessunit.html>`_ : Provide unit tests for sub-processes as blackbox system calls.

* `SystemCalls <systemcalls.html>`_ : Python class, wraps start of subprocesses by system calls.

* `PyDev remote debugging <pydeverdbg.html>`_  : Python class, automation of subprocess debugging by PyDev.



References
==========

* Eclipse - `<www.eclipse.org>`_ 

* PyUnit - `<pyunit.sourceforge.net>`_ 

* ePyUnit - `<https://pypi.python.org/pypi/epyunit>`_ 

* PyFileSysObjects - `<https://pypi.python.org/pypi/pyfilesysobjects>`_ 

* PySourceInfo - `<https://pypi.python.org/pypi/pysourceinfo>`_ 


