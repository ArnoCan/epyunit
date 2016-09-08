from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import sys
from cStringIO import StringIO
import unittest

import epyunit.SubprocUnit 

from testdata import epyu,call_scripy

#
#######################
#
class CallUnits(unittest.TestCase):

    def __init__(self,*args,**kargs):
        super(CallUnits,self).__init__(*args,**kargs)

    @classmethod
    def setUpClass(cls):
        syskargs = {}
        syskargs['emptyiserr'] = True
        cls.sx = epyunit.SubprocUnit.SubprocessUnit(**syskargs)

        # buffers for evaluation after intercepted exit.
        cls.stdoutbuf=StringIO()
        cls.stderrbuf=StringIO()
        cls.stdout = sys.stdout
        cls.stderr = sys.stderr

        cls._call  = epyu
        cls._call += " --exitign=False "
        cls._call += " -- "
        cls._call += call_scripy


    def testCase010(self):
        _call  = self._call
        _call += " OK "
        retX = [0,['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'],[]]
        ret = self.sx.callit(_call)
        self.assertEqual(ret,retX)

        state = self.sx.apply(ret)
        assert state
        pass

    def testCase011(self):
        _call  = self._call
        _call += " NOK "
        retX = [0,['fromB', 'arbitrary output', 'arbitrary output'],['arbitrary signalling ERROR string']]
        ret = self.sx.callit(_call)
        self.assertEqual(ret,retX)

        state = self.sx.apply(ret)
        assert state
        pass

    def testCase012(self):
        _call  = self._call
        _call += " PRIO "
        retX = [0,['fromC', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'],['arbitrary signalling ERROR string']]
        ret = self.sx.callit(_call)
        self.assertEqual(ret,retX)

        state = self.sx.apply(ret)
        assert state
        pass

    def testCase013(self):
        _call  = self._call
        _call += " EXITOK "
        retX = [0,['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'],[]]
        ret = self.sx.callit(_call)
        self.assertEqual(ret,retX)

        state = self.sx.apply(ret)
        assert state
        pass

    def testCase014(self):
        _call  = self._call
        _call += " EXITNOK "
        retX = [1,['fromE', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'],[]]
        ret = self.sx.callit(_call)
        self.assertEqual(ret,retX)

        _s1 = self.sx.getruleset().states() # for hover
        state = self.sx.apply(ret)
        self.assertFalse(state)
        pass

    def testCase015(self):
        _call  = self._call
        _call += " EXIT7 "
        retX = [1,['fromF', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'],[]]
        ret = self.sx.callit(_call)
        self.assertEqual(ret,retX)

        _s1 = self.sx.getruleset().states() # for hover
        state = self.sx.apply(ret)
        self.assertFalse(state)
        pass

    def testCase016(self):
        _call  = self._call
        _call += " EXIT8 "
        retX = [1,['fromG', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'],['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']]
        ret = self.sx.callit(_call)
        self.assertEqual(ret,retX)

        _s1 = self.sx.getruleset().states() # for hover
        state = self.sx.apply(ret)
        self.assertFalse(state)
        pass

    def testCase017(self):
        _call  = self._call
        _call += " EXIT9OK3NOK2 "
        retX = [1,['fromH', 'OK', 'OK', 'OK'],['NOK', 'NOK']]
        ret = self.sx.callit(_call)
        self.assertEqual(ret,retX)

        _s1 = self.sx.getruleset().states() # for hover
        state = self.sx.apply(ret)
        self.assertFalse(state)
        pass

    def testCase018(self):
        _call  = self._call
        _call += " DEFAULT "
        retX = [1,['arbitrary output'],[]]
        ret = self.sx.callit(_call)
        self.assertEqual(ret,retX)

        _s1 = self.sx.getruleset().states() # for hover
        state = self.sx.apply(ret)
        self.assertFalse(state)
        pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()

