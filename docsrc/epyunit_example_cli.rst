Command line call examples
==========================

A call example of the the command line interface, 
for syntax details refer to the call wrapper
`epyunit <epyunit_cli.html>`_ .

The test executable is a simple shell script named
'myscript.sh' demonstrating some of the major cases. 
The indication supported by this simulated blackbox 
here consists of 'signalling' strings, exit values, 
and none of them as the user defined default case:
::

  #
  # NAME:      myscript.sh
  # PROJECT:   epyunit
  # WWW:       https://pypi.python.org/pypi/epyunit/
  # DOCS:      https://pythonhosted.org/epyunit/
  # VERSION:   01.01.001
  # AUTHOR:    Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez
  # COPYRIGHT: Copyright (C) 2015,2016 Arno-Can Uestuensoez
  # LICENSE:   Artistic-License-2.0 + Forced-Fairplay-Constraints
  #
  # DESCRIPTION: Test dummy for the selftest option of epyunit. 
  #

  # A: succeed
  if test "X$1" == "XOK";then
    echo arbitrary output
    echo arbitrary signalling OK string
    echo arbitrary output

  # B: fail
  elif test "X$1" == "XNOK";then
    echo arbitrary output
    echo arbitrary signalling ERROR string >&2
    echo arbitrary output

  # C: redundancy resolved by user defined priority
  elif test "X$1" == "XPRIO";then
    echo arbitrary output
    echo arbitrary signalling OK string
    echo arbitrary signalling ERROR string >&2
    echo arbitrary output

  # D: exit value
  elif test "X$1" == "XEXITOK";then
    echo arbitrary output
    echo arbitrary signalling OK string
    echo arbitrary output
    exit 0

  # E: exit value
  elif test "X$1" == "XEXITNOK";then
    echo arbitrary output
    echo arbitrary signalling OK string
    echo arbitrary output
    exit 1

  # F: exit value
  elif test "X$1" == "XEXIT7";then
    echo arbitrary output
    echo arbitrary signalling NOK string
    echo arbitrary output
    exit 7    

  # G: exit value
  elif test "X$1" == "XEXIT8";then
    echo arbitrary output
    echo arbitrary signalling NOK string
    echo arbitrary output
    echo arbitrary err output >&2
    echo arbitrary err signalling NOK string >&2
    echo arbitrary err output >&2
    exit 8

  # DEFAULT: define: here succeed '--default-ok'
  else
    echo arbitrary output
    exit 123

  fi

For the complete code refer to contained 'myscript.sh'.

The commandline wrapper call for case 'A' is 
::

  epyunit \
    --ok-stdout="arbitrary signalling OK string" \
    myscript.sh OK

The commandline wrapper call for case 'B' is 
::

  epyunit \
    --nok-stderr="arbitrary signalling ERROR string" \
    myscript.sh NOK

The commandline wrapper call for case 'C' is 
::

  epyunit \
    --ok-stdout="arbitrary signalling OK string" \
    --nok-stderr="arbitrary signalling ERROR string" \
    --prio-ok
    myscript.sh PRIO

The commandline wrapper call for case 'D' is 
::

  epyunit \
    --ok-stdout="arbitrary signalling OK string" \
    --nok-stderr="arbitrary signalling ERROR string" \
    --exit-ok \
    myscript.sh EXITOK

The commandline wrapper call for case 'E' is 
::

  epyunit \
    --ok-stdout="arbitrary signalling OK string" \
    --nok-stderr="arbitrary signalling ERROR string" \
    --exit-nok \
    myscript.sh EXITNOK

The commandline wrapper call for case 'F' is 
::

  epyunit \
    --ok-stdout="arbitrary signalling NOK string" \
    --nok-stderr="arbitrary signalling ERROR string" \
    --exit=7 \
    myscript.sh EXIT7

The commandline wrapper call for case 'DEFAULT' is 
::

  epyunit \
    --ok-stdout="arbitrary signalling OK string" \
    --nok-stderr="arbitrary signalling ERROR string" \
    --exit-ignore \
    --default-ok \
    myscript.sh


The complete source is contained in the module directory 'epyunit/myscript.sh'.

For detailed examples refer to the subdirectories of the source package for:

* Unit tests 

* UseCases


For examples of application within Eclipse refer to

* `Executable <epyunit_example_eclipse_executable.html>`_ 

* `Python API <epyunit_example_eclipse_python.html>`_ 

