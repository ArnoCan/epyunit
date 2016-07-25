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

class CallUnits(unittest.TestCase):
    name=os.path.curdir+__file__

    output=True
    output=False

    def testCase000(self):
        ret = epyunit.FileSysObjectsMin.getSourceFuncName()
        retx = 'testCase000'
        assert retx == ret

    def testCase001(self):
        ret = epyunit.FileSysObjectsMin.getSourceFuncName(1)
        retx = 'testCase001'
        assert retx == ret

    def testCase002(self):
        ret = epyunit.FileSysObjectsMin.getSourceFuncName(2)
        retx = 'run'
        assert retx == ret

    def testCase003(self):
        ret = epyunit.FileSysObjectsMin.getSourceFuncName(3)
        retx = '__call__'
        assert retx == ret

    def testCase004(self):
        ret = epyunit.FileSysObjectsMin.getSourceFuncName(4)
        retx = '_wrapped_run'
        assert retx == ret

#
#######################
#

if __name__ == '__main__':
    unittest.main()
