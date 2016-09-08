"""
Verifies basic facilities for remote debugging by starting a subprocess.
Uses:

* epyunit.SystemCalls()

* epyunit.callit()

Applies a two-level subprocess stack:

0. This UseCase

1. The wrapper 'epyunit4RDbg.py'

2. The script with dummy responses for tests 'myscript.sh'

"""
from __future__ import absolute_import

import unittest
import os,sys
from cStringIO import StringIO


from epyunit.SystemCalls import SystemCalls,SystemCallsExceptionSubprocessError
from testdata import epyu,call_scripy

#
#######################
#
class CallUnits(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cache = True

    def testSubprocessesWithErrorAsException(self):
        """Selftest of the remote debugging feature.
        """
        call   = epyu
        call  += " --rdbg "
        call  += " -- "
        call += ' ' + call_scripy
        call += ' EXIT8'

        _kargs = {}

        #
        # *** some error passing options, refer to API ***
        #
        # _kargs['passerr'] = True
        #
        _kargs['errasexcept'] = True
        # _kargs['useexit'] = True
        # _kargs['usestderr'] = True

        #
        _kargs['emptyiserr'] = True

        sx = SystemCalls(**_kargs)

        # buffers for evaluation after intercepted exit.
        stdoutbuf=StringIO()
        stderrbuf=StringIO()
        stdout = sys.stdout
        stderr = sys.stderr

        # passerr is going to call sys.exit,
        # thus cache output and intercept the exit
        sys.stdout = stdoutbuf
        sys.stderr = stderrbuf

        try:
            ret = sx.callit(call) #@UnusedVariable
        except SystemCallsExceptionSubprocessError as e:
            #print "Expected Exception received:"+str(e)
            # save the exception
            einfo = sys.exc_info()
            if not einfo:
                print >>sys.stderr,"Cannot fetch 'sys.exc_info()'"
            elif type(einfo[0]) != SystemCallsExceptionSubprocessError or einfo[1].code != 1:
                outval = stdoutbuf.getvalue()
                errval = stderrbuf.getvalue()

#                 sys.stdout = stdout
#                 sys.stderr = stderr
                # print >>sys.stderr,"STDOUT="+str(outval)
                # print >>sys.stderr,"STDERR="+str(errval)

            pass
        except Exception as e:
            raise

        # assure it is actually the sys.exit
        self.assertIsNotNone(einfo)
        self.assertEqual( [einfo[0], einfo[1].code,], [SystemCallsExceptionSubprocessError, 1,] )

        stdval = stdoutbuf.getvalue().replace('\r','')
        stdref = """fromG
arbitrary output
arbitrary signalling NOK string
arbitrary output
""".replace('\r','')
        try:
            assert stdval == stdref
        except Exception as e:
            # switch back from stdout and stderr buffers
            sys.stdout = stdout
            sys.stderr = stderr
            print >>sys.stderr,"*** stdout-val="+str(stdval)
            print >>sys.stderr,"*** stdout-ref="+str(stdref)
            raise e

        errval = stderrbuf.getvalue().replace('\r','')
        errval = errval.replace('\r','') # it's win,, not SystemCalls!
        errref = """arbitrary err output
arbitrary err signalling NOK string
arbitrary err output
""".replace('\r','')
        try:
            assert errval == errref
        except Exception as e:
            # switch back from stdout and stderr buffers
            sys.stdout = stdout
            sys.stderr = stderr
            print >>sys.stderr,"*** stderr-val="+str(errval)
            print >>sys.stderr,"*** stderr-ref="+str(errref)
            raise e

        # switch back from stdout and stderr buffers
        sys.stdout = stdout
        sys.stderr = stderr

    def testSubprocessesWithErrorAsExceptionPassedExit(self):
        """Selftest of the remote debugging feature.
        """
        call   = epyu
        call  += " --rdbg "
        call  += " --passall "
        call  += " -- "
        call += ' ' + call_scripy
        call += ' EXIT8'

        _kargs = {}

        #
        # *** some error passing options, refer to API ***
        #
        #
        _kargs['passerr'] = True
        #
        _kargs['errasexcept'] = True
        # _kargs['useexit'] = True
        # _kargs['usestderr'] = True

        #
        _kargs['emptyiserr'] = True

        sx = SystemCalls(**_kargs)

        # buffers for evaluation after intercepted exit.
        stdoutbuf=StringIO()
        stderrbuf=StringIO()
        stdout = sys.stdout
        stderr = sys.stderr

        # passerr is going to call sys.exit,
        # thus cache output and intercept the exit
        sys.stdout = stdoutbuf
        sys.stderr = stderrbuf

        try:
            ret = sx.callit(call) #@UnusedVariable
        except SystemCallsExceptionSubprocessError as e:
            #print "Expected Exception received:"+str(e)
            # save the exception
            einfo = sys.exc_info()
            if not einfo:
                print >>sys.stderr,"Cannot fetch 'sys.exc_info()'"
            elif type(einfo[0]) != SystemCallsExceptionSubprocessError or einfo[1].code != 8:
                outval = stdoutbuf.getvalue()
                errval = stderrbuf.getvalue()

                sys.stdout = stdout
                sys.stderr = stderr
                # print >>sys.stderr,"STDOUT="+str(outval)
                # print >>sys.stderr,"STDERR="+str(errval)

            pass
        except Exception as e:
            raise

        # assure it is actually the sys.exit
        self.assertIsNotNone(einfo)
        self.assertEqual( [einfo[0], einfo[1].code,], [SystemCallsExceptionSubprocessError, 8,] )

        stdval = stdoutbuf.getvalue().replace('\r','')
        stdref = """fromG
arbitrary output
arbitrary signalling NOK string
arbitrary output
""".replace('\r','')
        try:
            assert stdval == stdref
        except Exception as e:
            # switch back from stdout and stderr buffers
            sys.stdout = stdout
            sys.stderr = stderr
            print >>sys.stderr,"*** stdout-val="+str(stdval)
            print >>sys.stderr,"*** stdout-ref="+str(stdref)
            raise e

        errval = stderrbuf.getvalue().replace('\r','')
        errval = errval.replace('\r','') # it's win,, not SystemCalls!
        errref = """arbitrary err output
arbitrary err signalling NOK string
arbitrary err output
""".replace('\r','')
        try:
            assert errval == errref
        except Exception as e:
            # switch back from stdout and stderr buffers
            sys.stdout = stdout
            sys.stderr = stderr
            print >>sys.stderr,"*** stderr-val="+str(errval)
            print >>sys.stderr,"*** stderr-ref="+str(errref)
            raise e

        # switch back from stdout and stderr buffers
        sys.stdout = stdout
        sys.stderr = stderr


#
#######################
#

if __name__ == '__main__':
    unittest.main()
