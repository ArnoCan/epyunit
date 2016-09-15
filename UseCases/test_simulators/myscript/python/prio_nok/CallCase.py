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
from testdata import call_scripy,epyu
import epyunit.SystemCalls

#
#######################
#
#
class CallUnits(unittest.TestCase):


    def testCase010_NOK(self):
        if not call_scripy:
            self.skipTest("bash not available")
        
        _call  = epyu 
        _call += " --  "+ call_scripy
        _call += " NOK "

        syskargs = {}
        sx = epyunit.SystemCalls.SystemCalls(**syskargs)

        callkargs = {}
        ret = sx.callit(_call,**callkargs)

        assert ret[0] == 0

    def testCase020_NOK_PRIOTYPE(self):
        if not call_scripy:
            self.skipTest("bash not available")

        _call  = epyu 
        _call += " --priotype=False "
        _call += " --  "+ call_scripy
        _call += " NOK "

        syskargs = {}
        sx = epyunit.SystemCalls.SystemCalls(**syskargs)

        callkargs = {}
        ret = sx.callit(_call,**callkargs)

        assert ret[0] == 0

    def testCase030_NOK_PRIOTYPE(self):
        if not call_scripy:
            self.skipTest("bash not available")

        _call  = epyu 
        _call += " --priotype=False "
        _call += " --  "+ call_scripy
        _call += " EXIT7 "

        syskargs = {}
        sx = epyunit.SystemCalls.SystemCalls(**syskargs)

        callkargs = {}
        ret = sx.callit(_call,**callkargs)

        assert ret[0] == 1
#
#######################
#

if __name__ == '__main__':
    unittest.main()
