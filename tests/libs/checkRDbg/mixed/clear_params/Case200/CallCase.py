# -*- coding: utf-8 -*-
from __future__ import absolute_import

import unittest
import os,sys

from testdata import epyu,call_scripy

try:
    from epyunit.debug.checkRDbg import checkRDbg,checkAndRemoveRDbgOptions,setDefaults
except Exception as e:
    print "\n#\n#*** Set 'PYTHONPATH' ("+str(e)+")\n#\n"
    sys.exit(1)

import shlex

#
#######################
#
class CallUnits(unittest.TestCase):
    
    def __init__(self,*args,**kargs):
        super(CallUnits,self).__init__(*args,**kargs)

    def setUp(self):
        self._optstring4 = "python mycall --opt1 --rdbg host0:1111 --opt2=val1 --opt3 val3 --rdbg-root /my/root --opt4 --rdbg-sub sub/a --opt5 --rdbg-forward 2 arg0 arg1 arg2 "
        setDefaults()

    def testCall050_CheckRdbgStr(self):
        """Selftest for removeal of cli parts.
        """
        cr0 = checkRDbg(self._optstring4)
        assert cr0 == True

    def testCall051_CheckRdbgList(self):
        """Selftest for removeal of cli parts.
        """
        lst = shlex.split(self._optstring4)
        cr0 = checkRDbg(lst)
        assert cr0 == True

    def testCall052_ClearOptionAndValue(self):
        """Selftest for removeal of cli parts.
        """
        lst = shlex.split(self._optstring4)
        cr0 = checkAndRemoveRDbgOptions(lst)
        cr0ref = (True, 'host0:1111', 1, '/my/root', 'sub/a',)
        assert cr0ref == cr0

        cr1ref = shlex.split("python mycall --opt1 --opt2=val1 --opt3 val3 --opt4 --opt5 arg0 arg1 arg2 ")
        assert cr1ref == lst

#
#######################
#
if __name__ == '__main__':
    unittest.main()
