
===================================
 'epyunit' - Command line interface
===================================

The *epyunit* commandline interface provides a command line wrapper
for unit and regression tests of arbitrary executables.
The wrapper internally relies on the standard 
packages 'PyUnit' and integrates into Eclipse by 'PyDev'.

**SYNOPSIS:**::

  epyunit [OPTIONS] [--] <testee> [<testee-options>]

**OPTIONS:**::

  --appname=<arbitrary-name-of-app>
    An arbitrary application name to be inserted into record headers.
    
  --csv
    Prints complete test result CSV format including header.

  -d --debug
     Debug entries, does NOT work with 'python -O ...'.
     Developer output, aimed for filtering.

  --default-nok
    When multiple options match, prioritize a 
    matching NOK option as success.

  --default-ok
    When multiple options match, prioritize a 
    matching OK option as success.

  --environment
    Include platform info into header.

  --exit=<exit-value>
    Indicates success when exit value is equal to the provided value.

  --exit-ignore
    Ignore exit value, as default '0' is
    required for success. 

  --exit-nok
    Exit value '!=0' indicates success.

  --exit-ok
    Exit value '0' indicates success.

  -h --help
     This help.

  --nok-stderr=<nok-string>
    Error string on stderr indicates success.

  --nok-stdout=<nok-string>
    Error string on stdout indicates success.

  --ok-stderr=<ok-string>
    OK string on stderr indicates success.

  --ok-stdout=<ok-string>
    OK string on stdout indicates success.

  --pass-through
    Pass through the testee results on STDOUT and STDERR.
    The exit value is intepreted by rules.
    
  --pass-through-all
    Pass through the testee result on STDOUT and STDERR,
    also passes transparently the received exit value.

  --prio-nok
    In case of present failure and success conditions,
    the success condition dominates.

  --prio-ok
    In case of present failure and success conditions,
    the failure condition dominates.

  --repr
    Prints complete test result by Python call of 'repr()'.

  -selftest --selftest

     Performs a basic functional selftest by executing the basic 
     examples based on 'myscript.sh'.

  --test-id=<arbitrary-identifier-for-record-header>
    Prints the test-id with the formats 'csv', and 'xml'.
    Too be applied in case of multiple test case calls.

  --timestamp
    Includes date and time into record header.

  -Version --Version
     Current version - detailed.

  -v --verbose
     Verbose, some relevant states for basic analysis.
     When '--selftest' is set, repetition raises the display level.

  -version --version
     Current version - terse.

  --xml
    Prints complete test result XML format.


**ARGUMENTS**::

  [--] 
     To be used when ambigous options and/or arguments exist, 
     the first match terminates the evaluatoin of the 
     wrapper options.

  <testee> 
     The wrapped testee.

  [<testee-options>]
     Options of the testee.

**DESCRIPTION**:

The call interface 'epyunit' provides the commandline interface for
the unit test wrapper classes.

The call is simply a prefix to the actual testee including it's options.
The wrapper itself provides various criteria for the indication of the
success and/or failure of the test case.

**ENVIRONMENT**:

  * PYTHON OPTIONS:
    -O, -OO: Eliminates '__debug__' code.
 
**EXAMPLES**:

Basic call examples are provided:

* `CLI: command line interface <epyunit_example_cli.html>`_ 

* Eclipse: PyDev integration by call of:

  * `Executable <epyunit_example_eclipse_executable.html>`_ 

  * `Python API <epyunit_example_eclipse_python.html>`_ 

For detailed examples refer to the subdirectories of the source package for:

* Unit tests 

* UseCases
