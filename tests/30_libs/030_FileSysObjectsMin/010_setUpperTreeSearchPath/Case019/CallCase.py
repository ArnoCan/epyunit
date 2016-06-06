"""Check defaults.
"""
from __future__ import absolute_import

import unittest
import os

from filesysobjects.PySourceInfo import getPythonPathRel
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
        """Check defaults.
        """

        start = os.path.dirname(__file__)
        top = 'tests'
        _res = []
        ret = setUpperTreeSearchPath(start,top,_res) #@UnusedVariable
        
        import sys
        forDebugOnly = sys.path
        
        res = []
        for i in range(len(_res)):
            res.append(getPythonPathRel(_res[i])) 
        resx = [
            '30_libs/030_FileSysObjectsMin/010_setUpperTreeSearchPath/Case019', 
            '30_libs/030_FileSysObjectsMin/010_setUpperTreeSearchPath', 
            '30_libs/030_FileSysObjectsMin', 
            '30_libs', 
            ''
        ]                

        assert resx == res
        pass

if __name__ == '__main__':
    unittest.main()
