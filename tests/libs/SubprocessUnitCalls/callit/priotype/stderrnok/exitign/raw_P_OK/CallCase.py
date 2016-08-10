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

#
#######################
# 
class CallUnits(unittest.TestCase):

    def __init__(self,*args,**kargs):
        super(CallUnits,self).__init__(*args,**kargs)

        self.slst = []
        setUpperTreeSearchPath(os.path.abspath(os.path.dirname(__file__)),'epyunit',self.slst)
        
        syskargs = {}
        syskargs['raw'] = True
        syskargs['priotype'] = True
        syskargs['exitign'] = True
        syskargs['stderrnok'] = ['.+',] # a non-empty STDERR string

        self.sx = epyunit.SubprocUnit.SubprocessUnit(**syskargs)

        self.epyu = findRelPathInSearchPath('bin/epyunit',self.slst,matchidx=0)
        self.scri = findRelPathInSearchPath('epyunit/myscript.sh',self.slst,matchidx=0)
        self.scri = self.scri

    def testCase010(self):
        callkargs = {}
        _call  = self.scri
        _call += " OK "

        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, [0, 'fromA\narbitrary output\narbitrary signalling OK string\narbitrary output\n', ''])

        _s1 = self.sx.getruleset().states() # for hover
        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # for hover
        self.assertTrue(state)

        pass

    def testCase011(self):
        callkargs = {}
        _call = self.scri
        _call += " NOK "

        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, [0, 'fromB\narbitrary output\narbitrary output\n', 'arbitrary signalling ERROR string\n'])

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # for hover
        self.assertFalse(state)

        pass

    def testCase012(self):
        callkargs = {}
        _call = self.scri
        _call += " PRIO "

        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, [0, 'fromC\narbitrary output\narbitrary signalling OK string\narbitrary output\n', 'arbitrary signalling ERROR string\n'])

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # for hover
        self.assertFalse(state)

        pass

    def testCase013(self):
        callkargs = {}
        _call = self.scri
        _call += " EXITOK "

        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, [0, 'fromD\narbitrary output\narbitrary signalling OK string\narbitrary output\n', ''])

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # for hover
        self.assertTrue(state)

        pass

    def testCase014(self):
        callkargs = {}
        _call = self.scri
        _call += " EXITNOK "
        

        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, [1, 'fromE\narbitrary output\narbitrary signalling OK string\narbitrary output\n', ''])

        _s0 = self.sx.getruleset().states() # for hover in debugger
        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states()  # for hover in debugger
        self.assertTrue(state)

        pass

    def testCase015(self):
        callkargs = {}
        _call = self.scri
        _call += " EXIT7 "

        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, [7,  'fromF\narbitrary output\narbitrary signalling NOK string\narbitrary output\n', ''])

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # for hover
        self.assertTrue(state)

        pass

    def testCase016(self):
        callkargs = {}
        _call = self.scri
        _call += " EXIT8 "

        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, [8, 'fromG\narbitrary output\narbitrary signalling NOK string\narbitrary output\n', 'arbitrary err output\narbitrary err signalling NOK string\narbitrary err output\n'])

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # for hover
        self.assertFalse(state)

        pass

    def testCase017(self):
        callkargs = {}
        _call = self.scri
        _call += " EXIT9OK3NOK2 "

        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, [9, 'fromH\nOK\nOK\nOK\n', 'NOK\nNOK\n'])

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # for hover
        self.assertFalse(state)

        pass

    def testCase018(self):
        callkargs = {}
        _call = self.scri
        _call += " DEFAULT "

        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret,  [123, 'arbitrary output\n', ''])

        state = self.sx.apply(ret)
        _s1 = self.sx.getruleset().states() # for hover
        self.assertTrue(state)

        pass

    def testCase200(self):
        callkargs = {}
        _call  = self.scri
        _call += " OK "

        ret = self.sx.callit(_call,**callkargs)
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
