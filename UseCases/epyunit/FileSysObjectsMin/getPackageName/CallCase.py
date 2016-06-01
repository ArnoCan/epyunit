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

def _funcDummyLvl0(sx=2):
    return (epyunit.FileSysObjectsMin.getCallerPackageName(sx), None, )

def _funcDummyLvl1(sx=1):
    return (epyunit.FileSysObjectsMin.getCallerPackageName(sx), _funcDummyLvl0(sx+1), )

def _funcDummyLvl2(sx=1):
    return (epyunit.FileSysObjectsMin.getCallerPackageName(sx), _funcDummyLvl1(sx+1), )

def _funcDummyLvl3(sx=1):
    return (epyunit.FileSysObjectsMin.getCallerPackageName(sx), _funcDummyLvl2(sx+1), )


class CallUnits(unittest.TestCase):
    name=os.path.curdir+__file__

    output=True
    output=False

    def testCase000(self):
        ret = epyunit.FileSysObjectsMin.getCallerPackageName()
        retx = None 
        assert retx == ret

    def testCase001(self):
        ret = epyunit.FileSysObjectsMin.getCallerPackageName(1)
        retx = None 
        assert retx == ret

    def testCase002(self):
        ret = epyunit.FileSysObjectsMin.getCallerPackageName(2)
        retx = 'unittest' 
        assert retx == ret

    def testCase003(self):
        ret = epyunit.FileSysObjectsMin.getCallerPackageName(3)
        retx = 'unittest' 
        assert retx == ret

    def testCase004(self):
        ret = epyunit.FileSysObjectsMin.getCallerPackageName(4)
        retx = 'unittest2' 
        assert retx == ret

    def testCase009(self):
        ret = epyunit.FileSysObjectsMin.getCallerPackageName(9)
        retx = 'unittest2' 
        assert retx == ret


#
#######################
#

if __name__ == '__main__':
    unittest.main()

