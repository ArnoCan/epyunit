# -*- coding: utf-8 -*-
"""The module 'epyunit.spUnittest' provides classes derived from 'unittest' for tests of arbitrary subprocesses.

"""
from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.12'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import sys,re
from types import NoneType

from unittest import TestCase
#import unittest

version = '{0}.{1}'.format(*sys.version_info[:2])
if version < '2.7': # pragma: no cover
    raise Exception("Requires Python-2.7.* or higher")


#from epyunit.SystemCalls import SystemCalls
from epyunit.SubprocUnit import SubprocessUnit,SProcUnitRules

class TestExecutableException(Exception):
    """Application error for called executable.
    """
    pass


#class TestExecutable(unittest.TestCase):
class TestExecutable(TestCase):
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

                noparent: Suppress call of parent class. 

                rules: Sets the rules object to be used.

                spunit: Sets the subprocess unit.

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


    def callSubprocess(self,callstr,**kargs):
        """Calls a subprocess and fetches the result data.

        Args:
            callstr: Complete call string for subprocess.
            
            **kargs: Pass-through parameters for 'SystemCalls.callit()'.

        Returns:
            When successful returns the tupel:

                returnvalue := (exit-value, stdout-value, stderr-value)

        Raises:
            passed through exceptions:
        
        """
        return self.spunit.callit(callstr,**kargs)

    def callSubprocessCached(self,callstr,**kargs):
        """Calls a subprocess and fetches the result data into cache for further processing.

        Args:
            callstr: Complete call string for subprocess.
            
            **kargs: Pass-through parameters for 'SystemCalls.callit()'.

        Returns:
            When successful returns the tupel:

                returnvalue := (exit-value, stdout-value, stderr-value)

        Raises:
            passed through exceptions:
        
        """
        self.spcache = self.spunit.callit(callstr,**kargs)
        return self.spcache

    def assertEqual(self,exp,cur=None):
        """Asserts on the exit value of the called process.
        """
        if cur==NoneType:
            cur = self.spcache
        super(TestExecutable,self).assertEqual(exp, cur)
        pass
    
    def assertExit(self,exp,cur=None):
        """Asserts on the exit value of the called process.
        """
        if cur==NoneType:
            cur = self.spcache[0]
        assert exp[0] == cur[0]
        pass
    
    def assertStdout(self,exp,cur=None):
        """Asserts a list of provided regexpr on the STDOUT of the called process.
        """
        if cur==NoneType:
            cur = self.spcache[1]
        super(TestExecutable,self).assertEqual(exp[1], cur[1])
        pass

    def assertStderr(self,exp,cur=None):
        """Asserts a list of provided regexpr on the STDERR of the called process.
        """
        if cur==NoneType:
            cur = self.spcache[2]
        super(TestExecutable,self).assertEqual(exp[2], cur[2])
        pass

    def __str__(self):
        """Prints the current test state.
        """
        pass
