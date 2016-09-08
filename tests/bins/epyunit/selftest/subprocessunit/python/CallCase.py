"""
Selftest with 'epyunit.SystemCall' wrapper.

"""
from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import sys
from cStringIO import StringIO
import unittest

from testdata import epyu

import epyunit.SystemCalls


#
#######################
#

class CallUnits(unittest.TestCase):


    def __init__(self,*args,**kargs):
        super(CallUnits,self).__init__(*args,**kargs)

    @classmethod
    def setUpClass(cls):
        syskargs = {}
        cls.sx = epyunit.SystemCalls.SystemCalls(**syskargs)

        # buffers for evaluation after intercepted exit.
        cls.stdoutbuf=StringIO()
        cls.stderrbuf=StringIO()
        cls.stdout = sys.stdout
        cls.stderr = sys.stderr

    def setUp(self):
        syskargs = {}
        syskargs['emptyiserr'] = True

    def testCase010(self):
        """Simple call, providing a return value only.
        """
        _call  = epyu + " "
        _call  += " --selftest "

        retX = [0, [], []]
        callkargs = {}
        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, retX)

    def testCase020(self):
        """Simple call, but with verbose flag for some output filtering.
        """
        _call  = epyu + " "
        _call  += " -v "
        _call  += " --selftest "
        _call  += " --slang=python "

        retX = [
            0,
            [
                '#*** epyunit/myscript.py DEFAULT ***',
                '',
                '#*** epyunit/myscript.py OK ***',
                '',
                '#*** epyunit/myscript.py PRIO ***',
                '',
                '#*** epyunit/myscript.py EXITOK ***',
                '',
                '#*** epyunit/myscript.py EXITNOK ***',
                '',
                '#*** epyunit/myscript.py EXIT7 ***',
                '',
                '#*** epyunit/myscript.py EXIT8 ***',
                '',
                '#*** epyunit/myscript.py EXIT9OK3NOK2 ***',
                '',
                '#*** epyunit/myscript.py STDERRONLY ***',
                '',
                '#*** epyunit/myscript.py DEFAULT ***'
            ],
            []
        ]
        #retX[1] = [ x for x in retX[1] if x!='']
        callkargs = {}
        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, retX)

if __name__ == '__main__':
    unittest.main()

