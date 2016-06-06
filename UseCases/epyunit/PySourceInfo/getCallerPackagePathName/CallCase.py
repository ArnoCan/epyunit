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

# _4test=sys.path
# for i in sys.path:
#     print("4TEST: "+str(i))

import filesysobjects.FileSysObjects
#
# prefix from unchanged sys.path
mySysPathPrefixRaw = filesysobjects.PySourceInfo.getPythonPathPrefixMatchFromSysPath(__file__)


#
# set search for the call of 'myscript.sh'
from filesysobjects.FileSysObjects import setUpperTreeSearchPath
setUpperTreeSearchPath(None,'UseCases')


#
#######################
#


class CallUnits(unittest.TestCase):
    name=os.path.curdir+__file__

    output=True
    output=False

    def testCase000(self):
        global mySysPathPrefix

        ppn = filesysobjects.PySourceInfo.getCallerPackagePathName()
        assert ppn == None
        pass

    def testCase001(self):
        global mySysPathPrefix

        ppn = filesysobjects.PySourceInfo.getCallerPackagePathName(1)
        assert ppn == None
        pass

    def testCase002(self):
        global mySysPathPrefix

        ppn = filesysobjects.PySourceInfo.getCallerPackagePathName(2)
        assert ppn == "/usr/lib64/python2.7/unittest"
        pass

    def testCase003(self):
        global mySysPathPrefix

        ppn = filesysobjects.PySourceInfo.getCallerPackagePathName(3)
        assert ppn == "/usr/lib64/python2.7/unittest"
        pass

    def testCase009(self):
        global mySysPathPrefix

        ppn = filesysobjects.PySourceInfo.getCallerPackagePathName(9)
        assert ppn == "/usr/lib/python2.7/site-packages/unittest2"
        pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()

