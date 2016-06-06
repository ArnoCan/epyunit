"""Check the expansion of 'sys.path' by PATH components derived from splice of upper tree.
"""
from __future__ import absolute_import

import unittest
import os

from filesysobjects.FileSysObjects import setUpperTreeSearchPath


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

        top = os.path.abspath(os.path.dirname(__file__))  #@UnusedVariable
        start = top+os.sep+A

        res = []
        ret = setUpperTreeSearchPath(start,top,res) #@UnusedVariable
        
        resx = [
            os.path.dirname(top+os.sep+A),
            top,
        ]

        assert resx == res
        pass

    def testCase001(self):

        A = 'a/A.txt'         #@UnusedVariable
        B = 'a/b/B.txt'       #@UnusedVariable
        C = 'a/b/c/C.txt'     #@UnusedVariable
        D = 'a/b/c/d/D.txt'   #@UnusedVariable

        top = os.path.abspath(os.path.dirname(__file__))
        start = top+os.sep+B

        res = []
        ret = setUpperTreeSearchPath(start,top,res) #@UnusedVariable
        
        resx = [
            os.path.dirname(top+os.sep+B),
            top,
        ]
        resx.insert(1,os.path.dirname(resx[0][:-1]))

        assert resx == res
        pass

    def testCase002(self):

        A = 'a/A.txt'         #@UnusedVariable
        B = 'a/b/B.txt'       #@UnusedVariable
        C = 'a/b/c/C.txt'     #@UnusedVariable
        D = 'a/b/c/d/D.txt'   #@UnusedVariable

        top = os.path.abspath(os.path.dirname(__file__))
        start = top+os.sep+C

        res = []
        ret = setUpperTreeSearchPath(start,top,res) #@UnusedVariable
        
        resx = [
            os.path.dirname(top+os.sep+C),
            top,
        ]
        resx.insert(1,os.path.dirname(resx[0][:-1]))
        resx.insert(2,os.path.dirname(resx[1][:-1]))

        assert resx == res
        pass

    def testCase003(self):

        A = 'a/A.txt'         #@UnusedVariable
        B = 'a/b/B.txt'       #@UnusedVariable
        C = 'a/b/c/C.txt'     #@UnusedVariable
        D = 'a/b/c/d/D.txt'   #@UnusedVariable

        top = os.path.abspath(os.path.dirname(__file__))
        start = top+os.sep+D

        res = []
        ret = setUpperTreeSearchPath(start,top,res) #@UnusedVariable
        
        resx = [
            os.path.dirname(top+os.sep+D),
            top,
        ]
        resx.insert(1,os.path.dirname(resx[0][:-1]))
        resx.insert(2,os.path.dirname(resx[1][:-1]))
        resx.insert(3,os.path.dirname(resx[2][:-1]))

        assert resx == res
        pass

if __name__ == '__main__':
    unittest.main()
