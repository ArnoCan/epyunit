from __future__ import absolute_import
from __future__ import print_function
from linecache import getline

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__='af90cc0c-de54-4a32-becd-06f5ce5a3a75'

__docformat__ = "restructuredtext en"

import unittest
import os,sys

import filesysobjects.FileSysObjects
import pysourceinfo.PySourceInfo


#
#######################
#


class CallUnits(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        self._s = sys.path[:]
        #
        # prefix from unchanged sys.path
        self.mySysPathPrefixRaw = pysourceinfo.PySourceInfo.getPythonPathFromSysPath(__file__) #@UnusedVariable

    def reset_sys_path(self):
        [ sys.path.pop() for x in range(len(sys.path)) ] #@UnusedVariable
        sys.path.extend(self._s)

    def testCase000_locate_perl(self):

        px = filesysobjects.FileSysObjects.findRelPathInSearchPath('perl',os.environ['PATH'])
        if not px:
            px = filesysobjects.FileSysObjects.findRelPathInSearchPath('perl.exe',os.environ['PATH'])

        if not px:
            self.skipTest("Missing perl")
        pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()

