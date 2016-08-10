
===================================
 'epyunit' - Command line interface
===================================

The *epyunit* commandline interface provides a call wrapper
for unit and regression tests of arbitrary executables.
The wrapper internally relies on the standard packages 'PyUnit'
and integrates into Eclipse by 'PyDev'. Thus unit tests could
be applied in particular for shell scripts and intermixed 
application processes implemented in multiple programming 
languages. Automation of remote debugging by PyDev is 
supported.

The interface is minimalistic but allows for almost any required
blackbox test including seamless cross-process-debugging of executables.
  ::

    Less Is More...

In particular blackbox-tests unittests of bash-scripts are provided by a simple
call interface for seamless integration into PyDev and Eclipse.

SYNOPSIS:
^^^^^^^^^
  ::

    epyunit [OPTIONS] [--] <testee> [<testee-options>]

* rulesets for testcase evaluation
  `[syntax-tree] <rules_logic.html#the-data-correlator-status-decision>`_ 
  `[API] <epyunit.html#class-sprocunitrules>`_ 
  `[source] <_modules/epyunit/SubprocUnit.html#SProcUnitRules>`_ :

  * match pattern for filter
    `[exitvalues] <rules_logic.html#exit-values>`_ 
    `[outputstreams] <rules_logic.html#output-streams>`_ :
    ::

      --exitign,   --exittype,  --exitval,      
      --stdoutnok, --stdoutok, 
      --stderrnok, --stderrok,  

    Goto:
    :ref:`exitign <exitign>`,
    :ref:`exittype <exittype>`,
    :ref:`exitval <exitval>`,
    :ref:`stdoutnok <stdoutnok>`,
    :ref:`stdoutok <stdoutok>`,
    :ref:`stderrnok <stderrnok>`,
    :ref:`stderrok <stderrok>`

  * filter parameters
    `[outputstreams] <rules_logic.html#output-streams>`_ :
    ::

      --redebug,   --redotall,  --reignorecase, --remultiline, 
      --reunicode,

    Goto:
    :ref:`redebug <redebug>`,
    :ref:`redotall <redotall>`,
    :ref:`reignorecase <reignorecase>`,
    :ref:`remultiline <remultiline>`,
    :ref:`reunicode <reunicode>`

  * correlator parameters
    `[fuzzy results] <rules_logic.html#resolution-of-fuzzy-results>`_ :
    ::

      --priotype
      --result,    --resultnok, --resultok,      

    Goto:
    :ref:`priotype <priotype>`,
    :ref:`result <result>`,
    :ref:`resultnok <resultnok>`,
    :ref:`resultok <resultok>`

* output and format
  `[format] <rules_logic.html#output-formats-for-postprocessing>`_ :
  ::

    --csv,     --pass,    --passall,   --raw, 
    --repr,    --str,     --xml
      
    --appname, --test-id, --timestamp

  Goto:
  :ref:`csv <csv>`,
  :ref:`pass <pass>`,
  :ref:`passall <passall>`,
  :ref:`raw <raw>`,
  :ref:`repr <repr>`,
  :ref:`str <str>`,
  :ref:`xml <xml>`

* process wrapper:
  ::

    --debug,    --environment, --help,   -Version,
    --Version,  --verbose,     -version, --version
    
    --selftest, --subproc,     --subunit, 

  Goto:
  :ref:`debug <debug>`,
  :ref:`environment <environment>`,
  :ref:`help <help>`,
  :ref:`Version <Versionu>`,
  :ref:`verbose <verbose>`,
  :ref:`version <versionl>`,
  :ref:`selftest <selftest>`,
  :ref:`subproc <subproc>`,
  :ref:`subunit <subunit>`

* subprocess debugging:
  ::

    --pydev-remote-debug, --rdbg

  Goto:
  :ref:`pydev-remote-debug <pydev-remote-debug>`,
  :ref:`rdbg <pydev-remote-debug>`

OPTIONS:
^^^^^^^^

.. index::
   single: options; --appname

.. _appname:

* **appname**

  An arbitrary application name to be inserted into record 
  headers.
    ::

       --appname=<arbitrary-name-of-app>

.. index::
   single: options; --csv

.. _csv:

* **csv**

  Prints complete test result CSV format including header.
    ::

       --csv

.. index::
   single: options; --debug

.. _debug:

* **debug**

  Debug entries, does NOT work with 'python -O ...'.
  Developer output, aimed for filtering.
    ::

       --debug
       -d

.. index::
   single: options; --environment

.. _environment:

* **environment**

  Include platform info into header.
    ::

       --environment

.. index::
   single: options; --exitign

.. _exitign:

* **exitign**

  Ignore exit value. 
    ::

       --exitign=(True|False)

.. index::
   single: options; --exittype

.. _exittype:

* **exittype**

  Expect exit value type as success.
    ::

       --exittype=(True|False)

    * True:  Exit value '0' indicates success.
    * False: Exit value '!=0' indicates success.

.. index::
   single: options; --exitval
    
.. _exitval:

* **exitval**

  Indicates success when exit value is equal to the provided 
  value.
    ::

       --exitval=<exit-value>

.. index::
   single: options; --help

.. _help:

* **help**

  This help.
    ::

       --help
       -h

.. index::
   single: options; --pass

.. _pass:

* **pass**

  Pass through the testee results on STDOUT and STDERR.
  The exit value is interpreted by rules, else the
  execution state of the framework defines the exit value.
    ::

       --pass
       
         exit:   exec-state-of-wrapper-epyunit
         STDOUT: output-from-subprocess
         STDERR: output-from-subprocess

.. index::
   single: options; --passall

.. _passall:

* **passall**

  Pass through the testee result on STDOUT and STDERR
  including transparently the received exit value.
    ::

       --passall
         
         exit:   exit-of-subprocess
         STDOUT: output-from-subprocess
         STDERR: output-from-subprocess

.. index::
   single: options; --priotype

.. _priotype:

* **priotype**

  In case of present failure and success conditions,
    ::

       --priotype=(True|False)

         default := False

  * True:  The success conditions dominate, if present at least one.

  * False: the failure condition dominates. if present at least one.


.. index::
   single: options; --pydev-remote-debug

.. _pydev-remote-debug:

* **pydev-remote-debug**

  Activates remote debugging with PyDev plugin of Eclipse.
    ::

       --pydev-remote-debug[=host[:port]]

         host := (ip-add|dns-name)
         port := (port-number)       
          
         default := localhost:5678

.. index::
   single: options; --raw

.. _raw:

* **raw**

  Enables 'raw', equal to :ref:`passall <passall>`.
    ::

       --raw

.. index::
   single: options; --redebug
   single: re; re.DEBUG

.. _redebug:

* **redebug**

  Enables 're.DEBUG'
    ::

       --redebug

.. index::
   single: options; --redotall
   single: re; re.DOTALL

.. _redotall:

* **redotall**

  Enables 're.DOTALL'
    ::

       --redotall

  
.. index::
   single: options; --reignorecase
   single: re; re.IGNORECASE

.. _reignorecase:

* **reignorecase**

  Enables 're.IGNORECASE'.
    ::

       --reignorecase

  
.. index::
   single: options; --remultiline
   single: re; re.MULTILINE

.. _remultiline:

* **remultiline**

  Enables 're.MULTILINE'.
    ::

       --remultiline

.. index::
   single: options; --repr

.. _repr:

* **repr**

  Prints complete test result by Python call of 'repr()'.
    ::

       --repr

.. index::
   single: options; --result

.. _result:

* **result**

  The treshold of the total matched results for changing
  the overall state to success. 
    ::

       --result=#total-results
       
         #total-results = #total-failure-results + #total-success-results

.. index::
   single: options; --resultnokw

.. _resultnok:

* **resultnok**

  The treshold of the total matched failure results for
  changing the overall state to success. 
    ::

       --resultnok=#total-failure-results

.. index::
   single: options; --resultok

.. _resultok:

* **resultok**

  The treshold of the total matched success results for
  changing the overall state to success. 
    ::

       --resultok=#total-success-results

.. index::
   single: options; --reunicode
   single: re; re.UNICODE

.. _reunicode:

* **reunicode**

  Enables 're.UNICODE'.
    ::

       --reunicode

.. index::
   single: options; --selftest

.. _selftest:

* **selftest**

  Performs a basic functional selftest by executing the 
  basic examples based on 'myscript.sh'.
    ::

       --selftest

.. index::
   single: options; --stderrnok

.. _stderrnok:

* **stderrnok**

  Matched string '<nok-string>' on stderr indicates success.
    ::

       --stderrnok=<nok-string>
       
       <nok-string>:=(literal|regexpr)
       literal := string-literal
       regexpr := regular-expression-re-module

.. index::
   single: options; --stdoutnok

.. _stdoutnok:

* **stdoutnok**

  Matched string '<nok-string>' on stdout indicates success.
    ::

       --stdoutnok=<nok-string>
       
       <nok-string>:=(literal|regexpr)
       literal := string-literal
       regexpr := regular-expression-re-module

.. index::
   single: options; --stderrnok

.. _stderrok:

* **stderrok**

  Matched string '<ok-string>' on stderr indicates success.
    ::

       --stderrok=<ok-string>
       
       <ok-string>:=(literal|regexpr)
       literal := string-literal
       regexpr := regular-expression-re-module

.. index::
   single: options; --stdotok

.. _stdoutok:

* **stdoutok**

  Matched string '<ok-string>' on stdout indicates success.
    ::

       --stdoutok=<ok-string>
       
       <ok-string>:=(literal|regexpr)
       literal := string-literal
       regexpr := regular-expression-re-module

.. index::
   single: options; --str

.. _str:

* **str**

  Prints complete test result by Python call of 'str()'.
    ::

       --str

.. index::
   single: options; --subproc

.. _subproc:

* **subproc**

  Change the framework for the subprocess call.
    ::

       --subproc

  Starts the subprocess by:

     'epyunit.SystemCalls'

  instead of the default:

      'epyunit.SubprocessUnit'

.. index::
   single: options; --subunit

.. _subunit:

* **subunit**

  Change the framework for the subprocess call.
    ::

       --subunit

  Starts the subprocess by default:

      'epyunit.SubprocessUnit'

.. index::
   single: options; --test-id

.. _test-id:

* **test-id**

  Prints the test-id with the formats 'csv', and 'xml'.
  Too be applied in case of multiple test case calls.
    ::

       --test-id=<arbitrary-identifier-for-record-header>

.. index::
   single: options; --timestamp

.. _timestamp:

* **timestamp**

  Includes date and time into record header.
    ::

       --timestamp

.. index::
   single: options; --Version

.. _Versionu:

* **Version**

  Current version - detailed.
    ::

       --Version
       -Version

.. index::
   single: options; --verbose

.. _verbose:

* **verbose**

  Verbose, some relevant states for basic analysis.
  When '--selftest' is set, repetition raises the display 
  level.
    ::

       --verbose
       -v

.. index::
   single: options; --version

.. _versionl:

* **version**

  Current version - terse.
    ::

       --version
       -version

.. _xml:

.. index::
   single: options; --xml

* **xml**

  Prints complete test result XML format.
    ::

       --xml

ARGUMENTS:
^^^^^^^^^^

.. index::
   single: arguments; --

* **[--]**

  To be used when ambigous options and/or arguments exist, 
  the first match terminates the evaluatoin of the 
  wrapper options.
    ::

      [--]

.. index::
   single: arguments; testee

* **testee**

  The wrapped testee, see :ref:`EXAMPLES <examples>`.
    ::

      <testee> 

.. index::
   single: arguments; testee-options

* **testee-options**

  Options of the testee, see :ref:`EXAMPLES <examples>`.
    ::

      [<testee-options>]

DESCRIPTION:
^^^^^^^^^^^^

The call interface 'epyunit' provides the commandline interface for
the unit test wrapper classes.

The call is simply a prefix to the actual testee including it's options.
The wrapper itself provides various criteria for the indication of the
success and/or failure of the test case.
Therefore correlation of stdout, stderr, and exit 
values is provided. 

The following categories of parameter are provided:

.. index::
   single: filtering

* **Filtering of sub-results**:

  .. hlist::
     :columns: 4

     * --exitign
     * --exittype
     * --exitval
     * --stderrnok
     * --stdoutnok
     * --stderrok
     * --stdoutok

  .
.. index::
   single: decision
   single: filtering

* **Adjusting the decision process**:

  * **Expected result types**:

    .. hlist::
       :columns: 4

       * --priotype

    .
.. index::
   single: counter
   single: threshold

  * **Counter and thresholds**:

    .. hlist::
       :columns: 4

       * --result
       * --resultnok
       * --resultok

    .
.. index::
   single: match
   single: regexpr
   single: re

  * **Match sub-results**:

    .. hlist::
       :columns: 4

       * --redebug
       * --redotall
       * --reignorecase
       * --remultiline
       * --reunicode

    .
.. index::
   single: wrapper
   single: SystemCalls
   single: SubprocessUnit

  * **Wrapper**:

    .. hlist::
       :columns: 4

       * --subproc
       * --subunit

    .
.. index::
   single: debugging

* **Subprocess debugging**:

  .. hlist::
     :columns: 4

     * --pydev-remote-debug

  .
.. index::
   single: format

* **Output format**:

  .. hlist::
     :columns: 4

     * --csv
     * --pass
     * --passall
     * --repr
     * --str
     * --xml

  .
* **Miscellaneous**:

  .. hlist::
     :columns: 4

     * -d
     * --debug
     * --appname
     * --environment
     * -h 
     * --help
     * --selftest
     * --test-id
     * --timestamp
     * -Version 
     * --Version
     * -v 
     * --verbose
     * -version
     * --version

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
