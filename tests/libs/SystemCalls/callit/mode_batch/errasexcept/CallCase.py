from __future__ import absolute_import
#from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import unittest
import os,sys
from cStringIO import StringIO

from testdata import call_scripy

import epyunit.SystemCalls 

from filesysobjects.FileSysObjects import setUpperTreeSearchPath,findRelPathInSearchPath

#
#######################
#
class CallUnits(unittest.TestCase):

    def __init__(self,*args,**kargs):
        super(CallUnits,self).__init__(*args,**kargs)

    @classmethod
    def setUpClass(cls):
        syskargs = {}
        syskargs['errasexcept'] = True

        cls.sx = epyunit.SystemCalls.SystemCalls(**syskargs)

    def setUp(self):
        syskargs = {}
        syskargs['emptyiserr'] = True

        # buffers for evaluation after intercepted exit.
        self.stdoutbuf=StringIO()
        self.stderrbuf=StringIO()
        self.stdout = sys.stdout
        self.stderr = sys.stderr

    def testCase010(self):
        _call  = call_scripy+" "
        _call += "OK"
        retX = [0, ["fromA", 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'],[]]
        callkargs = {}
        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, retX)

    def testCase011(self):
        _call  = call_scripy+" "
        _call += "NOK"
        retX = [0, ['fromB', 'arbitrary output', 'arbitrary output'], ['arbitrary signalling ERROR string']]
        callkargs = {}
        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, retX)
        pass

    def testCase012(self):
        _call  = call_scripy+" "
        _call += " PRIO "
        retX = [0, ['fromC', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], ['arbitrary signalling ERROR string']]
        callkargs = {}
        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, retX)
        pass

    def testCase013(self):
        _call  = call_scripy+" "
        _call += " EXITOK "
        retX = [0, ['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]
        callkargs = {}
        ret = self.sx.callit(_call,**callkargs)
        self.assertEqual(ret, retX)
        pass

    def testCase014(self):
        callkargs = {}
        _call  = call_scripy+" "
        _call += " EXITNOK "

        # passerr is going to call sys.exit,
        # thus cache output and intercept the exit
        sys.stdout = self.stdoutbuf
        sys.stderr = self.stderrbuf

        einfo = None
        try:
            ret = self.sx.callit(_call,**callkargs) #@UnusedVariable
        except:
            # save the exception
            einfo = sys.exc_info()
            pass

        # assure it is actually the sys.exit
        self.assertIsNotNone(einfo)
        assert einfo[0] == epyunit.SystemCalls.SystemCallsExceptionSubprocessError
        assert einfo[1].code== 1

        stdval = self.stdoutbuf.getvalue().replace('\r','')
        stdref = """fromE
arbitrary output
arbitrary signalling OK string
arbitrary output
""".replace('\r','')
        try:
            assert stdval == stdref
        except Exception as e:
            # switch back from stdout and stderr buffers
            sys.stdout = self.stdout
            sys.stderr = self.stderr
            raise e

        errval = self.stderrbuf.getvalue()
        errref = ""
        try:
            assert errval == errref
        except Exception as e:
            # switch back from stdout and stderr buffers
            sys.stdout = self.stdout
            sys.stderr = self.stderr
            raise e

        # switch back from stdout and stderr buffers
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        pass

    def testCase015(self):
        callkargs = {}
        _call  = call_scripy+" "
        _call += " EXIT7 "

        sys.stdout = self.stdoutbuf
        sys.stderr = self.stderrbuf

        einfo = None
        try:
            ret = self.sx.callit(_call,**callkargs) #@UnusedVariable
        except:
            einfo = sys.exc_info()
            pass

        # assure it is actually the sys.exit
        self.assertIsNotNone(einfo)
        assert einfo[0] == epyunit.SystemCalls.SystemCallsExceptionSubprocessError
        assert einfo[1].code== 7

        stdval = self.stdoutbuf.getvalue().replace('\r','')
        stdref = """fromF
arbitrary output
arbitrary signalling NOK string
arbitrary output
""".replace('\r','')
        try:
            assert stdval == stdref
        except Exception as e:
            sys.stdout = self.stdout
            sys.stderr = self.stderr
            raise e

        errval = self.stderrbuf.getvalue()
        errref = ""
        try:
            assert errval == errref
        except Exception as e:
            sys.stdout = self.stdout
            sys.stderr = self.stderr
            raise e

        sys.stdout = self.stdout
        sys.stderr = self.stderr
        pass


    def testCase016(self):
        callkargs = {}
        _call  = call_scripy+" "
        _call += " EXIT8 "

        sys.stdout = self.stdoutbuf
        sys.stderr = self.stderrbuf

        einfo = None
        try:
            ret = self.sx.callit(_call,**callkargs) #@UnusedVariable
        except:
            einfo = sys.exc_info()
            pass

        # assure it is actually the sys.exit
        self.assertIsNotNone(einfo)
        assert einfo[0] == epyunit.SystemCalls.SystemCallsExceptionSubprocessError
        assert einfo[1].code== 8

        stdval = self.stdoutbuf.getvalue().replace('\r','')
        stdref = """fromG
arbitrary output
arbitrary signalling NOK string
arbitrary output
""".replace('\r','')
        try:
            assert stdval == stdref
        except Exception as e:
            sys.stdout = self.stdout
            sys.stderr = self.stderr
            raise e

        errval = self.stderrbuf.getvalue().replace('\r','')
        errref = """arbitrary err output
arbitrary err signalling NOK string
arbitrary err output
""".replace('\r','')
        try:
            assert errval == errref
        except Exception as e:
            sys.stdout = self.stdout
            sys.stderr = self.stderr
            raise e

        sys.stdout = self.stdout
        sys.stderr = self.stderr
        pass

    def testCase017(self):
        callkargs = {}
        _call  = call_scripy+" "
        _call += " EXIT9OK3NOK2 "

        sys.stdout = self.stdoutbuf
        sys.stderr = self.stderrbuf

        einfo = None
        try:
            ret = self.sx.callit(_call,**callkargs) #@UnusedVariable
        except:
            einfo = sys.exc_info()
            pass

        # assure it is actually the sys.exit
        self.assertIsNotNone(einfo)
        assert einfo[0] == epyunit.SystemCalls.SystemCallsExceptionSubprocessError
        assert einfo[1].code== 9

        stdval = self.stdoutbuf.getvalue().replace('\r','')
        stdref = """fromH
OK
OK
OK
""".replace('\r','')
        try:
            assert stdval == stdref
        except Exception as e:
            sys.stdout = self.stdout
            sys.stderr = self.stderr
            raise e

        errval = self.stderrbuf.getvalue().replace('\r','')
        errref = """NOK
NOK
""".replace('\r','')
        try:
            assert errval == errref
        except Exception as e:
            sys.stdout = self.stdout
            sys.stderr = self.stderr
            raise e

        sys.stdout = self.stdout
        sys.stderr = self.stderr
        pass

    def testCase018(self):
        callkargs = {}
        _call  = call_scripy+" "
        _call += " DEFAULT "


        sys.stdout = self.stdoutbuf
        sys.stderr = self.stderrbuf

        einfo = None
        try:
            ret = self.sx.callit(_call,**callkargs) #@UnusedVariable
        except:
            einfo = sys.exc_info()
            pass

        # assure it is actually the sys.exit
        self.assertIsNotNone(einfo)
        assert einfo[0] == epyunit.SystemCalls.SystemCallsExceptionSubprocessError
        assert einfo[1].code== 123

        stdval = self.stdoutbuf.getvalue().replace('\r','')
        stdref = """arbitrary output
""".replace('\r','')
        try:
            assert stdval == stdref
        except Exception as e:
            sys.stdout = self.stdout
            sys.stderr = self.stderr
            raise e

        errval = self.stderrbuf.getvalue()
        errref = ""
        try:
            assert errval == errref
        except Exception as e:
            sys.stdout = self.stdout
            sys.stderr = self.stderr
            raise e

        sys.stdout = self.stdout
        sys.stderr = self.stderr
        pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()

