Software Design - A Blueprint
*****************************

Layered Subcomponents for Reuse
===============================

The provided features for blackbox testst of subprocess calls are based standard Python packages with 
the additional components.
The internal architecture is hereby designed as a layered stack, where the subcomponents
components could be reused for other projects.
::

                                                      Application Layer
     
                                     .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
                                          |         |       |         |
                                          V         V       V         V

                                                              +-------------------+
    'unittest.TestCase'                                       |  TestExecutable   |
    integration                                               +-------------------+
                                                                        |
                                                       +--------------------------+
    Unittest management and                            |      SubprocessUnit      |
    state decision engine                              +--------------------------+
                                                                     |             
    Subprocess execution                       +----------------------------------+
    controller and data                        |           SystemCalls            |
    collector                                  +----------------------------------+
                                                  |                |       
                                        +------------------+       |
    Seamless debugger                   |    PyDevRDC    |       |
    integration for PyDev               +------------------+       |
    collector                                     |                |
                                                  V                V
                                     .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .

                                                      External Components
    


Components and Interfaces:

* `epyunit <epyunit_cli.html>`_  : Command line and batch interface.

* `unittest.subprocess <spunittest.html>`_ : Provide unit tests for sub-processes as blackbox system calls, contains 'TestExecutable'.

* `SubprocUnit <subprocessunit.html>`_ : Provide unit tests for sub-processes as blackbox system calls, contains 'SubprocessUnit'.

* `SystemCalls <systemcalls.html>`_ : Python class, wraps start of subprocesses by system calls, contains 'SystemCalls'.

* `PyDev remote debugging <pydeverdbg.html>`_  : Python class, automation of subprocess debugging by PyDev, contains PyDevRDC.


PyUnit Integration
==================

The overall integration with the support packages, PyUnit, and PyDev is as  follows. 
::

                                  +----------------------------------------+
    Python Units                  |                  ePyUnit               |   a minimalistic inerface for arbitrary executables 
                                  +----------------------------------------+   for unit tests and integrated remote debugging
                                        |    |    |             |
                                        |    |    |             V               generates and manages multiple sys.path
                                        |    |    V   +--------------------+    provides search for branches
    Advanced filesystem                 |    V        |  PyFilesysObjects  |    provides search by combined regexpr+glob+literals
     search                             V             +--------------------+    provides extended normpath, replaces
                                                                |                 'os.path.normpath',
                                                                |               cross-platform escape+unescape, integrates  
                                                                |                  with 're' and 'glob' expressions 
                                                                |                         
                                                                |                         
                                                 +-------------------------+    locates actual sources, modules, and calls
    Python file RTTI                             |       PySourceInfo      |    identifies actual search paths
                                                 +-------------------------+            
                                                          |
                                 . . . . . . . . . . . . . . . . . . . .
                                                          |
                                          +---------------+----------------+
    Unit Tests                            |              PyUnit            |    provides the Unit Library for CLI and GUI
                                          +----+----------------+----------+
                                               |                |
                                               V                |
                                  +------------------+          V
    IDE                           |  Eclipse+PyDev   |                          provides the framework for the GUI
                                  +------------------+



PyDev Subprocess Debugging for Eclipse
======================================

The provided features are based standard Python packages with 
the following additional components.
::

                                       +-------------------------------------+
    Subprocess debugging               |        ePyUnit                      |            auto localization and load of the 
                                       +-------------------------------------+               PyDev stub 'pydevd.py'
                                        |    |    |             |                         exec-wrapper for PyUnit
                                        |    |    |             V
                                        |    |    V   +----------------------+
    Advanced filesystem search          |    V        |   PyFilesysObjects   |            search for Eclipse and PyDev release,
                                        V             +----------------------+               'pydevd.py'
                                                                |                         
                                                +----------------------------+
    Python file RTTI                            |          PySourceInfo      |            identifies actual search path
                                                +----------------------------+            
                                                             |
                                 . . . . . . . . . . . . . . . . . . . . . . .
                                                             |
                                            +----------------+---------------+
    Unit Tests                              |              PyDev             |           provides the Integration into Eclipse
                                            +----------------+---------------+              and 'pdb'
                                                             |
                                       +---------------------+---------------+     
    IDE                                |      Eclipse        |       pdb     |           provides the framework for Python debug
                                       +---------------------+---------------+               and GUI



References
==========

* Eclipse - `<https://www.eclipse.org/>`_ 

* PyDev - `<http://www.pydev.org/>`_ 

* PyUnit - `<http://pyunit.sourceforge.net/>`_ 

* ePyUnit - `<https://pypi.python.org/pypi/epyunit>`_ 

* PyFileSysObjects - `<https://pypi.python.org/pypi/pyfilesysobjects>`_ 

* PySourceInfo - `<https://pypi.python.org/pypi/pysourceinfo>`_ 

