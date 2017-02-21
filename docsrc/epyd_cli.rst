'epyd' - Command line interface for pydevd.py
---------------------------------------------

SYNOPSIS:
^^^^^^^^^
  ::

    epyd [OPTIONS]

OPTIONS:
^^^^^^^^
.
  \--force

    Force selected parameters, ignore standard constraints.

  \--package

     Package the current 'pysrc' into a deployment archive
     for remote debugging.
     
     *REMARK*: current implementation packages the complete
     'pysrc' subdirectory, which actually seems not 
     to be required.

  \--package-type=(zip|tar.gz)

     Type of archive.

  \--package-path=<filepathname-package>

     The file pathname for the package to create.

  \--package-print
     Prints the path name of the created package to stdout.

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

ARGUMENTS:
^^^^^^^^^^

  none.

DESCRIPTION:
^^^^^^^^^^^^

The epyd commandline interface provides a helpers for the
preparation of remote debugging.

ENVIRONMENT:
^^^^^^^^^^^^

  * PYTHON OPTIONS:
    -O, -OO: Eliminates '__debug__' code.
 
EXAMPLES:
^^^^^^^^^

.. _examples:

Some simple call examples are:
  ::

    epyunit -- myscript.sh EXITOK
    epyunit -- myscript.sh EXITNOK
    epyunit -- myscript.sh EXIT8

A call example for cross-process-border remote debugging:
  ::

    epyunit --rdbg -- epyunit --rdbg -- myscript.sh EXITNOK
    0.                1.                2.

  #. Start outmost process from command line and attach it
     to PyDev by stub. 
     ::

       epyunit --rdbg

  #. Start level-01 subprocess outermost process and attach it
     to PyDev by stub. 
     ::

       epyunit --rdbg -- epyunit --rdbg

  #. Start level-02 subprocess, here a shell script from level-2 subprocess,
     and attach it to PyDev by stub. 
     ::

       epyunit --rdbg -- epyunit --rdbg -- myscript.sh EXITNOK

Additional examples could be found within the source code, unit tests, and UseCases.


* `CLI: command line interface <epyunit_example_cli.html>`_ 

* `Eclipse: Executable within Eclipse IDE <epyunit_example_eclipse_executable.html>`_ 

* Detailed examples in the subdirectories of the source package:

  * tests + testdata 

  * UseCases

COPYRIGHT:
^^^^^^^^^^

  Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez
  Copyright (C)2015-2016 Arno-Can Uestuensoez
