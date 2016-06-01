
.. epyunit documentation master file, created by
   sphinx-quickstart on `date`.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

'epyunit' - Unit tests of arbitrary executables by PyUnit
=========================================================

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
::

    
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
    


The test components collect internally the data of multiple output sources and 
decide based on the selection of the user whether the test was successful or failed.
The options therefore comprise output content related options, and additional 
weight options, defining priorities for the combination of the partial result.

The basic test output evaluation of the called process is based on one or more of:

* **stdout** - Arbitrary output written to stdout.

* **stderr** - Arbitrary output written to stderr.

* **exit code** - Exit code value.

The following options define the expected dominant values in order 
to resolve ambiguity when multiple criteria is matched:

* prio-ok, prio-nok

* exit-ignore, exit-ok, exit-nok

For details refer to 
`"Call Integration" <call_integration.html>`_ .
Call examples are provided by:

* `CLI: command line interface <epyunit_example_cli.html>`_ 

* Eclipse: PyDev integration by call of:

  * `Executable <epyunit_example_eclipse_executable.html>`_ 

  * `Python API <epyunit_example_eclipse_python.html>`_ 


The addons introduces the basic support components required for using
the filesystem as a drop-in container of units with basic lightweight object
orientation for filesystem trees.
This comprises in particular the upward directory tree search in order
to simulate inheritance and superposition of executables within 
the upper tree of the caller. 
The downward search is provided by the 'explore' feature of PyUnit. 

The provided feature modules comprise the following list for the automation 
of unit tests by arbitrary processes, for code examples 
refer to 'epyunit.UseCases.examples'.

* `FileSysObjectsMin <fileobjects.html>`_ : Manage branches of filesystem structures with support of basic file inheritance - *epyunit.FileSysObjectsMin*.

* `SystemCalls <systemcalls.html>`_ : Wraps system calls, particularly subprocess calls - *epyunit.SystemCalls*.

In addition the following main utilities are provided:
 
* `epyunit <epyunit_cli.html>`_  : Command line interface.

This document provides the developer information for the API, Use-Cases, and the 
documentation of the PyUnit tests as examples and application patterns.

* `Commandline tools <commandline_tools.html>`_ 
 
  * `epyunit <epyunit_cli.html>`_ 


.. toctree::
   :maxdepth: 3

   epyunit
   UseCases
   tests

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

