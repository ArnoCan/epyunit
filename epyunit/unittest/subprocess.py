# -*- coding: utf-8 -*-
"""The module 'epyunit.unittest.subprocess' provides classes derived from 'unittest' for tests of arbitrary subprocesses.

"""
from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.14'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import sys,os
from types import NoneType

#from unittest import TestCase
import unittest

version = '{0}.{1}'.format(*sys.version_info[:2])
if version < '2.7': # pragma: no cover
    raise Exception("Requires Python-2.7.* or higher")


#from epyunit.SystemCalls import SystemCalls
from epyunit.SubprocUnit import SubprocessUnit,SProcUnitRules

class TestExecutableException(Exception):
    """Application error for called executable.
    """
    pass

class FileNodeDoesNotExists(Exception):
    """Filesystem node does not exist.
    """
    pass

class TestExecutable(unittest.TestCase):
#class TestExecutable(TestCase):
    """Extends TestCase for subprocesses.
    """

    def __init__(self,*args, **kargs):
        """Initializes the test case, passes parameters to 'unittest.TestCase'. 

        Args:
            **kargs: Parameter specific for the operation,
                passed through to **setkargs**.

        Returns:
            When successful returns 'True'.

        Raises:
            passed through exceptions:

        """
        super(TestExecutable,self).__init__(*args,**kargs)

        self.spunit = None
        """Subprocess unit assigned to this test case."""
        if not kargs.get('spunit'): # else shift setting into setkargs()
            self.spunit = SubprocessUnit()

        self.spcache = [0,None,None]
        """Subprocess output caches.
        """
    
        self.setkargs(**kargs) # sets parameters
        pass

    def setkargs(self,**kargs):
        """Sets provided parameters for the subprocess call context.
        
        Applicable for the initial call of self.__init__(), 
        and later modification. Called for each start of
        a subprocess in order to update optional the specific 
        call context modification.

        Args:
            **kargs: Parameters specific for the operations.

                cache: 
                    Sets caching of the results for subprocess call. 

                noparent: 
                    Suppress call of parent class. 

                rules: 
                    Sets the rules object to be used.
                    See: epyunit.SubprocUnit.SProcUnitRules

                spunit: 
                    Sets the subprocess unit.
                    See: epyunit.SubprocUnit.SProcUnit

        Returns:
            When successful returns 'True', else returns either 'False', or
            raises an exception.

        Raises:
            passed through exceptions:
            
        """
        self.noparent = kargs.get('noparent',False)
        for k,v in kargs.items():
            if k == 'rules':
                self.spunit.setruleset(v)
            elif k == 'spunit':
                self.spunit = v
            elif k == 'cache':
                self.spcache = v


    def callSubprocess(self,callstr,**kargs):
        """Calls a subprocess and fetches the result data.

        Args:
            callstr: Complete call string for subprocess.
            
            **kargs: 
                Pass-through parameters for 'SystemCalls.callit()'.
            
                cache: 
                    Caches results.

        Returns:
            When successful returns the tupel:

                returnvalue := (exit-value, stdout-value, stderr-value)

        Raises:
            passed through exceptions:
        
        """
        _sargs = kargs.copy()
        _cache = self.spcache
        for k,v in _sargs.items():
            if k == 'cache':
                _cache = v
                _sargs.pop(k)

        if _cache:
            self.spcache = self.spunit.callit(callstr,**_sargs)
            return self.spcache
        return self.spunit.callit(callstr,**_sargs)

    def assertEqual(self,exp,cur=None):
        """Asserts tuple result value of the called process.

        Args:
            exp: Expected value:
                (exit-value, stdout-value, stderr-value)
            
            cur: Current value:
                (exit-value, stdout-value, stderr-value)

                default:=self.spcache

        Returns:
            When successful returns the True, else raises an exception.

        Raises:
            Raises result of assertEqueal.

        """
        if type(cur) == NoneType:
            cur = self.spcache
        super(TestExecutable,self).assertEqual(exp, cur)
        return True
    
    def assertExit(self,exp,cur=None):
        """Asserts on the exit value of the called process.

        Args:
            exp: Expected value:
                exit-value
            
            cur: Current value:
                exit-value

                default:=self.spcache[0]

        Returns:
            When successful returns the True, else raises an exception.

        Raises:
            Raises result of assertEqual.

        """
        if type(cur) == NoneType:
            cur = self.spcache[0]
        assert exp[0] == cur[0]
        pass
    
    def assertExists(self,fpname):
        """Asserts on the existance of a filesystem node.

        Args:
            fpname: Filesystem node.
            

        Returns:
            When successful returns the True, else raises an exception.

        Raises:
            Raises result FileNodeDoesNotExists.

        """
        self.assertTrue(os.path.exists(fpname))
        return True

    def assertStdout(self,exp,cur=None):
        """Asserts a list of provided regexpr on the STDOUT of the called process.

        Args:
            exp: Expected value:
                stdout-value
            
            cur: Current value:
                stdout-value

                default:=self.spcache[1]

        Returns:
            When successful returns the True, else raises an exception.

        Raises:
            Raises result of assertEqual.

        """
        if type(cur) == NoneType:
            cur = self.spcache[1]
        return super(TestExecutable,self).assertEqual(exp[1], cur[1])
        pass

    def assertStderr(self,exp,cur=None):
        """Asserts a list of provided regexpr on the STDERR of the called process.

        Args:
            exp: Expected value:
                stderr-value
            
            cur: Current value:
                stderr-value

                default:=self.spcache[2]

        Returns:
            When successful returns the True, else raises an exception.

        Raises:
            Raises result of assertEqual.

        """
        if type(cur) == NoneType:
            cur = self.spcache[2]
        return super(TestExecutable,self).assertEqual(exp[2], cur[2])
        pass

    def assertSubprocess(self,callstr, res, **kargs):
        """Calls a subprocess and asserts the result data.

        Args:
            callstr: 
                Complete call string for subprocess.
            
            res: 
                Result from 'TestExecutable.callSubprocess()'

                    returnvalue := (exit-value, stdout-value, stderr-value)

            **kargs: 
                Pass-through parameters for 'SystemCalls.callit()'.
            
                cache: 
                    Caches results.

        Returns:
            When successful returns True, else raises exception.

        Raises:
            passed through exceptions:
        
        """
        ret = self.callSubprocess(callstr)
        return self.assertEqual(ret, res)


    def __str__(self):
        """Prints the current test state.
        """
        pass
