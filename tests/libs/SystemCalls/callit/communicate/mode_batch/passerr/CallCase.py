from __future__ import absolute_import
#from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import os,sys
version = '{0}.{1}'.format(*sys.version_info[:2])
if version in ('2.6',): # pragma: no cover
    import unittest2 as unittest
elif version in ('2.7',): # pragma: no cover
    import unittest
else:
    sys.exit(1)

from cStringIO import StringIO

from testdata import call_scripy
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
        syskargs['passerr'] = True

        cls.sx = epyunit.SystemCalls.SystemCalls(**syskargs)
        cls.scri = call_scripy

    def setUp(self):

        # buffers for evaluation after intercepted exit.
        self.stdoutbuf=StringIO()
        self.stderrbuf=StringIO()
        self.stdout = sys.stdout
        self.stderr = sys.stderr

    def testCase010(self):
        callkargs = {}
        _call  = self.scri
        _call += " OK "

        ret = self.sx.callit(_call,**callkargs)
        assert ret ==  [0, ['fromA', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]
        pass

    def testCase011(self):
        callkargs = {}
        _call  = self.scri
        _call += " NOK "

        ret = self.sx.callit(_call,**callkargs)
        assert ret ==  [0, ['fromB', 'arbitrary output', 'arbitrary output'], ['arbitrary signalling ERROR string']]
        pass

    def testCase012(self):
        callkargs = {}
        _call  = self.scri
        _call += " PRIO "

        ret = self.sx.callit(_call,**callkargs)
        assert ret ==   [0, ['fromC', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], ['arbitrary signalling ERROR string']]
        pass

    def testCase013(self):
        callkargs = {}
        _call  = self.scri
        _call += " EXITOK "

        ret = self.sx.callit(_call,**callkargs)
        assert ret ==  [0, ['fromD', 'arbitrary output', 'arbitrary signalling OK string', 'arbitrary output'], []]
        pass

    def testCase014(self):
        callkargs = {}
        _call  = self.scri
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
        assert einfo[0] == SystemExit
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
        _call  = self.scri
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
        assert einfo[0] == SystemExit
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
        _call  = self.scri
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
        assert einfo[0] == SystemExit
        assert einfo[1].code== 8

        stdval = self.stdoutbuf.getvalue().replace('\r','')
        stdref = """fromG
arbitrary output
arbitrary signalling NOK string
arbitrary output
""".replace('\r','')
        try:
            assert stdval.strip('\r') == stdref.strip('\r')
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
            self.assertEqual(errval, errref)
            raise e

        sys.stdout = self.stdout
        sys.stderr = self.stderr
        pass

    def testCase017(self):
        callkargs = {}
        _call  = self.scri
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
        assert einfo[0] == SystemExit
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
        _call  = self.scri
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
        assert einfo[0] == SystemExit
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

