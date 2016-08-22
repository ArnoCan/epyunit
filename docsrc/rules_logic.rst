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


* **Adapters** - for Arbitrary Resources

  The epyunit package provides the unit test of an arbitrary subprocess by gathering the data
  provides at the interfaces exit-code, STDIN, and STDERR. In case arbitrary non-compliant resources
  are executed and have to be used as input source, an arbitrary mediation adapter could be used 
  in order to transform the results into the epyunit interface.

  For example a database adapter with access by SQL may transform the data into an appropriate
  response for the epyunit input gathering API. 
    ::

                                                                         -----
                                                  +-----------+        /       \
      +----------------+      +---------+      +------------+ |      -------    |
      |                |      |         |      |            | |     /         \ /
      | Python-Process | <--> | epyunit | <--> |  adapter   | | -- |  Resource |  
      |                |      |         |      |            |-+     \         /
      +----------------+      +---------+      +------------+         -------
              A                    A                 A                   A
              |                    |                 |                   |
           Test call          test wrapper   mediation adapter       Conformant and
                                               intermixed with       non/conformant
                                                  testees              Resources

The Data Correlator - Overall Status Decision
"""""""""""""""""""""""""""""""""""""""""""""
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

  Starts an arbitrary executable with options by standard package 'subprocess' in cli-mode,
  and collects the response data. 

  See classes:

  * *epyunit.SystemCalls.SystemCalls* 
    `[doc] <epyunit.html#class-systemcalls>`_
    `[source] <_modules/epyunit/SystemCalls.html#SystemCalls>`_

  * *epyunit.SubprocUnit.SubprocessUnit* 
    `[doc] <epyunit.html#class-subprocessunit>`_
    `[source] <_modules/epyunit/SubprocUnit.html#SubprocessUnit>`_

  .
* **apply**

  Applies filters and the state decision engine for the final result 
  of the current testcase, this includes all responses, correlators, 
  and constraints.
  The 'apply' function is applied on the final result as gathered by
  the 'SystemCall' function block. This includes the resulting exit code,
  the complete set of response lines from STDIN and from STDERR.  
  The actual actions performed on the result by the state decision engine  
  depend on the choosen rules and provided parameters.
  When required the standard class could be extended and/or replaced
  by custom classes.

  See classes:

  * *epyunit.SubprocUnit.SubprocessUnit* 
    `[doc] <epyunit.html#class-sprocunitrules>`_
    `[source] <_modules/epyunit/SubprocUnit.html#SProcUnitRules>`_

  .
* **pritotype**

  The functional block 'priotype' performs the final decision for the overall
  state by applying a priority scheme onto the resulting state assembly.
  If for example 2 success idicators and 3 failure indicators are gathered
  by default the failure dominates the result. The same occurs by default 
  when 3 success idicators and 1 failure indicators are gathered due to
  the default 'priotype:=NOK'. This defines the error condition as critical
  and sets the overall state of the test to failed.
  This behaviour could be inverted to success, where any success will dominate 
  an arbitrary number of errors, or to a weight factor for balancing between
  the occurances of success and failure indications.

  The option defines finally the priority of the dominating resulttype.
  The default is ERROR, thus each error sets the overall state to failure.

  * priotype:=False - **hasFailure**:
    Any failure dominates.

  * priotype:=True - **hasSuccess**:
    Any success dominates.

  * priotype:=WEIGHT - **weight**:
    Count criteria, the bigger value wins. 

  * priotype:=fctcallback - **custom**:
    The application of a custom state machine could be enabled either by inheritance,
    or by the provided custom callback. The callback is called within the 'apply' method
    for final state decision replacing the internal 'priotype' based final priority rules.
    The pointer to a weight function has to comply to the following signature. 
    ::

      fctcallback(ruleobject,data)

      Args:
        ruleobject: The ruleobject.

        data: The data from subprocess.

      Returns:
	    State, 'True' or 'False'. The result is
        forwarded by the method 'apply'.

	  Raises:
        Passes through.
  .
* **countres**

  The result counters, one total, and one for failure and one for success.
  These are internally incremented for each indication, but evaluated in case of
  present thresholds, or requested priority type 'weight'. 
  When thresholds are defined, the counter is measured by the threshold, and
  sets the state only in case of a value beyond the thresholds. When both are 
  defined the condition is combined by AND.

  * **result**: Success when the threshold is matched.

  * **resultok**: Counter for indicated success increments.
    Resulting in success when the threshold is matched.

  * **resultnok**: Counter for indicated failure increments.
    Resulting in failure when the threshold is matched.

  .
* **filter**

  The content match for a testcase on the reply by the testee to STDOUT, STDERR,
  or exit.
  This is either the match on content by regular expressions based on 're' or 
  by provided literal strings with the additional match on the exit value.
  The matched strings are collected and increment each a counter for later 
  processing.

  The filter is called repetitvely on each line within the 'apply' method.
  Thus it produces a list of matches in case multiple are present.
 
  .
* **exit**

  The type of match and/or the value to be matched. 

* **stdout**

  A set of regular expressions to be matched on the provided STDOUT text stream.
  The strings are matched when the filter is processed.
  The matched strings are collected and the indication is counted. 

  * **stdoutok**: A match indicates success and increments the weight of success
    by one.

  * **stdoutnok**: A match indicates failure and increments the weight of failure
    by one.

  .
* **stderr**

  A set of regular expressions to be matched on the provided STDERR text stream.
  The strings are matched when the filter is processed.
  The matched strings are collected and the indication is counted. 

  * **stderrok**: A match indicates success and increments the weight of success
    by one.

  * **stderrnok**: A match indicates failure and increments the weight of failure
    by one.

* **countnok, countok**

  A regular expression consiting of one or more groups which updates the match counters.

* **re.match**

  Attributes and flags for the match operations of regular expressions.
  these are actually dynamically precompiled with provided flags.


Test Norm and Reference Cases
"""""""""""""""""""""""""""""
The 'ePyUnit' package contains in the current version the scripts

* '`epyunit/myscript.sh <myscript-sh.html>`_ ' 
* '`epyunit/myscript.py <myscript-py.html>`_ ' 

for the siumulation of subprocess
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

  For examples refer to the test subpackage
  'epyunit.epyunit.myscript' `[test-sources] <myscript-py.html#>`_:

  * OK `[test-sources] <myscript-py.html#call-a-ok>`_
  * NOK `[test-sources] <myscript-py.html#call-b-nok>`_
  * PRIO `[test-sources] <myscript-py.html#call-c-prio>`_
  * EXITOK `[test-sources] <myscript-py.html#call-d-exitok>`_
  * EXITNOK `[test-sources] <myscript-py.html#call-e-exitnok>`_
  * EXIT7 `[test-sources] <myscript-py.html#call-f-exit7>`_
  * EXIT8 `[test-sources] <myscript-py.html#call-g-exit8>`_
  * EXIT9OK3NOK2 `[test-sources] <myscript-py.html#call-h-exit9ok3nok2>`_
  * STDERONLY `[test-sources] <myscript-py.html#call-i-stderronly>`_
  * DEFAULT `[test-sources] <myscript-py.html#call-default>`_

  .


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

  For examples refer to the test subpackage:

  * tests.libs.SubprocessUnitCalls.callit.exit.exitign `[test-sources] <tests.libs.SubprocessUnitCalls.callit.exit.exitign.html>`_

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

  For examples refer to the test subpackage:

  * exittype=False:
    tests.libs.SubprocessUnitCalls.callit.exit.exittype.True `[test-sources] <tests.libs.SubprocessUnitCalls.callit.exit.exittype.True.html>`_

  * exittype=True:
    tests.libs.SubprocessUnitCalls.callit.exit.exittype.False `[test-sources] <tests.libs.SubprocessUnitCalls.callit.exit.exittype.False.html>`_

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

  For examples refer to the test subpackage:

  * exitval=0:
    tests.libs.SubprocessUnitCalls.callit.exit.exitval.exitval_0 
    `[test-sources] <tests.libs.SubprocessUnitCalls.callit.exit.exitval.exitval_0.html>`_

  * exitval=1:
    tests.libs.SubprocessUnitCalls.callit.exit.exitval.exitval_1 
    `[test-sources] <tests.libs.SubprocessUnitCalls.callit.exit.exitval.exitval_1.html>`_

  * exitval=7:
    tests.libs.SubprocessUnitCalls.callit.exit.exitval.exitval_7 
    `[test-sources] <tests.libs.SubprocessUnitCalls.callit.exit.exitval.exitval_7.html>`_

  * exitval=8:
    tests.libs.SubprocessUnitCalls.callit.exit.exitval.exitval_8 
    `[test-sources] <tests.libs.SubprocessUnitCalls.callit.exit.exitval.exitval_8.html>`_

  * exitval=9:
    tests.libs.SubprocessUnitCalls.callit.exit.exitval.exitval_9 
    `[test-sources] <tests.libs.SubprocessUnitCalls.callit.exit.exitval.exitval_9.html>`_

  * exitval=123:
    tests.libs.SubprocessUnitCalls.callit.exit.exitval.exitval_123 
    `[test-sources] <tests.libs.SubprocessUnitCalls.callit.exit.exitval.exitval_123.html>`_

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
  | stderrnok      | 0    | 1   | 1    | 0      | 1       | 1     | 1     | 1            | 1       |
  +----------------+------+-----+------+--------+---------+-------+-------+--------------+---------+


  The match behaviour of the 're' module could be influenced by some flags which are 
  represented as:

  * redebug - *re.DEBUG*

  * redotall - *re.DOTALL*

  * reignorecase - *re.IGNORECASE*

  * remultiline - *re.MULTILINE*

  * reunicode - *re.UNICODE*

  For examples refer to the test subpackage:

  * stdoutok:
    tests.libs.SubprocessUnitCalls.callit.streams.stdoutok 
    `[test-sources] <tests.libs.SubprocessUnitCalls.callit.streams.stdoutok.html>`_

  * stdoutnok:
    tests.libs.SubprocessUnitCalls.callit.streams.stdoutnok 
    `[test-sources] <tests.libs.SubprocessUnitCalls.callit.streams.stdoutnok.html>`_

  * stderrok:
    tests.libs.SubprocessUnitCalls.callit.streams.stderrok 
    `[test-sources] <tests.libs.SubprocessUnitCalls.callit.streams.stderrok.html>`_

  * stderrnok:
    tests.libs.SubprocessUnitCalls.callit.streams.stderrnok 
    `[test-sources] <tests.libs.SubprocessUnitCalls.callit.streams.stderrnok.html>`_
  .

Resolution of Fuzzy Results
"""""""""""""""""""""""""""
The epyunit package handles in particular unit tests on arbitrary executables.
The executables frequently frequently do have ambigious states when several actions are
involved, thus the result may present a number of success as well as a number of failure
indicators.
The epyunit package implements customizable state machine for defining the resulting
overall execution state. This is based on fuzzy matching and locking onto execution results
by rule chains.
The provided default rules are here evaluated in accordance to the choosen parameters and
decide by priorities and counter values and weights the overall excution state.  
The basic apporach here is finally similar to fuzzy logic based algorithms.
The state decision classes including 
`epyunit.SubprocUnit.SProcUnitRules <epyunit.html#class-sprocunitrules>`_
could be extended and/or replaced as required. 

The following depicted commandline options could be transformed to the API as well, to which 
these are mapped as key arguments, thus these are exchangeable.

* **priorities for ambiguity**: Flags - mixed on exit and output values

  The priotype defines the dominant type in case of ambuigity.
  This is for example the case, when OK and NOK matches occur on the output streams
  of the testee.
  In those cases a simple definition of the dominant priotype results in a unique
  result.
  The 'priotype' could be seen as a joker, which dominates all others.

  * defaults:

    Result in the output:

    +------------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
    | rule/option      | OK   | NOK | PRIO | EXITOK | EXITNOK | EXIT7 | EXIT8 | EXIT9OK3NOK2 | DEFAULT |
    +==================+======+=====+======+========+=========+=======+=======+==============+=========+
    | priotype = True  | 0    | 0   | 0    | 0      | 1       | 1     | 1     | 1            | 1       |
    +------------------+------+-----+------+--------+---------+-------+-------+--------------+---------+
    | priotype = False | 1    | 0   | 0    | 0      | 1       | 1     | 1     | 1            | 1       |
    +------------------+------+-----+------+--------+---------+-------+-------+--------------+---------+

    For examples refer to the test subpackage:

    * priotype=False:
      tests.libs.SubprocessUnitCalls.callit.priotype.NOK.defaults `[test-sources] <tests.libs.SubprocessUnitCalls.callit.priotype.NOK.defaults.html>`_

    * priotype=True:
      tests.libs.SubprocessUnitCalls.callit.priotype.OK.defaults `[test-sources] <tests.libs.SubprocessUnitCalls.callit.priotype.OK.defaults.html>`_

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

    For examples refer to the test subpackage:

    * priotype=True:
      tests.libs.SubprocessUnitCalls.callit.priotype.NOK.exittype.False `[test-sources] <tests.libs.SubprocessUnitCalls.callit.priotype.NOK.exittype.False.html>`_

    * priotype=True:
      tests.libs.SubprocessUnitCalls.callit.priotype.OK.exittype.False `[test-sources] <tests.libs.SubprocessUnitCalls.callit.priotype.OK.exittype.False.html>`_
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

    For examples refer to the test subpackage:

    * priotype=True:
      tests.libs.SubprocessUnitCalls.callit.priotype.NOK.stderrnok.defaults `[test-sources] <tests.libs.SubprocessUnitCalls.callit.priotype.NOK.stderrnok.defaults.html>`_

    * priotype=True:
      tests.libs.SubprocessUnitCalls.callit.priotype.OK.stderrnok.defaults `[test-sources] <tests.libs.SubprocessUnitCalls.callit.priotype.OK.stderrnok.defaults.html>`_

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

    For examples refer to the test subpackage:

    * priotype=True:
      tests.libs.SubprocessUnitCalls.callit.priotype.NOK.stderrnok.exitign `[test-sources] <tests.libs.SubprocessUnitCalls.callit.priotype.NOK.stderrnok.exitign.html>`_

    * priotype=True:
      tests.libs.SubprocessUnitCalls.callit.priotype.OK.stderrnok.exitign `[test-sources] <tests.libs.SubprocessUnitCalls.callit.priotype.OK.stderrnok.exitign.html>`_

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

    For examples refer to the test subpackage:

    * priotype=True:
      tests.libs.SubprocessUnitCalls.callit.priotype.NOK.stderrok.defaults `[test-sources] <tests.libs.SubprocessUnitCalls.callit.priotype.NOK.stderrok.defaults.html>`_

    * priotype=True:
      tests.libs.SubprocessUnitCalls.callit.priotype.OK.stderrok.defaults `[test-sources] <tests.libs.SubprocessUnitCalls.callit.priotype.OK.stderrok.defaults.html>`_

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

    For examples refer to the test subpackage:

    * priotype=True:
      tests.libs.SubprocessUnitCalls.callit.priotype.NOK.stderrok.exitign `[test-sources] <tests.libs.SubprocessUnitCalls.callit.priotype.NOK.stderrok.exitign.html>`_

    * priotype=True:
      tests.libs.SubprocessUnitCalls.callit.priotype.OK.stderrok.exitign `[test-sources] <tests.libs.SubprocessUnitCalls.callit.priotype.OK.stderrok.exitign.html>`_
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
  `[doc] <tests.libs.SystemCalls.displayit.csv.html#>`_
  `[test-sources] <_modules/tests/libs/SystemCalls/displayit/csv/CallCase.html#>`_

* **html**: Records in HTML format.
  `[doc] <tests.libs.SystemCalls.displayit.html.html#>`_
  `[test-sources] <_modules/tests/libs/SystemCalls/displayit/html/CallCase.html#>`_

* **json**: Records in JSON format.
  `[doc] <tests.libs.SystemCalls.displayit.json.html#>`_
  `[test-sources] <_modules/tests/libs/SystemCalls/displayit/json/CallCase.html#>`_

* **pass**: Pass STDOUT and STDERR transparently, set wrapper execution state as exit code.
  `[doc] <tests.libs.SystemCalls.displayit.pass.html#>`_
  `[test-sources] <_modules/tests/libs/SystemCalls/displayit/pass/CallCase.html#>`_

* **passall**: Pass STDOUT, STDERR, and exit code  transparently.
  `[doc] <tests.libs.SystemCalls.displayit.passall.html#>`_
  `[test-sources] <_modules/tests/libs/SystemCalls/displayit/passall/CallCase.html#>`_

* **raw**: Saem as passall.
  `[doc] <tests.libs.SystemCalls.displayit.raw.html#>`_
  `[test-sources] <_modules/tests/libs/SystemCalls/displayit/raw/CallCase.html#>`_

* **repr**: Python 'repr' format.
  `[doc] <tests.libs.SystemCalls.displayit.repr.html#>`_
  `[test-sources] <_modules/tests/libs/SystemCalls/displayit/repr/CallCase.html#>`_

* **review**: Records in 'review' format for on-screen inspection.
  `[doc] <tests.libs.SystemCalls.displayit.review.html#>`_
  `[test-sources] <_modules/tests/libs/SystemCalls/displayit/review/CallCase.html#>`_

* **str**: Python 'str' format.
  `[doc] <tests.libs.SystemCalls.displayit.str.html#>`_
  `[test-sources] <_modules/tests/libs/SystemCalls/displayit/str/CallCase.html#>`_

* **xml**: XML format
  `[doc] <tests.libs.SystemCalls.displayit.xml.html#>`_
  `[test-sources] <_modules/tests/libs/SystemCalls/displayit/xml/CallCase.html#>`_
