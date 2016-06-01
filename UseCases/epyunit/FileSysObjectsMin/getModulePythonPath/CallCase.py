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

import epyunit.FileSysObjectsMin


#
#######################
#

class CallUnits(unittest.TestCase):
    name=os.path.curdir+__file__

    output=True
    output=False

    def testCase002(self):
        f2 = epyunit.FileSysObjectsMin.getCallerModuleFilePathName(2)

        p0 = epyunit.FileSysObjectsMin.getPythonPathPrefixMatchFromSysPath(f2)
        p1 = epyunit.FileSysObjectsMin.getCallerModulePythonPath(2)
        assert p0 == p1

    def testCase003(self):
        f3 = epyunit.FileSysObjectsMin.getCallerModuleFilePathName(2)

        p0 = epyunit.FileSysObjectsMin.getPythonPathPrefixMatchFromSysPath(f3)
        p1 = epyunit.FileSysObjectsMin.getCallerModulePythonPath(3)
        assert p0 == p1


#
#######################
#

if __name__ == '__main__':
    unittest.main()

