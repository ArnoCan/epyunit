"""Check defaults.
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
        """Check defaults.
        """

        start = None
        top = None
        res = []
        ret = setUpperTreeSearchPath(start,top,res) #@UnusedVariable
        
        resx = [
            os.path.abspath(os.path.dirname(__file__)),
        ]

        assert resx == res
        pass

if __name__ == '__main__':
    unittest.main()
