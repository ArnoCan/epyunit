
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

**SYNOPSIS:**:
  ::

    epyunit [OPTIONS] [--] <testee> [<testee-options>]

**OPTIONS:**:

.. index::
   single: options; --appname

* **appname**

  An arbitrary application name to be inserted into record 
  headers.
    ::

       --appname=<arbitrary-name-of-app>

.. index::
   single: options; --csv

* **csv**

  Prints complete test result CSV format including header.
    ::

       --csv

.. index::
   single: options; --debug

* **debug**

  Debug entries, does NOT work with 'python -O ...'.
  Developer output, aimed for filtering.
    ::

       --debug
       -d

.. index::
   single: options; --environment

* **environment**

  Include platform info into header.
    ::

       --environment

.. index::
   single: options; --exitign

* **exitign**

  Ignore exit value. 
    ::

       --exitign=(True|False)

.. index::
   single: options; --exittype

* **exittype**

  Exit value 'True' indicates success for '0',
  'False' indicates success for '!=0'.
    ::

       --exittype=(True|False)

.. index::
   single: options; --exitval
    
* **exitval**

  Indicates success when exit value is equal to the provided 
  value.
    ::

       --exitval=<exit-value>

.. index::
   single: options; --help

* **help**

  This help.
    ::

       --help
       -h

.. index::
   single: options; --pass

* **pass**

  Pass through the testee results on STDOUT and STDERR.
  The exit value is interpreted by rules, else the
  execution state of the framework defines the exit value.
    ::

       --pass

.. index::
   single: options; --passall

* **passall**

  Pass through the testee result on STDOUT and STDERR
  including transparently the received exit value.
    ::

       --passall

.. index::
   single: options; --priotype

* **priotype**

  In case of present failure and success conditions,
  * TRUE:  the success condition dominates.
  * FALSE: the failure condition dominates.

    ::

       --priotype


.. index::
   single: options; --pydev-remote-debug

* **pydev-remote-debug**

  Activates remote debugging with PyDev plugin of Eclipse.
    ::

       --pydev-remote-debug[=host[:port]]

.. index::
   single: options; --redebug
   single: re; re.DEBUG

* **redebug**

  Enables 're.DEBUG'
    ::

       --redebug

.. index::
   single: options; --redotall
   single: re; re.DOTALL

* **redotall**

  Enables 're.DOTALL'
    ::

       --redotall

  
.. index::
   single: options; --reignorecase
   single: re; re.IGNORECASE

* **reignorecase**

  Enables 're.IGNORECASE'.
    ::

       --reignorecase

  
.. index::
   single: options; --remultiline
   single: re; re.MULTILINE

* **remultiline**

  Enables 're.MULTILINE'.
    ::

       --remultiline

.. index::
   single: options; --repr

* **repr**

  Prints complete test result by Python call of 'repr()'.
    ::

       --repr

.. index::
   single: options; --result

* **result**

  The treshold of the total matched results for changing
  the overall state to success. 
    ::

       --result=#total-results

.. index::
   single: options; --resultnok

* **resultnok**

  The treshold of the total matched failure results for
  changing the overall state to success. 
    ::

       --resultnok=#total-failure-results

.. index::
   single: options; --resultok

* **resultok**

  The treshold of the total matched success results for
  changing the overall state to success. 
    ::

       --resultok=#total-success-results

.. index::
   single: options; --reunicode
   single: re; re.UNICODE

* **reunicode**

  Enables 're.UNICODE'.
    ::

       --reunicode

.. index::
   single: options; --selftest

* **selftest**

  Performs a basic functional selftest by executing the 
  basic examples based on 'myscript.sh'.
    ::

       --selftest

.. index::
   single: options; --stderrnok

* **stderrnok**

  Error string on stderr indicates success.
    ::

       --stderrnok=<nok-string>

.. index::
   single: options; --stdoutnok

* **stdoutnok**

  Error string on stdout indicates success.
    ::

       --stdoutnok=<nok-string>

.. index::
   single: options; --stderrnok

* **stderrok**

  OK string on stderr indicates success.
    ::

       --stderrok=<ok-string>

.. index::
   single: options; --stdotok

* **stdoutok**

  OK string on stdout indicates success.
    ::

       --stdoutok=<ok-string>

.. index::
   single: options; --str

* **str**

  Prints complete test result by Python call of 'str()'.
    ::

       --str

.. index::
   single: options; --subproc

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

* **subunit**

  Change the framework for the subprocess call.
    ::

       --subunit

  Starts the subprocess by default:

      'epyunit.SubprocessUnit'

.. index::
   single: options; --test-id

* **test-id**

  Prints the test-id with the formats 'csv', and 'xml'.
  Too be applied in case of multiple test case calls.
    ::

       --test-id=<arbitrary-identifier-for-record-header>

.. index::
   single: options; --timestamp

* **timestamp**

  Includes date and time into record header.
    ::

       --timestamp

.. index::
   single: options; --Version

* **Version**

  Current version - detailed.
    ::

       --Version
       -Version

.. index::
   single: options; --verbose

* **verbose**

  Verbose, some relevant states for basic analysis.
  When '--selftest' is set, repetition raises the display 
  level.
    ::

       --verbose
       -v

.. index::
   single: options; --version

* **version**

  Current version - terse.
    ::

       --version
       -version

.. index::
   single: options; --xml

* **xml**

  Prints complete test result XML format.
    ::

       --xml

**ARGUMENTS**:

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

  The wrapped testee.     
    ::

      <testee> 

.. index::
   single: arguments; testee-options

* **testee-options**

  Options of the testee.     
    ::

      [<testee-options>]

**DESCRIPTION**:

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

**ENVIRONMENT**:

  * PYTHON OPTIONS:
    -O, -OO: Eliminates '__debug__' code.
 
**EXAMPLES**:

* `CLI: command line interface <epyunit_example_cli.html>`_ 

* `Eclipse: Executable within Eclipse IDE <epyunit_example_eclipse_executable.html>`_ 

* Detailed examples in the subdirectories of the source package:

  * tests + testdata 

  * UseCases

COPYRIGHT:
  Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez
  Copyright (C)2015-2016 Arno-Can Uestuensoez
