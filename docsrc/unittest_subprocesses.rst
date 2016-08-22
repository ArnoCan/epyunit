Unittest for Subprocesses
*************************

The 'epyunit' package provides extensions for the 
PyUnit framework for the test of arbitrary executables.::

  The overall main reason to setup this project is the integration of
  lightweight blackbox unit tests for scripts with a GUI based on PyDev + Eclipse.

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

* priotype

* result, resultok, resultnok

The following exit criteria provide either for weighting the output, or
as criteria itself.

* exitign, exittype, exitval



Common Parameters
=================

The input data of the tesstee are collected from the the character based 
streams stdout and  stderr.
Character based streams are interpreted by lines by default, where each line is matched
seperately.
The behavipur could be adapted by 're' flags.
Multiple match strings could be provided by repetition of the match option.
When enhanced regular expression and functions for match criteria  are required, the 
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

      CLI: --stdoutok=(string-literal|regexpr) x N
      API: 'stdoutok': [ (string-literal|regexpr), ]

  * Match on failure condition::

      CLI: --stdoutnok=(string-literal|regexpr) x N
      API: 'stdoutnok': [ (string-literal|regexpr), ]

* **stderr**

  Arbitrary output written to stderr could be checked
  for user provided strings. Multiple strings could be
  provided.

  * Match on success condition::

      CLI: --stderrok=(string-literal|regexpr) x N
      API: 'stderrok' : [ (string-literal|regexpr), ]

  * Match on failure condition::

      CLI: --stderrnok=(string-literal|regexpr) x N
      API: 'stderrnok': [ (string-literal|regexpr), ]

* **exit code**

  Exit code value.
  The exit code of the testee is interpreted independently 
  and eventually superposes the previous.

  * Ignores the exit code::

      CLI: --exitign
      API: 'exitign': (True|False)

  * Match on success condition::

      CLI: --exitval=<value>
      API: 'exitval': <value>

  * Match on failure::

      CLI: --exittype=False
      API: 'exittype': False

  * Exit value '0' indicates success::

      CLI: --exittype=True
      API: 'exittype': True

The following options resolve ambiguity when success and failure conditions
are matched:

* The success conditions dominate::

    CLI: --priotype=True
    API: 'priotype': True

* The failure conditions dominate::

    CLI: --priotype=False
    API: 'priotype': False

Similar the following counters:

* The matches at all::

    CLI: --result=<int-value>
    API: 'result': <int-value>

* The number of success matches::

    CLI: --resultok=<int-value>
    API: 'resultok': <int-value>

* The number of failure matches::

    CLI: --resultnok=<int-value>
    API: 'resultnok': <int-value>

Examples
========

* `CLI: command line interface <epyunit_example_cli.html>`_ 

* `Eclipse: Executable within Eclipse IDE <epyunit_example_eclipse_executable.html>`_ 

* Detailed examples in the subdirectories of the source package:

  * `UseCases <UseCases.html>`_ 

  * `tests <tests.html>`_ 

References
==========

* Eclipse - `<www.eclipse.org>`_ 

* PyUnit - `<pyunit.sourceforge.net>`_ 

* ePyUnit - `<https://pypi.python.org/pypi/epyunit>`_ 

* PyFileSysObjects - `<https://pypi.python.org/pypi/pyfilesysobjects>`_ 

* PySourceInfo - `<https://pypi.python.org/pypi/pysourceinfo>`_ 


