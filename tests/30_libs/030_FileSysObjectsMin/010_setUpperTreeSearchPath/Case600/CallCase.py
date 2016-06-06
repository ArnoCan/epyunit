"""Check error condition.
"""
from __future__ import absolute_import

import unittest
import os

from filesysobjects.FileSysObjects import setUpperTreeSearchPath,FileSysObjectsException


#
#######################
#
class CallUnits(unittest.TestCase):
    name=os.path.curdir+__file__

    output=True
    output=False

    #
    # Create by object
    #
    def testCase000(self):
        """Check error condition.
        """
        A = 'a/A.txt'        #@UnusedVariable
        B = 'a/b/B.txt'      #@UnusedVariable
        C = 'a/b/c/C.txt'    #@UnusedVariable
        D = 'a/b/c/d/D.txt'  #@UnusedVariable

        start = None
        top = ''
        res = []
        try:
            ret = setUpperTreeSearchPath(start,top,res) #@UnusedVariable
        except FileSysObjectsException:
            pass
        else:
            raise
        pass

    def testCase001(self):
        """Check error condition.
        """
        A = 'a/A.txt'        #@UnusedVariable
        B = 'a/b/B.txt'      #@UnusedVariable
        C = 'a/b/c/C.txt'    #@UnusedVariable
        D = 'a/b/c/d/D.txt'  #@UnusedVariable

        start = ''
        top = None
        res = []
        try:
            ret = setUpperTreeSearchPath(start,top,res) #@UnusedVariable
        except FileSysObjectsException:
            pass
        else:
            raise
        pass

if __name__ == '__main__':
    unittest.main()
