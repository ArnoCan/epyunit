
'epyunit' - Call Integration into PyUnit and PyDev
**************************************************

The 'epyunit' package provides extensions of the 
PyUnit framework based on library modules for Python. 
The call API of the tested components could be integrated
into PyUnit either by calling Python bindings, or by the 
the provided executable 'epyunit' for the command line 
interface and script automation.

The test components collect internally the data from multiple 
output streams for combined interpretation.
The final decision on the state of the current test case is 
based on the selected interpretation criteria.
The options therefore comprise output content related scan options, 
and additional weight options, defining priorities for the combination
of the partial result.


Syntax Elements
===============

The provided options for the basic test output evaluation of the called 
process are based on one or more of the following input sources. 
These comprise in current version the character based streams stdout and stderr, 
which could deliver multiple match criteria, whereas the exit code is a 
single value for each testee by definition.

Character based streams are interpreted by lines, where each line is matched seperately.
Multiple match strings could be provided by repetition of the match option.
When enhanced regular expression matchin is required, the testee could either be defined
as a piped group of shell scripts, or wrapped itself by a script for normalization of it's
output stream.
This provides for the full scope of individual application of regular expressions e.g.
by 'sed' and 'awk'. 


* **stdout**

  Arbitrary output written to stdout could be checked
  for user provided strings. 

  The provided options are:

  * --ok-stdout=<string>

    Match defines a success condition.

  * --nok-stdout=<string>

    Match defines a failure condition.

* **stderr**

  Arbitrary output written to stderr could be checked
  for user provided strings. Multiple strings could be
  provided.

  The provided options are:

  * --ok-stderr=<string>

    Match defines a success condition.

  * --nok-stderr=<string>

    Match defines a failure condition.

* **exit code**

  Exit code value.

  * --exit=<val>

    Match defines a success condition.

  * --exit-nok

    Exit value '!=0' indicates success.

  * --exit-ok

    Exit value '0' indicates success.



The following options resolve ambiguity when multiple criteria are matched:

* prio-ok

  In case of present failure and success conditions,
  the success condition dominates.

* prio-nok

  In case of present failure and success conditions,
  the failure condition dominates.
  
  This is the default.

Independently the exit coded of the testee is interpreted and eventually
superposes the previous due to one of following options.

* exit-ignore

  Ignores the exit code.

* exit-value=<value>

  Matches the exit code for success criteria.
  When present defines OK.

* exit-ok

  Requires OK(0) for the previous to be valid.
  Else superposes the overall result to failure.

* exit-nok

  Requires NOK(!=0) for the previous to be valid.
  Else superposes the overall result to failure.


Examples
========

Call examples are:

* `CLI: command line interface <epyunit_example_cli.html>`_ 

* Eclipse: PyDev integration by call of:

  * `Executable <epyunit_example_eclipse_executable.html>`_ 

  * `Python API <epyunit_example_eclipse_python.html>`_ 
