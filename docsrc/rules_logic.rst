Test Syntax, Rules, and Correlation
===================================

The provided unit test environment by ePyUnit is designed as a simple add-on
for PyUnit, and/or PyDev+Eclipse.
Thus with a little efford the command line interface as well as an integrated
GUI plugin for Eclipse were utilized for genric blackbox tests.
Therefore the feature set is limited to the mandatory basics of blackbox tests 
with major reuse of PyUnit and PyDev.

The provided instrumentation of decisions on the resulting test state is provided 
as string tables with regular expressions to be matched on the output of testees.
This also includes the match on the resulting exit value of the called process.
Though only processes with output relibably representing the actual execution
state could be tested. When the testee provides indirect results only like 
log entries, a wrapper e.g. as a short bash-script could be applied.

The analysed results could be priorized and correlated by several parameters,
thus a lightweight fuzzy approach of data analysis is implemented for the 
test results.

The following figure depicts the main components of a subprocess test.
  ::

    +------------------+         +---------------------+         +---------------------+
    |                  |         |                     |         |                     |
    |  Python-Process  |  <--->  |  Python-Subprocess  |  <--->  |    Shell-Script     |  
    |                  |         |                     |         |                     |
    +------------------+         +---------------------+         +---------------------+
             A                              A                              A
             |                              |                              |
       data correlator               the actual testee                 a resource
       frame for tests                responding with                  triggering
                                        test output                    the testee


The tested subprocesses are viewed as blackboxes with output representing the
state of the last action.
Therefore the data correlator inspects the output of the testee only and combines
one or multiple sources into an overall state.

The Data Correlator - Status Decision
"""""""""""""""""""""""""""""""""""""

The following test case definition syntax is provided by the correlator engine for subprocesses.

  .. figure:: _static/syntax-flow.png
     :width: 500

* **SubprocessUnit, SystemCalls**

  See classes:

  * *epyunit.SystemCalls.SystemCalls*

  * *epyunit.SubprocUnit.SubprocessUnit*

  .
* **apply**

  Applies filters and the state decision engine for the final result 
  of the current testcase, this includes all responses, correlators, 
  and constraints.
  See classes:

  * *epyunit.SubprocUnit.SProcUnitRules*

  .
* **pritotype**

  The priotiry of matched resulttype which dominates.
  The default is ERROR, thus each error sets the overall state to failure.

* **coutres**

  The result counters, one total, and one for failure and one for success.
  When thresholds are defined, the counter is measured by the threshold, and
  sets the state only in case of a value beyond the thresholds.

* **filter**

  The content match for a testcase.
  This is either the literal content of the output as displayed strings, or the
  exit value.

* **exit**

  The type of match and/or the value to be matched. 

* **stdout**

  A set of regular expressions to be matched on the provided STDOUT text stream.

* **stderr**

  A set of regular expressions to be matched on the provided STDERR text stream.

* **countnok, countok**

  A regular expression consiting of one or more groups.

* **re.match**

  Attributes and flags for the match operations of regular expressions.
  these are actually dynamically precompiled with provided flags.


Testnorm and Reference Cases
""""""""""""""""""""""""""""

* **Shell-Script** - Responses of simulated result sets

  The following results are returned from the internal reference script 'myscript.sh'
  for the simulation of a testee.
  The realworld application has to define it's own result interface. 

  Each column represents one set of result data. Including the exit value, the STDOUT
  string, and the STDERR string. As already mentioned, this is a direct output
  example, others may involve a caller wrapper, which forwards indirect results 
  such as logfile or database entries.

  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | output type    | OK   | NOK | PRIO | EXITOK | EXITNOK | EXIT7 | EXIT8 | EXIT9OK3NOK2 | DEFAULT |
  +================+======+=====+======+========+=========+=======+=======+==============+=========+
  | exit-value     | 0    | 0   | 0    | 0      | 1       | 7     | 8     | 9            | 123     |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | stdout         | txt  | txt | txt  | txt    | txt     | txt   | txt   | txt          | txt     |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | stderr         | --   | txt | txt  | --     | --      | --    | txt   | txt          | --      |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+

  The generic format of the response set EXIT9OK3NOK2 used in a number of generic tests
  for the state decision engine is:
    ::

      EXIT:      9
      STDOUT:    OK
                 OK
                 OK
      STDERR:    NOK
                 NOK

  For further detauils refer to 'myscript.sh'`[source] <myscript-sh.html>`_
  .
Exit values
"""""""""""
* **exit values**: Result of flags on the input type of exit values

  The controlling flags for the resulting exit states are:

  * exitign - ignore exit values, for output stream only

  * exittype - define success on exit==0, or else

  * exitval - define success for a specific exit value only

  The following results are returned for specific exit values as input into
  the wrapper 'epyunit'. Each column represents some resulting states 
  for a specific reference data set dependent on the applied rule/option.
  The resulting values are based on the exit value only.

  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | rule/option    | OK   | NOK | PRIO | EXITOK | EXITNOK | EXIT7 | EXIT8 | EXIT9OK3NOK2 | DEFAULT |
  +================+======+=====+======+========+=========+=======+=======+==============+=========+
  | exitign=True   | 0    | 0   | 0    | 0      | 0       | 0     | 0     | 0            | 0       |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | exittype=False | 1    | 1   | 1    | 1      | 0       | 0     | 0     | 0            | 0       |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | exittype=True  | 0    | 0   | 0    | 0      | 1       | 1     | 1     | 1            | 1       |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | exitval=0      | 0    | 0   | 0    | 0      | 1       | 1     | 1     | 1            | 1       |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | exitval=1      | 1    | 1   | 1    | 1      | 0       | 1     | 1     | 1            | 1       |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | exitval=7      | 1    | 1   | 1    | 1      | 1       | 0     | 1     | 1            | 1       |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | exitval=8      | 1    | 1   | 1    | 1      | 1       | 1     | 0     | 1            | 1       |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | exitval=9      | 1    | 1   | 1    | 1      | 1       | 1     | 1     | 0            | 1       |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | exitval=123    | 1    | 1   | 1    | 1      | 1       | 1     | 1     | 1            | 0       |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+

  .

Output Streams
""""""""""""""

* **stdout and stderr**: Flags for output values

  The standard out and err streams are handled technically similarly. The difference
  is the semantics as either an 'error-stream', or more or less as a 'success-stream'.
  Technically a set of match-rules is provided by the caller, which are evaluated on 
  the input data until a match occurs. In case of multiple rules each is matched in
  order to correctly detect required macth counts.

  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | rule/option    | OK   | NOK | PRIO | EXITOK | EXITNOK | EXIT7 | EXIT8 | EXIT9OK3NOK2 | DEFAULT |
  +================+======+=====+======+========+=========+=======+=======+==============+=========+
  | stdoutok       | 0    | 0   | 0    | 0      | 1       | 1     | 1     | 1            | 1       |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | stdoutnok      | 0    | 0   | 0    | 0      | 1       | 1     | 1     | 1            | 1       |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | stderrok       | 0    | 0   | 0    | 0      | 1       | 1     | 1     | 1            | 1       |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | stderrnok      | 0    | 0   | 0    | 0      | 1       | 1     | 1     | 1            | 1       |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+


  The match behaviour of the 're' module could be influenced by some flags which are 
  represented as:

  * debug - *re.DEBUG*

  * dotall - *re.DOTALL*

  * ignorecase - *re.IGNORECASE*

  * multiline - *re.MULTILINE*

  * unicode - *re.UNICODE*

  .

Resolution of Fuzzy Results
"""""""""""""""""""""""""""
* **priorities for ambiguity**: Flags - mixed on exit and output values

  The priotype defines the dominant type in case of ambuigity.
  This is for example the case, when OK and NOK matches occur on the output streams
  of the testee.
  In those cases a simple definition of the dominant priotype results in a unique
  result.

  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | rule/option    | OK   | NOK | PRIO | EXITOK | EXITNOK | EXIT7 | EXIT8 | EXIT9OK3NOK2 | DEFAULT |
  +================+======+=====+======+========+=========+=======+=======+==============+=========+
  | priotype = OK  | 0    | 0   | 0    | 0      | 1       | 1     | 1     | 1            | 1       |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | priotype = NOK | 0    | 1   | 1    | 0      | 1       | 1     | 1     | 1            | 1       |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+

  .
* **counter values**: Counter for success and failure matches

  The counter values provide also a means for the resolution of ambiguity,
  but also for required multiple occurances of specific regular expressions.
  The provided counters are:

  * result
  * resultnok
  * resultok

