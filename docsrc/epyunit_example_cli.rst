Command line call examples
==========================

A call example of the the command line interface, 
for syntax details refer to the call wrapper
`epyunit <epyunit_cli.html>`_ .

The test executable is a simple shell script named
'myscript.sh' 
`[doc] <myscript-sh.html>`_
`[source] <myscript-sh.html>`_
demonstrating some of the major cases. 
The indication supported by this simulated blackbox 
here consists of 'signalling' strings, exit values, 
and none of them as the user defined default case.

The commandline wrapper calls are:

* case 'A'::

    epyunit \
      --ok-stdout="arbitrary signalling OK string" \
      myscript.sh OK

* case 'B'::

    epyunit \
      --nok-stderr="arbitrary signalling ERROR string" \
      myscript.sh NOK

* case 'C'::

    epyunit \
      --ok-stdout="arbitrary signalling OK string" \
      --nok-stderr="arbitrary signalling ERROR string" \
      --prio-ok
      myscript.sh PRIO

* case 'D'::

    epyunit \
      --ok-stdout="arbitrary signalling OK string" \
      --nok-stderr="arbitrary signalling ERROR string" \
      --exit-ok \
      myscript.sh EXITOK

* case 'E'::

    epyunit \
      --ok-stdout="arbitrary signalling OK string" \
      --nok-stderr="arbitrary signalling ERROR string" \
      --exit-nok \
      myscript.sh EXITNOK

* case 'F'::

    epyunit \
      --ok-stdout="arbitrary signalling NOK string" \
      --nok-stderr="arbitrary signalling ERROR string" \
      --exit=7 \
      myscript.sh EXIT7

* case 'G'::

    epyunit \
      --ok-stdout="arbitrary signalling OK string" \
      --nok-stderr="arbitrary signalling ERROR string" \
      --exit-ignore \
      --default-ok \
      myscript.sh


The complete source is contained in the module directory 'epyunit/myscript.sh'.

For detailed examples refer to the subdirectories of the source package for:

* `UseCases <UseCases.html>`_ 

* `tests <tests.html>`_ 


For examples of application within Eclipse refer to

* `Executable <epyunit_example_eclipse_executable.html>`_ 

* `Python API <epyunit_example_eclipse_python.html>`_ 

