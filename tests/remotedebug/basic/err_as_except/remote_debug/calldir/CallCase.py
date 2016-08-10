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

#
#######################
#
class CallUnits(unittest.TestCase):
    def testSubprocessesWithErrorAsException(self):
        """Selftest of the remote debugging feature.
        """

        #
        # *** first level subprocess - call Python process and bring it under control of PyDev ***
        #
        tstcall = os.path.abspath(os.path.dirname(__file__)+os.sep+'../subprocdir/bin/epyunit4RDbg.py')
        tstcall = os.path.normpath(tstcall)
        call  = 'python ' + tstcall  # call the wrapper 

        #
        # *** second level subprocess - call bash process and evaluate hard-coded response ***
        #
        scall = os.path.dirname(tstcall)+'/../../scriptdir/libexec/myscript.sh'       # add a script
        scall = os.path.normpath(scall)
        call += ' ' + scall
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
            pass
        except Exception as e:
            raise


        # assure it is actually the sys.exit
        self.assertIsNotNone(einfo)
        assert einfo[0] == SystemCallsExceptionSubprocessError
        assert einfo[1].code== 8

        stdval = stdoutbuf.getvalue()
        stdref = """['arbitrary output', 'arbitrary signalling NOK string', 'arbitrary output']
"""
        try:
            assert stdval == stdref
        except Exception as e:
            # switch back from stdout and stderr buffers
            sys.stdout = stdout
            sys.stderr = stderr
            print >>sys.stderr,"*** stdout-val="+str(stdval)
            print >>sys.stderr,"*** stdout-ref="+str(stdref)
            raise e

        errval = stderrbuf.getvalue()
        errref = """['arbitrary err output', 'arbitrary err signalling NOK string', 'arbitrary err output']
"""
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
