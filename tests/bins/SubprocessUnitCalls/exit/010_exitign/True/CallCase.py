from __future__ import absolute_import
from __future__ import print_function
 
__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'
 
__docformat__ = "restructuredtext en"
 
import unittest
import os,sys
 
from filesysobjects.FileSysObjects import setUpperTreeSearchPath,findRelPathInSearchPath
import epyunit.SystemCalls 

#
#######################
# 
class CallUnits(unittest.TestCase):

    def __init__(self,*args,**kargs):
        super(CallUnits,self).__init__(*args,**kargs)
        
        self.slst = []
        setUpperTreeSearchPath(os.path.abspath(os.path.dirname(__file__)),'epyunit',self.slst)
        
        self.epyu = findRelPathInSearchPath('bin/epyunit',self.slst,matchidx=0)
        self.scri = findRelPathInSearchPath('epyunit/myscript.sh',self.slst,matchidx=0)

        syskargs = {}
        self.sx = epyunit.SystemCalls.SystemCalls(**syskargs)

        self._call  = self.epyu
        #self. _call += " --rdbg "
        #self._call += " --raw "
        self._call += " --exitign=True "
        self._call += " -- "
        self._call += self.scri

    def testCase010(self):
        callkargs = {}
        self._call += " OK "
        ret = self.sx.callit(self._call,**callkargs)
        assert ret ==  [0, ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]
        pass

    def testCase011(self):
        callkargs = {}
        self._call += " NOK "
        ret = self.sx.callit(self._call,**callkargs)
        assert ret ==  [0, ['fromB', 'arbitrary output', 'arbitrary output'], ['arbitrary signalling ERROR string']]
        pass

    def testCase012(self):
        callkargs = {}
        self._call += " PRIO "
        ret = self.sx.callit(self._call,**callkargs)
        assert ret ==   [0, ['fromC', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], ['arbitrary signalling ERROR string']]
        pass

    def testCase013(self):
        callkargs = {}
        self._call += " EXITOK "
        ret = self.sx.callit(self._call,**callkargs)
        assert ret ==  [0, ['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]
        pass

    def testCase014(self):
        callkargs = {}
        self._call += " EXITNOK "
        ret = self.sx.callit(self._call,**callkargs)
        assert ret ==   [0, ['fromE', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]
        pass

    def testCase015(self):
        callkargs = {}
        self._call += " EXIT7 "
        ret = self.sx.callit(self._call,**callkargs)
        assert ret ==   [0, ['fromF', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], []]
        pass

    def testCase016(self):
        callkargs = {}
        self._call += " EXIT8 "
        ret = self.sx.callit(self._call,**callkargs)
        assert ret ==   [0, ['fromG', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], ['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']]
        pass

    def testCase017(self):
        callkargs = {}
        self._call += " EXIT9OK3NOK2 "
        ret = self.sx.callit(self._call,**callkargs)
        assert ret ==  [0, ['fromH', 'OK', 'OK', 'OK'], ['NOK', 'NOK']]
        
        pass

    def testCase018(self):
        callkargs = {}
        self._call += " DEFAULT "
        ret = self.sx.callit(self._call,**callkargs)
        assert ret ==   [0, ['arbitrary output'], []]
        pass

#
#######################
#
 
if __name__ == '__main__':
    unittest.main()

