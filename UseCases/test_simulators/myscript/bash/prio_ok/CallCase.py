"""
Default case for a testee with result: succeed: OK

  EXIT:
     0
  STDOUT:
     arbitrary output
     arbitrary signalling OK string
     arbitrary output
  STDERR:
     -

"""
from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"


import unittest
import sys
from testdata import call_scrish,epyu,_available_bash
import epyunit.SystemCalls

#
#######################
#
#
class CallUnits(unittest.TestCase):

    def testCase010(self):
        if not _available_bash:
            self.skipTest("bash not available")

        _call  = epyu
        _call += " --priotype=True "
        _call += " --  "+ call_scrish
        _call += " OK "

        syskargs = {}
        sx = epyunit.SystemCalls.SystemCalls(**syskargs)

        callkargs = {}
        ret = sx.callit(_call,**callkargs)
        if sys.platform == 'win32' and ret[0] != ret:
            self.skipTest("bash not available")
        else:
            assert ret[0] == 0

    def testCase020(self):
        if not _available_bash:
            self.skipTest("bash not available")

        _call  = epyu
        _call += " --priotype=True "
        _call += " --  "+ call_scrish
        _call += " NOK "

        syskargs = {}
        sx = epyunit.SystemCalls.SystemCalls(**syskargs)

        callkargs = {}
        ret = sx.callit(_call,**callkargs)
        if sys.platform == 'win32' and ret[0] != ret:
            self.skipTest("bash not available")
        else:
            assert ret[0] == 0

    def testCase030(self):
        if not _available_bash:
            self.skipTest("bash not available")

        _call  = epyu
        _call += " --priotype=True "

        _call += " --  "+ call_scrish
        _call += " EXIT7 "

        syskargs = {}
        sx = epyunit.SystemCalls.SystemCalls(**syskargs)

        callkargs = {}
        ret = sx.callit(_call,**callkargs)
        if sys.platform == 'win32' and ret[0] != ret:
            self.skipTest("bash not available")
        else:
            assert ret[0] == 1

#
#######################
#

if __name__ == '__main__':
    unittest.main()

