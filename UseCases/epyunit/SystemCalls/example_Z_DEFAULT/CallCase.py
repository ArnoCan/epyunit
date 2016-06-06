"""example_DEFAULT

Case for a testee with default failure, exit 123: DEFAULT

   EXIT:
     123
   STDOUT:
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
setUpperTreeSearchPath(None,'UseCases')


from epyunit.SystemCalls import SystemCalls

#
#######################
#

class CallUnits(unittest.TestCase):
    name=os.path.curdir+__file__

    output=True
    output=False

    def testCase000(self):
        """Call first selftest part.
        """
        
        sx = SystemCalls()
        # use PATH for search of 'myscript.sh'
        _env = os.environ.copy()
        _env['PATH'] = os.pathsep.join(sys.path)
         
        ret = sx.callit("myscript.sh",**{'env': _env} )

        if ret[0] == 126:
            print("check exec permissions of 'myscript.sh'", file=sys.stderr)

        assert ret[1] == ['arbitrary output']
        assert ret[0] == 123
        assert ret[2] == []
        pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()


# import unittest
#    2 import doctest
#    3
#    4 class DeviceTest( unittest.TestCase ):
#    5     # This is a simple test that just tries to load the module
#    6     def runTest( self ):
#    7         try:
#    8             import examp
#    9         except ImportError, e:
#   10             self.Fail( str( e ) )
