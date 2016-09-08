from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import unittest
import os

from testdata import call_scripy,epyu

import epyunit.SubprocUnit

from filesysobjects.FileSysObjects import setUpperTreeSearchPath,findRelPathInSearchPath
import epyunit.SystemCalls

#
#######################
#
class CallUnits(unittest.TestCase):

    def __init__(self,*args,**kargs):
        super(CallUnits,self).__init__(*args,**kargs)

    @classmethod
    def setUpClass(cls):
        syskargs = {}
        cls.sx = epyunit.SubprocUnit.SubprocessUnit(**syskargs)

        #
        # wrapper call
        cls._call  = epyu
        cls._call += " --raw "
        cls._call += " --rdbg "
        cls._call += " --pderd_unit_self "
        cls._call += " -- "
        cls._call += call_scripy

    def setUp(self):
        syskargs = {}
        syskargs['emptyiserr'] = True


    def testCase010(self):
        _call  = self._call
        _call += " OK "
        ret = self.sx.callit(_call);
        ret[1]=[ lx.replace('\r','') for lx in ret[1] ]
        ret[2]=[ lx.replace('\r','') for lx in ret[2] ]
        retX = [
            0,
            ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'],
            ['RDBG:init:pydevrdc', 'RDBG:found pydevd.py', 'RDBG:debug started'],
        ]
        self.assertEqual(ret, retX)
        pass

    def testCase011(self):
        _call  = self._call
        _call += " NOK "
        ret = self.sx.callit(_call)
        ret[1]=[ lx.replace('\r','') for lx in ret[1] ]
        ret[2]=[ lx.replace('\r','') for lx in ret[2] ]
        retX = [
            0,
            ['fromB', 'arbitrary output', 'arbitrary output'],
            ['RDBG:init:pydevrdc', 'RDBG:found pydevd.py', 'RDBG:debug started', 'arbitrary signalling ERROR string'],
        ]
        self.assertEqual(ret, retX)
        pass

    def testCase012(self):
        _call  = self._call
        _call += " PRIO "
        ret = self.sx.callit(_call)
        ret[1]=[ lx.replace('\r','') for lx in ret[1] ]
        ret[2]=[ lx.replace('\r','') for lx in ret[2] ]
        retX = [
            0,
            ['fromC', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'],
            ['RDBG:init:pydevrdc', 'RDBG:found pydevd.py', 'RDBG:debug started', 'arbitrary signalling ERROR string'],
        ]
        self.assertEqual(ret, retX)
        pass

    def testCase013(self):
        _call  = self._call
        _call += " EXITOK "
        ret = self.sx.callit(_call)
        ret[1]=[ lx.replace('\r','') for lx in ret[1] ]
        ret[2]=[ lx.replace('\r','') for lx in ret[2] ]
        retX = [
            0,
            ['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'],
            ['RDBG:init:pydevrdc', 'RDBG:found pydevd.py', 'RDBG:debug started'],
        ]
        self.assertEqual(ret, retX)
        pass

    def testCase014(self):
        _call  = self._call
        _call += " EXITNOK "
        ret = self.sx.callit(_call)
        ret[1]=[ lx.replace('\r','') for lx in ret[1] ]
        ret[2]=[ lx.replace('\r','') for lx in ret[2] ]
        retX = [
            1,
            ['fromE', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'],
            ['RDBG:init:pydevrdc', 'RDBG:found pydevd.py', 'RDBG:debug started'],
        ]
        self.assertEqual(ret, retX)
        pass

    def testCase015(self):
        _call  = self._call
        _call += " EXIT7 "
        ret = self.sx.callit(_call)
        ret[1]=[ lx.replace('\r','') for lx in ret[1] ]
        ret[2]=[ lx.replace('\r','') for lx in ret[2] ]
        retX = [
            7,
            ['fromF', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'],
            ['RDBG:init:pydevrdc', 'RDBG:found pydevd.py', 'RDBG:debug started'],
        ]
        self.assertEqual(ret, retX)
        pass

    def testCase016(self):
        _call  = self._call
        _call += " EXIT8 "
        ret = self.sx.callit(_call)
        ret[1]=[ lx.replace('\r','') for lx in ret[1] ]
        ret[2]=[ lx.replace('\r','') for lx in ret[2] ]
        retX = [
            8,
            ['fromG', 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output'],
            ['RDBG:init:pydevrdc', 'RDBG:found pydevd.py', 'RDBG:debug started','arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output'],
        ]
        self.assertEqual(ret, retX)
        pass

    def testCase017(self):
        _call  = self._call
        _call += " EXIT9OK3NOK2 "
        ret = self.sx.callit(_call)
        ret[1]=[ lx.replace('\r','') for lx in ret[1] ]
        ret[2]=[ lx.replace('\r','') for lx in ret[2] ]
        retX = [
            9,
            ['fromH', 'OK', 'OK', 'OK'],
            ['RDBG:init:pydevrdc', 'RDBG:found pydevd.py', 'RDBG:debug started', 'NOK', 'NOK'],
        ]
        self.assertEqual(ret, retX)
        pass

    def testCase018(self):
        _call  = self._call
        _call += " DEFAULT "
        ret = self.sx.callit(_call)
        ret[1]=[ lx.replace('\r','') for lx in ret[1] ]
        ret[2]=[ lx.replace('\r','') for lx in ret[2] ]
        retX = [
            123,
            ['arbitrary output'],
            ['RDBG:init:pydevrdc', 'RDBG:found pydevd.py', 'RDBG:debug started'],
        ]
        self.assertEqual(ret, retX)
        pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()

