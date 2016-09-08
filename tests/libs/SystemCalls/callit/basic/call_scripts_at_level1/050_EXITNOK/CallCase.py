"""example_E

Case for a testee with failure, exit 1: EXITNOK

   EXIT:
     1
   STDOUT:
     arbitrary output
     arbitrary signalling OK string
     arbitrary output
   STDERR:
     -

"""
from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.2.0'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import unittest

from testdata import call_scripy

import epyunit.SystemCalls

#
#######################
#

class CallUnits(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.sx = epyunit.SystemCalls.SystemCalls()
        pass

    def testCase000(self):
        _call  = call_scripy+" "
        _call += "EXITNOK"
        retX = [
            1,
            ["fromE", 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'],
            []
        ]

        ret = self.sx.callit(_call)
        self.assertEqual(ret, retX)

        _repr = repr(self.sx)
        import sys
        if sys.platform in ('win32'):
            _reprX = """{'bufsize': 16384, 'console': cli, 'emptyiserr': False, 'errasexcept': False, 'myexe': _mode_batch_win, 'passerr': False, 'proceed': doit, 'raw': False, 'useexit': True, 'usestderr': False}"""
        else:
            _reprX = """{'bufsize': 16384, 'console': cli, 'emptyiserr': False, 'errasexcept': False, 'myexe': _mode_batch_posix, 'passerr': False, 'proceed': doit, 'raw': False, 'useexit': True, 'usestderr': False}"""
        self.assertEqual(_repr, _reprX)
        pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()

