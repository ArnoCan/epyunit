epyunit - Test Syntax, Rules, and Correlation
=============================================

The provided unit test environment by ePyUnit is designed as a simple add-on
for PyUnit, and/or PyDev+Eclipse.
Thus a command line interface as well as an integrated
GUI plugin for Eclipse are provided.

The provided syntax for analysing the test ouput is described in the following chapter.
The analysed results could be priorized and correlated by several parameters,
thus a lightweight fuzzy approach of data analysis is implemented for the 
test results.

* **Single level subprocesses**

  The following figure depicts the main components of a simple subprocess test
  by UseCases and testCases.
  This comprises a caller, either the binariy 'epyunit', or the library module
  'SubprocUnit', and a subprocess as testee.
  The script 'myscript.sh' is used as testee with defined responses.
  These tests are performed for the library itself and could be find
  in the source package 'tests/30_libs'.
    ::

                                                                          --------------
                                     +---------------------+            /                \
      +------------------+         +-+-------------------+ |          ----------------    |
      |                  |         |                     | |        /                  \ /
      |  Python-Process  |  <--->  |      Subprocess     | |------ |      Resource      |  
      |                  |         |                     |-+        \                  /
      +------------------+         +---------------------+            ----------------
               A                              A                              A
               |                              |                              |
         The test wrapper             The actual testee                 Resources
       executing the testee            responding with                  triggering
       CLI:    epyunit                   test output                    the testee
       Python: SubprocessUnit                                        for tests of epyunit
                                                                     itself 'myscript.sh'

* **Nested subprocesses**

  Another slightly more complex scenario is given when the command line interface 'epyunit'
  is called as a wrapper from within a python program.
  These tests are performed for the 'epyunit' executable itself and could be find
  in the source package 'tests/60_bins'.
    ::

                                                                         -----
                                                  +-----------+        /       \
      +----------------+      +---------+      +------------+ |      -------    |
      |                |      |         |      |            | |     /         \ /
      | Python-Process | <--> | epyunit | <--> | Subprocess | | -- |  Resource |  
      |                |      |         |      |            |-+     \         /
      +----------------+      +---------+      +------------+         -------
              A                    A                 A                   A
              |                    |                 |                   |
           Test call          test wrapper     actual testee         Resources


The Data Correlator - Status Decision
"""""""""""""""""""""""""""""""""""""
Subprocesses are treated as blackboxes with output representing the state.
Therefore the data correlator inspects the output of the testee only and combines
one or multiple sources into an overall state.

The following test case definition syntax is provided by the correlator engine for subprocesses
'epyunit.SubprocUnit'
`[API] <epyunit.html#class-sprocunitrules>`_ 
`[source] <_modules/epyunit/SubprocUnit.html#SProcUnitRules>`_ 
.

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

  Defines the priority of the dominating resulttype.
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


Test Norm and Reference Cases
"""""""""""""""""""""""""""""
The 'ePyUnit' package contains the script '`myscript.sh <myscript-sh.html>`_ ' for the siumulation of subprocess
responses as examples and test results, located in the package directory.
The following results are returned for the simulation of a testee.
Each column represents one set of result data. Including the exit value, the STDOUT
string, and the STDERR string. 

  +----------------+------+-----+------+--------+---------+-------+-------+--------------+-----------+---------+
  | output type    | OK   | NOK | PRIO | EXITOK | EXITNOK | EXIT7 | EXIT8 | EXIT9OK3NOK2 | STDERONLY | DEFAULT |
  +================+======+=====+======+========+=========+=======+=======+==============+===========+=========+
  | exit-value     | 0    | 0   | 0    | 0      | 1       | 7     | 8     | 9            | 0         | 123     |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+-----------+---------+
  | stdout         | txt  | txt | txt  | txt    | txt     | txt   | txt   | txt          | --        | txt     |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+-----------+---------+
  | stderr         | --   | txt | txt  | --     | --      | --    | txt   | txt          | txt       | --      |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+-----------+---------+

The generic format e.g. of the response set 'EXIT9OK3NOK2' used in a number of generic tests
for the state decision engine is:
  ::

   > # call of the TNR script
   > myscript.sh EXIT9OK3NOK2
   fromH
   OK
   OK
   OK
   NOK
   NOK
   > echo $?
   9

The resulting semantics on the standard output channels is:
  ::

    EXIT:      9
    STDOUT:    OK
               OK
               OK
    STDERR:    NOK
               NOK

The output protocol is defined in various formats for further processing.


Exit values
"""""""""""

The exit values of subprocesses represent mostly their execution state.
These could be interpreted in various ways, which is defined by the flags:

* **exitign** 

  Ignore exit values, if filter defined check output stream.
  Results in the values:

  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | rule/option    | OK   | NOK | PRIO | EXITOK | EXITNOK | EXIT7 | EXIT8 | EXIT9OK3NOK2 | DEFAULT |
  +================+======+=====+======+========+=========+=======+=======+==============+=========+
  | exitign=True   | 0    | 0   | 0    | 0      | 0       | 0     | 0     | 0            | 0       |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+

  .

* **exittype**

  Defines success on exit category.

    True:  exit==0

    False: exit!=0

  Resulting in the values:

  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | rule/option    | OK   | NOK | PRIO | EXITOK | EXITNOK | EXIT7 | EXIT8 | EXIT9OK3NOK2 | DEFAULT |
  +================+======+=====+======+========+=========+=======+=======+==============+=========+
  | exittype=False | 1    | 1   | 1    | 1      | 0       | 0     | 0     | 0            | 0       |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | exittype=True  | 0    | 0   | 0    | 0      | 1       | 1     | 1     | 1            | 1       |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+

  .

* **exitval**

  Defines success for a specific exit value only, resulting on the values:

  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
  | rule/option    | OK   | NOK | PRIO | EXITOK | EXITNOK | EXIT7 | EXIT8 | EXIT9OK3NOK2 | DEFAULT |
  +================+======+=====+======+========+=========+=======+=======+==============+=========+
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

  The controlling pattern for the resulting states  by string match are:

  * **stdoutok** - list of 're' pattern indicating a success state from STDOUT

  * **stdoutnok** - list of 're' pattern indicating a failure state from STDOUT

  * **stderrok** - list of 're' pattern indicating a success state from STDERR

  * **stderrnok** - list of 're' pattern indicating a failure state from STDERR

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

  * redebug - *re.DEBUG*

  * redotall - *re.DOTALL*

  * reignorecase - *re.IGNORECASE*

  * remultiline - *re.MULTILINE*

  * reunicode - *re.UNICODE*

  .

Resolution of Fuzzy Results
"""""""""""""""""""""""""""
* **priorities for ambiguity**: Flags - mixed on exit and output values

  The priotype defines the dominant type in case of ambuigity.
  This is for example the case, when OK and NOK matches occur on the output streams
  of the testee.
  In those cases a simple definition of the dominant priotype results in a unique
  result.
  The 'priotype' could be seen as a joker, which dominates all others.

  * defaults:

    Result in the output:

    +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
    | rule/option    | OK   | NOK | PRIO | EXITOK | EXITNOK | EXIT7 | EXIT8 | EXIT9OK3NOK2 | DEFAULT |
    +================+======+=====+======+========+=========+=======+=======+==============+=========+
    | priotype = OK  | 0    | 0   | 0    | 0      | 1       | 1     | 1     | 1            | 1       |
    +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
    | priotype = NOK | 1    | 0   | 0    | 0      | 1       | 1     | 1     | 1            | 1       |
    +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+

  .

  * exittype:
    ::

       --exittype=False

    Inverts the semantics of 'exit'.
    Results in the output:

    +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
    | rule/option    | OK   | NOK | PRIO | EXITOK | EXITNOK | EXIT7 | EXIT8 | EXIT9OK3NOK2 | DEFAULT |
    +================+======+=====+======+========+=========+=======+=======+==============+=========+
    | priotype = OK  | 1    | 1   | 1    | 1      | 0       | 0     | 0     | 0            | 0       |
    +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
    | priotype = NOK | 1    | 1   | 1    | 1      | 0       | 0     | 0     | 0            | 0       |
    +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+

  .

  * stderrnok:
    ::

       --stderrnok='.+'

    Scans the STDERR output, sets the partial state to failure when a 're.match()' occurs.
    Results in the output:

    +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
    | rule/option    | OK   | NOK | PRIO | EXITOK | EXITNOK | EXIT7 | EXIT8 | EXIT9OK3NOK2 | DEFAULT |
    +================+======+=====+======+========+=========+=======+=======+==============+=========+
    | priotype = OK  | 0    | 0   | 0    | 0      | 1       | 1     | 1     | 1            | 1       |
    +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
    | priotype = NOK | 0    | 1   | 1    | 0      | 1       | 1     | 1     | 1            | 1       |
    +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+

    With additional flag:
    ::

       --stderrnok='.+'
       --ignoreexit=True


    +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
    | rule/option    | OK   | NOK | PRIO | EXITOK | EXITNOK | EXIT7 | EXIT8 | EXIT9OK3NOK2 | DEFAULT |
    +================+======+=====+======+========+=========+=======+=======+==============+=========+
    | priotype = OK  | 0    | 1   | 1    | 0      | 0       | 0     | 1     | 1            | 0       |
    +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
    | priotype = NOK | 0    | 1   | 1    | 0      | 0       | 0     | 1     | 1            | 0       |
    +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+

  .

  * stderrok:
    ::

       --stderrok='.+'

    Scans the STDER output, sets the partial state to success when a 're.match()' occurs.
    Results in the output:

    +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
    | rule/option    | OK   | NOK | PRIO | EXITOK | EXITNOK | EXIT7 | EXIT8 | EXIT9OK3NOK2 | DEFAULT |
    +================+======+=====+======+========+=========+=======+=======+==============+=========+
    | priotype = OK  | 0    | 0   | 0    | 0      | 1       | 1     | 1     | 1            | 1       |
    +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
    | priotype = NOK | 0    | 0   | 0    | 0      | 1       | 1     | 1     | 1            | 1       |
    +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+

    With additional flag:
    ::

       --stderrok='.+'
       --ignoreexit=True


    +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
    | rule/option    | OK   | NOK | PRIO | EXITOK | EXITNOK | EXIT7 | EXIT8 | EXIT9OK3NOK2 | DEFAULT |
    +================+======+=====+======+========+=========+=======+=======+==============+=========+
    | priotype = OK  | 1    | 0   | 0    | 1      | 1       | 1     | 0     | 0            | 1       |
    +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
    | priotype = NOK | 1    | 0   | 0    | 1      | 1       | 1     | 0     | 0            | 1       |
    +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+

  .

* **counter values**: Counter for success and failure matches

  The counter values provide also a means for the resolution of ambiguity,
  but also for required multiple occurances of specific regular expressions.
  The provided counters are:

  * result
  * resultnok
  * resultok

Output Formats for Postprocessing
"""""""""""""""""""""""""""""""""
The following output formats are available in current version.

* **csv**: Records with the hard-coded FS=';'

* **pass**: Pass STDOUT and STDERR transparently, set wrapper execution state as exit code.

* **passall**: Pass STDOUT, STDERR, and exit code  transparently.

* **raw**: Saem as passall.

* **repr**: Python 'repr' format.

* **str**: Python 'str' format.

* **xml**: XML format
