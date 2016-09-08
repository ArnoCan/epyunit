from __future__ import absolute_import
from __future__ import print_function
 
__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'
 
__docformat__ = "restructuredtext en"
 
import unittest
import os
 
from filesysobjects.FileSysObjects import setUpperTreeSearchPath,findRelPathInSearchPath
import epyunit.SubprocUnit 
from epyunit.unittest.subprocess import TestExecutable 
from testdata import call_scripy,call_scrish,epyu

#
#######################
# 
class CallUnits(TestExecutable):

    def __init__(self,*args,**kargs):
        super(CallUnits,self).__init__(*args,**kargs)

    @classmethod
    def setUpClass(cls):
        cls.epyu = epyu
        cls.scri = call_scripy
        cls._call = call_scripy
        
        cls.callkargs = {}
        cls.callkargs['exitign'] = False # default
        cls.callkargs['exittype'] = False

    def setUp(self):
        syskargs = {}
        self.sx = epyunit.SubprocUnit.SubprocessUnit(**syskargs)


    def testCase010(self):
        self._call += " OK "
        ret = self.sx.callit(self._call,**self.callkargs)
        assert ret ==  [0, ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]
        pass

    def testCase011(self):
        self._call += " NOK "
        ret = self.sx.callit(self._call,**self.callkargs)
        assert ret ==  [0, ['fromB', 'arbitrary output', 'arbitrary output'], ['arbitrary signalling ERROR string']]
        pass

    def testCase012(self):
        self._call += " PRIO "
        ret = self.sx.callit(self._call,**self.callkargs)
        assert ret ==   [0, ['fromC', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], ['arbitrary signalling ERROR string']]
        pass

    def testCase013(self):
        self._call += " EXITOK "
        ret = self.sx.callit(self._call,**self.callkargs)
        assert ret ==  [0, ['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]
        pass

    def testCase014(self):
        self._call += " EXITNOK "
        ret = self.sx.callit(self._call,**self.callkargs)
        assert ret ==   [1, ['fromE', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]
        pass

    def testCase015(self):
        self._call += " EXIT7 "
        ret = self.sx.callit(self._call,**self.callkargs)
        assert ret ==   [7, ['fromF', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], []]
        pass

    def testCase016(self):
        self._call += " EXIT8 "
        ret = self.sx.callit(self._call,**self.callkargs)
        assert ret ==   [8, ['fromG', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], ['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']]
        pass

    def testCase017(self):
        self._call += " EXIT9OK3NOK2 "
        ret = self.sx.callit(self._call,**self.callkargs)
        assert ret ==  [9, ['fromH', 'OK', 'OK', 'OK'], ['NOK', 'NOK']]
        pass

    def testCase018(self):
        self._call += " DEFAULT "
        ret = self.sx.callit(self._call,**self.callkargs)
        assert ret ==   [123, ['arbitrary output'], []]
        pass

#
#######################
#
 
if __name__ == '__main__':
    unittest.main()

