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

import sys
from cStringIO import StringIO
import unittest

import epyunit.SystemCalls 

from testdata import epyu,call_scripl

from filesysobjects.FileSysObjects import findRelPathInSearchPath

#
#######################
#
#
class CallUnits(unittest.TestCase):

    def __init__(self,*args,**kargs):
        super(CallUnits,self).__init__(*args,**kargs)

    @classmethod
    def setUpClass(cls):
        syskargs = {}
        cls.sx = epyunit.SystemCalls.SystemCalls(**syskargs)

        # buffers for evaluation after intercepted exit.
        cls.stdoutbuf=StringIO()
        cls.stderrbuf=StringIO()
        cls.stdout = sys.stdout
        cls.stderr = sys.stderr

    def setUp(self):
        syskargs = {}
        syskargs['emptyiserr'] = True

    def testCase010(self):
        if not call_scripl:
            self.skipTest("perl not available")

        _call  = epyu 
        _call += " --exittype=True "
        _call += " --  "+ call_scripl
        _call += " OK "

        callkargs = {}
        ret = self.sx.callit(_call,**callkargs)

        retX = [0, ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'],[]]
        self.assertEqual(ret,retX)

    def testCase020(self):
        if not call_scripl:
            self.skipTest("perl not available")

        _call  = epyu 
        _call += " --exittype=True "
        _call += " --  "+ call_scripl
        _call += " NOK "

        callkargs = {}
        ret = self.sx.callit(_call,**callkargs)

        retX = [0, ['fromB', 'arbitrary output', 'arbitrary output'],['arbitrary signalling ERROR string']]
        self.assertEqual(ret,retX)

    def testCase030(self):
        if not call_scripl:
            self.skipTest("perl not available")

        _call  = epyu 
        _call += " --exittype=True "
        _call += " --  "+ call_scripl
        _call += " EXIT7 "

        callkargs = {}
        ret = self.sx.callit(_call,**callkargs)

        retX = [1, ['fromF', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'],[]]
        self.assertEqual(ret,retX)
#
#######################
#

if __name__ == '__main__':
    unittest.main()


