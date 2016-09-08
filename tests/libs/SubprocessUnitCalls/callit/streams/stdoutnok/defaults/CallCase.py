"""Initial raw tests by SubprocessUnit with hard-coded defaults.

Due to the basic character of the test these are done a little more than less.

"""
from __future__ import absolute_import
#from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import unittest
import os

from filesysobjects.FileSysObjects import setUpperTreeSearchPath,findRelPathInSearchPath
import epyunit.SubprocUnit
from testdata import call_scripy,epyu

#
#######################
#
class CallUnits(unittest.TestCase):

    def __init__(self,*args,**kargs):
        super(CallUnits,self).__init__(*args,**kargs)

    @classmethod
    def setUpClass(cls):
        cls.slst = []
        setUpperTreeSearchPath(os.path.abspath(os.path.dirname(__file__)),'epyunit',cls.slst)

        cls.epyu = epyu
        cls.scri = call_scripy
        cls.scri = cls.scri

    def setUp(self):
        syskargs = {}
        syskargs['raw'] = True
        #syskargs['priotype'] = True
        syskargs['stderrnok'] = ['.+',] # a non-empty STDERR string

        self.sx = epyunit.SubprocUnit.SubprocessUnit(**syskargs)

    def testCaseOK(self):
        callkargs = {}
        _call  = self.scri
        _call += " OK "

        ret = self.sx.callit(_call,**callkargs); ret[1]=ret[1].replace('\r','');ret[2]=ret[2].replace('\r','')
        self.assertEqual(ret, [0, 'fromA\narbitrary output\narbitrary signalling OK string\narbitrary output\n', ''])

        _s1 = self.sx.getruleset().states() # for hover
        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # for hover
        self.assertTrue(state)

        pass

    def testCaseNOK(self):
        callkargs = {}
        _call = self.scri
        _call += " NOK "

        ret = self.sx.callit(_call,**callkargs); ret[1]=ret[1].replace('\r','');ret[2]=ret[2].replace('\r','')
        self.assertEqual(ret, [0, 'fromB\narbitrary output\narbitrary output\n', 'arbitrary signalling ERROR string\n'])

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # for hover
        self.assertFalse(state)

        pass

    def testCasePRIO(self):
        callkargs = {}
        _call = self.scri
        _call += " PRIO "

        ret = self.sx.callit(_call,**callkargs); ret[1]=ret[1].replace('\r','');ret[2]=ret[2].replace('\r','')
        self.assertEqual(ret, [0, 'fromC\narbitrary output\narbitrary signalling OK string\narbitrary output\n', 'arbitrary signalling ERROR string\n'])

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # for hover
        self.assertFalse(state)

        pass

    def testCaseEXITOK(self):
        callkargs = {}
        _call = self.scri
        _call += " EXITOK "

        ret = self.sx.callit(_call,**callkargs); ret[1]=ret[1].replace('\r','');ret[2]=ret[2].replace('\r','')
        self.assertEqual(ret, [0, 'fromD\narbitrary output\narbitrary signalling OK string\narbitrary output\n', ''])

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # for hover
        self.assertTrue(state)

        pass

    def testCaseEXITNOK(self):
        callkargs = {}
        _call = self.scri
        _call += " EXITNOK "


        ret = self.sx.callit(_call,**callkargs); ret[1]=ret[1].replace('\r','');ret[2]=ret[2].replace('\r','')
        self.assertEqual(ret, [1, 'fromE\narbitrary output\narbitrary signalling OK string\narbitrary output\n', ''])

        _s0 = self.sx.getruleset().states() # for hover in debugger
        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states()  # for hover in debugger
        self.assertFalse(state)

        pass

    def testCaseEXIT7(self):
        callkargs = {}
        _call = self.scri
        _call += " EXIT7 "

        ret = self.sx.callit(_call,**callkargs); ret[1]=ret[1].replace('\r','');ret[2]=ret[2].replace('\r','')
        self.assertEqual(ret, [7,  'fromF\narbitrary output\narbitrary signalling NOK string\narbitrary output\n', ''])

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # for hover
        self.assertFalse(state)

        pass

    def testCaseEXIT8(self):
        callkargs = {}
        _call = self.scri
        _call += " EXIT8 "

        ret = self.sx.callit(_call,**callkargs); ret[1]=ret[1].replace('\r','');ret[2]=ret[2].replace('\r','')
        self.assertEqual(ret, [8, 'fromG\narbitrary output\narbitrary signalling NOK string\narbitrary output\n', 'arbitrary err output\narbitrary err signalling NOK string\narbitrary err output\n'])

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # for hover
        self.assertFalse(state)

        pass

    def testCaseEXIT9OK3NOK2(self):
        callkargs = {}
        _call = self.scri
        _call += " EXIT9OK3NOK2 "

        ret = self.sx.callit(_call,**callkargs); ret[1]=ret[1].replace('\r','');ret[2]=ret[2].replace('\r','')
        self.assertEqual(ret, [9, 'fromH\nOK\nOK\nOK\n', 'NOK\nNOK\n'])

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # for hover
        self.assertFalse(state)

        pass

    def testCaseDEFAULT(self):
        callkargs = {}
        _call = self.scri
        _call += " DEFAULT "

        ret = self.sx.callit(_call,**callkargs); ret[1]=ret[1].replace('\r','');ret[2]=ret[2].replace('\r','')
        self.assertEqual(ret,  [123, 'arbitrary output\n', ''])

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # for hover
        self.assertFalse(state)

        pass

    def testCase200_OK(self):
        callkargs = {}
        _call  = self.scri
        _call += " OK "

        ret = self.sx.callit(_call,**callkargs); ret[1]=ret[1].replace('\r','');ret[2]=ret[2].replace('\r','')
        self.assertEqual(ret, [0, 'fromA\narbitrary output\narbitrary signalling OK string\narbitrary output\n', ''])

        _s1 = self.sx.getruleset().states()
        self.sx.getruleset().setrules(**{'stderrnok': ['.+','..*','[a-zA-Z0-9]+'],})
        _s1 = self.sx.getruleset().states() # for hover
        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # for hover
        self.assertTrue(state)

        pass


#
#######################
#

if __name__ == '__main__':
    unittest.main()
