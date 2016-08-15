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
 
import unittest
import os,sys
 
from filesysobjects.FileSysObjects import setUpperTreeSearchPath,findRelPathInSearchPath
import epyunit.SystemCalls 

#
#######################
#
slst = []
setUpperTreeSearchPath(os.path.abspath(os.path.dirname(__file__)),'epyunit',slst)

epyu = findRelPathInSearchPath('bin/epyunit',slst,matchidx=0)

class CallUnits(unittest.TestCase):

    def testCase010(self):
        """Simple call, providing a return value only.
        """
        _call  = epyu + " --selftest "
        _call  += " --rdbg "
        _call  += " --rdbg-forward all "
        #_call  += " --pderd_debug_self "

        syskargs = {}
        sx = epyunit.SystemCalls.SystemCalls(**syskargs)

        callkargs = {}
        ret = sx.callit(_call,**callkargs)

        assert ret[0] == 0 
        retX = [0, [], []]
        self.assertEqual(retX, ret)
 
    def testCase020(self):
        """Simple call, but with verbose flag for some output filtering.
        """
        _call  = epyu + " -v --selftest "

        syskargs = {}
        sx = epyunit.SystemCalls.SystemCalls(**syskargs)

        callkargs = {}
        ret = sx.callit(_call,**callkargs)

        assert ret[0] == 0
        retX = [
            0, 
            [
                '#*** epyunit/myscript.sh DEFAULT ***', 
                '', 
                '#*** epyunit/myscript.sh OK ***', 
                '', 
                '#*** epyunit/myscript.sh PRIO ***', 
                '', 
                '#*** epyunit/myscript.sh EXITOK ***', 
                '', 
                '#*** epyunit/myscript.sh EXITNOK ***', 
                '', 
                '#*** epyunit/myscript.sh EXIT7 ***', 
                '', 
                '#*** epyunit/myscript.sh EXIT8 ***', 
                '', 
                '#*** epyunit/myscript.sh DEFAULT ***', 
                '', 
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
                '#*** epyunit/myscript.py DEFAULT ***',
            ],                
            []
        ]
        #retX[1] = [ x for x in retX[1] if x!='']

        self.assertEqual(retX[1], ret[1])
        self.assertEqual(retX[2], [])

#
#######################
#
 
if __name__ == '__main__':
    unittest.main()

