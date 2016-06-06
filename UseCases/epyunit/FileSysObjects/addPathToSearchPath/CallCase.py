"""Check search of a relative filepathname - side-branch - in upper tree.
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

# 
# forDebug0 = sys.path
# print
# for i in  forDebug0:
#     print(i)

#from epyunit.SystemCalls import SystemCalls
import epyunit.SystemCalls

#
# set search for the call of 'myscript.sh'
from filesysobjects.FileSysObjects import setUpperTreeSearchPath
# forDebug1 = sys.path
# print
# for i in  forDebug1:
#     print(i)
setUpperTreeSearchPath(None,'epyunit')
# forDebug2 = sys.path
# print
# for i in  forDebug2:
#     print(i)


from filesysobjects.FileSysObjects import addPathToSearchPath
from filesysobjects.FileSysObjects import findRelPathInUpperTree
from epyunit.SystemCalls import SystemCalls



#
#######################
#

class CallUnits(unittest.TestCase):
    name=os.path.curdir+__file__

    output=True
    output=False

    def testCase000(self):
        sx = SystemCalls(**{"proceed":"trace",'raw':True})
        epy = "epyunit"
        mys = findRelPathInUpperTree("myscript.sh",os.path.dirname(os.path.abspath(__file__)),'epyunit',**{'matchcnt':0})

        addPathToSearchPath("bin")

        _env = os.environ.copy()
        _env['PATH'] = os.pathsep.join(sys.path) + os.pathsep + _env['PATH'] 

        _thecall = epy+" --pass-through "+mys+" xOK"
        ret = sx.callit(_thecall,**{'env': _env} )

        if ret[0] == 126:
            print("check exec permissions of 'myscript.sh'", file=sys.stderr)

        assert ret[1] == "arbitrary output\n" #raw-mode
        assert ret[0] == 123
        assert ret[2] == ""
        pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()

