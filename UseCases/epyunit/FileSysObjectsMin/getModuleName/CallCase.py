"""Get the caller name.
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
import os,sys

#
# set search for the call of 'myscript.sh'
from epyunit.FileSysObjectsMin import setUpperTreeSearchPath
setUpperTreeSearchPath(None,'UseCases')

import epyunit.FileSysObjectsMin

#
#######################
#

def _funcDummyLvl0(sx=1):
    return (epyunit.FileSysObjectsMin.getCallerModuleName(sx), None, )

def _funcDummyLvl1(sx=1):
    return (epyunit.FileSysObjectsMin.getCallerModuleName(sx), _funcDummyLvl0(sx+1), )

def _funcDummyLvl2(sx=1):
    return (epyunit.FileSysObjectsMin.getCallerModuleName(sx), _funcDummyLvl1(sx+1), )

def _funcDummyLvl3(sx=1):
    return (epyunit.FileSysObjectsMin.getCallerModuleName(sx), _funcDummyLvl2(sx+1), )


class CallUnits(unittest.TestCase):
    name=os.path.curdir+__file__

    output=True
    output=False

    def testCase000(self):
        ret = epyunit.FileSysObjectsMin.getCallerModuleName()
        retx =  'UseCases.epyunit.FileSysObjectsMin.getModuleName.CallCase'
        assert retx == ret

    def testCase010(self):
        ret = _funcDummyLvl0()
        retx =  ('UseCases.epyunit.FileSysObjectsMin.getModuleName.CallCase', None)
        assert retx == ret

    def testCase011(self):
        ret = _funcDummyLvl1()
        retx = ('UseCases.epyunit.FileSysObjectsMin.getModuleName.CallCase', ('UseCases.epyunit.FileSysObjectsMin.getModuleName.CallCase', None))
        assert retx == ret

    def testCase012(self):
        ret = _funcDummyLvl2()
        retx = ('UseCases.epyunit.FileSysObjectsMin.getModuleName.CallCase', ('UseCases.epyunit.FileSysObjectsMin.getModuleName.CallCase', ('UseCases.epyunit.FileSysObjectsMin.getModuleName.CallCase', None)))
        assert retx == ret

    def testCase013(self):
        ret = _funcDummyLvl3()
        retx = ('UseCases.epyunit.FileSysObjectsMin.getModuleName.CallCase', ('UseCases.epyunit.FileSysObjectsMin.getModuleName.CallCase', ('UseCases.epyunit.FileSysObjectsMin.getModuleName.CallCase', ('UseCases.epyunit.FileSysObjectsMin.getModuleName.CallCase', None))))
        assert retx == ret

#
#######################
#

if __name__ == '__main__':
    unittest.main()

