PyDev call examples within Eclipse - Python Library
===================================================

A call example of the integration of 'epyunit' into
Eclipse with PyDev and PyUnit.
The test executable is a simple shell script named
'myscript.sh' demonstrating some of the major cases
of integration into PyUnit.
For the script code refer to 
`CLI examples <epyunit_example_cli.html>`_ .

The integration into the PyUnit framework is coded as a
test case by provided library modules::

  """Test in PyUnit environment.
  """
  from __future__ import absolute_import

  __author__ = 'Arno-Can Uestuensoez'
  __license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
  __copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
  __version__ = '0.0.1'
  __uuid__ = '72d93726-cc26-46a2-a3d5-097d9f700b42'

  __docformat__ = "restructuredtext en"

  import unittest
  import os

  #
  # set search for the call of 'myscript.sh'
  from epyunit.FileSysObjectsMin import setUpperTreeSearchPath
  setUpperTreeSearchPath(None,'tests')

  from epyunit.SystemCalls import SystemCalls

  #
  #######################
  #

  class CallUnits(unittest.TestCase):
      name=os.path.curdir+__file__

      output=True
      output=False

      def testCase000(self):
          """Call first selftest part.
          """
          sx = SystemCalls(**{"proceed":"trace"})
          ret = sx.callit("myscript.sh xOK")

          assert ret[0] == 123
          assert ret[1] == "arbitrary output\n"
          assert ret[2] == ""
          pass

  #
  #######################
  #
  if __name__ == '__main__':
      unittest.main()



A setup and call example for the Eclipse integration with PyDev.

  0. Setup Eclipse and PyDev

  1. Setup PyUnit wrapper extension ePyUnit

  2. Setup call parameters

  3. Call PyUnit within Eclipse 

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
    myscript.sh NOK

The commandline wrapper call for case 'E' is 
::

  epyunit \
    --ok-stdout="arbitrary signalling OK string" \
    --nok-stderr="arbitrary signalling ERROR string" \
    --exit-ok \
    --default-ok \
    myscript.sh


For detailed examples refer to the subdirectories of the source package for:

* Unit tests 

* UseCases


For examples of application as a commandline call of PyUnit refer to

  * `Executable <epyunit_example_eclipse_executable.html>`_ 

  * `Python API <epyunit_example_eclipse_python.html>`_ 
