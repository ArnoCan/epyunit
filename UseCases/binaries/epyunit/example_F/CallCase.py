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
import os,sys

#
# set search for the call of 'myscript.sh'
from filesysobjects.FileSysObjects import setUpperTreeSearchPath
setUpperTreeSearchPath(os.path.dirname(__file__),'UseCases')


from epyunit.SystemCalls import SystemCalls

#
#######################
#

class CallUnits(unittest.TestCase):
    name=os.path.curdir+__file__

    output=True
    output=False

    def testCase000(self):
        sx = SystemCalls()
        # use PATH for search of 'myscript.sh'
        _env = os.environ.copy()
        _env['PATH'] = os.pathsep.join(sys.path)
         
        ret = sx.callit("myscript.sh EXIT7",**{'env': _env} )

        if ret[0] == 126:
            print("check exec permissions of 'myscript.sh'", file=sys.stderr)

        assert ret[1] == ['arbitrary output','arbitrary signalling NOK string','arbitrary output']
        assert ret[0] == 7
        assert ret[2] == []
        pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()
