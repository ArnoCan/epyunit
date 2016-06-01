"""Pretty print self.data.
"""
from __future__ import absolute_import

import unittest
import os

from epyunit.FileSysObjectsMin import setUpperTreeSearchPath


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

        A = 'a/A.txt'         #@UnusedVariable
        B = 'a/b/B.txt'       #@UnusedVariable
        C = 'a/b/c/C.txt'     #@UnusedVariable
        D = 'a/b/c/d/D.txt'   #@UnusedVariable

        top = os.path.abspath(os.path.dirname(__file__))+os.sep  #@UnusedVariable
        start = top+A

        res = []
        ret = setUpperTreeSearchPath(start,top,res) #@UnusedVariable
        
        resx = [
            os.path.dirname(top+A)+os.sep,
            top,
        ]

        assert resx == res
        pass

    def testCase001(self):

        A = 'a/A.txt'         #@UnusedVariable
        B = 'a/b/B.txt'       #@UnusedVariable
        C = 'a/b/c/C.txt'     #@UnusedVariable
        D = 'a/b/c/d/D.txt'   #@UnusedVariable

        top = os.path.abspath(os.path.dirname(__file__))+os.sep
        start = top+B

        res = []
        ret = setUpperTreeSearchPath(start,top,res) #@UnusedVariable
        
        resx = [
            os.path.dirname(top+B)+os.sep,
            top,
        ]
        resx.insert(1,os.path.dirname(resx[0][:-1])+os.sep)

        assert resx == res
        pass

    def testCase002(self):

        A = 'a/A.txt'         #@UnusedVariable
        B = 'a/b/B.txt'       #@UnusedVariable
        C = 'a/b/c/C.txt'     #@UnusedVariable
        D = 'a/b/c/d/D.txt'   #@UnusedVariable

        top = os.path.abspath(os.path.dirname(__file__))+os.sep
        start = top+C

        res = []
        ret = setUpperTreeSearchPath(start,top,res) #@UnusedVariable
        
        resx = [
            os.path.dirname(top+C)+os.sep,
            top,
        ]
        resx.insert(1,os.path.dirname(resx[0][:-1])+os.sep)
        resx.insert(2,os.path.dirname(resx[1][:-1])+os.sep)

        assert resx == res
        pass

    def testCase003(self):

        A = 'a/A.txt'         #@UnusedVariable
        B = 'a/b/B.txt'       #@UnusedVariable
        C = 'a/b/c/C.txt'     #@UnusedVariable
        D = 'a/b/c/d/D.txt'   #@UnusedVariable

        top = os.path.abspath(os.path.dirname(__file__))+os.sep
        start = top+D

        res = []
        ret = setUpperTreeSearchPath(start,top,res) #@UnusedVariable
        
        resx = [
            os.path.dirname(top+D)+os.sep,
            top,
        ]
        resx.insert(1,os.path.dirname(resx[0][:-1])+os.sep)
        resx.insert(2,os.path.dirname(resx[1][:-1])+os.sep)
        resx.insert(3,os.path.dirname(resx[2][:-1])+os.sep)

        assert resx == res
        pass

if __name__ == '__main__':
    unittest.main()
