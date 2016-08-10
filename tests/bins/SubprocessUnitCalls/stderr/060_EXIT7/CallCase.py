"""example_F
 
Case for a testee with failure, exit 7: EXIT7
 
   EXIT:
     7
   STDOUT:
     arbitrary output
     arbitrary signalling NOK string
     arbitrary output
   STDERR:
     -
 
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
import os
 
from filesysobjects.FileSysObjects import setUpperTreeSearchPath,findRelPathInSearchPath
import epyunit.SystemCalls 
 
#
#######################
#
 
class CallUnits(unittest.TestCase):
    def testCase000(self):

        slst = []
        setUpperTreeSearchPath(os.path.abspath(os.path.dirname(__file__)),'epyunit',slst)
        myscript = findRelPathInSearchPath('epyunit/myscript.sh',slst,matchidx=0)

        sx = epyunit.SystemCalls.SystemCalls()

#         _env = os.environ.copy()
#         _env['PATH'] = os.pathsep.join(sys.path)
          
        ret = sx.callit(myscript+" EXIT7")

        assert ret[0] == 7
        assert ret[1] == ["fromF", 'arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output']
        assert ret[2] == []
        pass
 
 
#
#######################
#
 
if __name__ == '__main__':
    unittest.main()

