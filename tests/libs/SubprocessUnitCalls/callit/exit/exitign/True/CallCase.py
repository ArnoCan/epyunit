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
        self.sx = epyunit.SubprocUnit.SubprocessUnit(**syskargs)

        self._call = self.scri
        
        self.callkargs = {}
        self.applyargs = {}
        self.applyargs['exitign'] = True

    def testCase010(self):
        self._call += " OK "
        
        # call subprocess
        ret = self.sx.callit(self._call,**self.callkargs)
        assert ret ==  [0, ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        # update rules for next match
        status = self.sx.getruleset().setrules(**self.applyargs)
        assert status

        # perform next match
        status = self.sx.apply(ret)
        assert status
        pass

    def testCase011(self):
        self._call += " NOK "

        # call subprocess
        ret = self.sx.callit(self._call,**self.callkargs)
        assert ret ==  [0, ['fromB', 'arbitrary output', 'arbitrary output'], ['arbitrary signalling ERROR string']]

        # update rules for next match
        status = self.sx.getruleset().setrules(**self.applyargs)
        assert status

        # perform next match
        status = self.sx.apply(ret)
        assert status
        pass

    def testCase012(self):
        self._call += " PRIO "

        # call subprocess
        ret = self.sx.callit(self._call,**self.callkargs)
        assert ret ==   [0, ['fromC', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], ['arbitrary signalling ERROR string']]

        # update rules for next match
        status = self.sx.getruleset().setrules(**self.applyargs)
        assert status

        # perform next match
        status = self.sx.apply(ret)
        assert status
        pass

    def testCase013(self):
        self._call += " EXITOK "

        # call subprocess
        ret = self.sx.callit(self._call,**self.callkargs)
        assert ret ==  [0, ['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        # update rules for next match
        status = self.sx.getruleset().setrules(**self.applyargs)
        assert status

        # perform next match
        status = self.sx.apply(ret)
        assert status
        pass

    def testCase014(self):
        self._call += " EXITNOK "

        # call subprocess
        ret = self.sx.callit(self._call,**self.callkargs)
        assert ret ==   [1, ['fromE', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]

        # update rules for next match
        status = self.sx.getruleset().setrules(**self.applyargs)
        assert status

        # perform next match
        status = self.sx.apply(ret)
        assert status
        pass

    def testCase015(self):
        self._call += " EXIT7 "

        # call subprocess
        ret = self.sx.callit(self._call,**self.callkargs)
        assert ret ==   [7, ['fromF', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], []]

        # update rules for next match
        status = self.sx.getruleset().setrules(**self.applyargs)
        assert status

        # perform next match
        status = self.sx.apply(ret)
        assert status
        pass

    def testCase016(self):
        self._call += " EXIT8 "

        # call subprocess
        ret = self.sx.callit(self._call,**self.callkargs)
        assert ret ==   [8, ['fromG', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'], ['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']]

        # update rules for next match
        status = self.sx.getruleset().setrules(**self.applyargs)
        assert status

        # perform next match
        status = self.sx.apply(ret)
        assert status
        pass

    def testCase017(self):
        self._call += " EXIT9OK3NOK2 "

        # call subprocess
        ret = self.sx.callit(self._call,**self.callkargs)
        assert ret ==  [9, ['fromH', 'OK', 'OK', 'OK'], ['NOK', 'NOK']]

        # update rules for next match
        status = self.sx.getruleset().setrules(**self.applyargs)
        assert status

        # perform next match
        status = self.sx.apply(ret)
        assert status
        pass

    def testCase018(self):
        self._call += " DEFAULT "

        # call subprocess
        ret = self.sx.callit(self._call,**self.callkargs)
        assert ret ==   [123, ['arbitrary output'], []]

        # update rules for next match
        status = self.sx.getruleset().setrules(**self.applyargs)
        assert status

        # perform next match
        status = self.sx.apply(ret)
        assert status
        pass

#
#######################
#
 
if __name__ == '__main__':
    unittest.main()

