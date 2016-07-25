Call Integration into PyUnit
****************************

The 'epyunit' package provides extensions for the 
PyUnit framework for the test of arbitrary executables.::

  The overall main reason to setup this project is the integration of
  lightweight unit tests for scripts with a GUI based on PyDev + Eclipse.

The call API of the tested components could be integrated
into the ePyUnit interface either by calling Python bindings, or by the 
the provided executable 'epyunit' from the command line.

The output evaluation of the called subprocess is based on one or more of:

* **stdout** - Arbitrary output written to stdout.

* **stderr** - Arbitrary output written to stderr.

* **exit code** - Exit code value.

The components collect internally the data from multiple 
streams for combined processing.
A few behaviour based options define the expected dominant values and
reduce in a fuzzy based approach multiple criteria to the relevant:

* prio-ok, prio-nok

* exit-ignore, exit-ok, exit-nok


Common Parameters
=================

The input data from the tesstee are collected from the the character based 
streams stdout and  stderr.
Character based streams are interpreted by lines, where each line is matched
seperately.
Multiple match strings could be provided by repetition of the match option.
When enhanced regular expression for match criteria  is required, the 
testee could either be defined as a piped group of shell scripts, or 
wrapped itself by a script for the normalization of it's output stream.
This provides for the full scope of individual applications of customized
regular expressions as filters e.g. by 'sed' and 'awk'. 
The additional exit code is a single value for each testee.

The input sources are provided by the following parameters:

* **stdout**

  Arbitrary output written to stdout could be checked
  for user provided strings. Multiple strings could be
  provided:

  * Match on success condition::

      --ok-stdout=<string>

  * Match on failure condition::

      --nok-stdout=<string>

* **stderr**

  Arbitrary output written to stderr could be checked
  for user provided strings. Multiple strings could be
  provided.

  * Match on success condition::

      --ok-stderr=<string>

  * Match on failure condition::

      --nok-stderr=<string>

* **exit code**

  Exit code value.
  The exit code of the testee is interpreted independently 
  and eventually superposes the previous.

  * Ignores the exit code::

      --exit-ignore

  * Match on success condition::

      --exit=<val>

  * Match on failure::

      --exit-nok

  * Exit value '0' indicates success::

      --exit-ok

The following options resolve ambiguity when success and failure conditions
are matched:

* The success conditions dominate, optional counter::

    --prio-ok[=#count-min]

* The failure conditions dominate, optional counter::

    --prio-nok[=#count-min]

  This is the default::

    --prio-nok[=0]

Examples
========

* `CLI: command line interface <epyunit_example_cli.html>`_ 

* `Eclipse: Executable within Eclipse IDE <epyunit_example_eclipse_executable.html>`_ 

* Detailed examples in the subdirectories of the source package:

  * tests + testdata 

  * UseCases

* `Python API <epyunit_example_eclipse_python.html>`_ 

References
==========

* Eclipse - `<www.eclipse.org>`_ 

* PyUnit - `<pyunit.sourceforge.net>`_ 

* ePyUnit - `<https://pypi.python.org/pypi/epyunit>`_ 

* PyFileSysObjects - `<https://pypi.python.org/pypi/pyfilesysobjects>`_ 

* PySourceInfo - `<https://pypi.python.org/pypi/pysourceinfo>`_ 


