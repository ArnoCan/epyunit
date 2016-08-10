"""
Case for a testee with result: failure: NOK
 
   EXIT:
     0
   STDOUT:
     arbitrary output
     arbitrary output
   STDERR:
     arbitrary signalling ERROR string
 
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
        ret = sx.callit(myscript+" NOK")
        assert ret[0] == 0
        assert ret[1] == ["fromB", 'arbitrary output', 'arbitrary output']
        assert ret[2] == ['arbitrary signalling ERROR string']

        _repr = repr(sx)
        _reprX = """{'bufsize': 16384, 'console': cli, 'emptyiserr': False, 'errasexcept': False, 'myexe': _mode_batch, 'passerr': False, 'proceed': doit, 'raw': False, 'useexit': True, 'usestderr': False}"""
        assert _repr == _reprX 
        pass
 
 
#
#######################
#
 
if __name__ == '__main__':
    unittest.main()

