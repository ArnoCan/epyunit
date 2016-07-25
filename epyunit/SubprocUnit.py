# -*- coding: utf-8 -*-
"""The module 'epyunit.SubprocUnit' provides a simple unit test model for subprocess calls.

"""
from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.0'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import sys
version = '{0}.{1}'.format(*sys.version_info[:2])
if version < '2.7': # pragma: no cover
    raise Exception("Requires Python-2.7.* or higher")

from epyunit.SystemCalls import SystemCalls
import subprocess,datetime

class SubprocessUnitException(Exception):
    pass

class SUnitRules(object):
    """
    The 'epyunit.SubprocUnit.SUnitRules' defines the expected data, and
    the degree of expectation. Therefore a set of parameters constitute 
    a basic rule set, which map the provided reference data onto the 
    actual response data.  
    """

    rules_default = {
        'default': 'OK',
        'exit_chk': True,
        'exit_type': "OK",
        'exit_val': 0,
        'stderr_chk': False,
        'stderrok_val': [],
        'stderrnok_val': [],
        'stdout_chk': False,
        'stdoutok_val': [],
        'stdoutnok_val': [],
        'prio_chk': 'NOK',
        'result': False,
        'resultok': 0,
        'resultnok': 0,
    }
    """
    The default rules for OK operations
    """
    
    rules_reset = {
        'default': 'OK',
        'exit_chk': True,
        'exit_type': "OK",
        'exit_val': "0",
        'stderr_chk': False,
        'stderrok_val': [],
        'stderrnok_val': [],
        'stdout_chk': False,
        'stdoutok_val': [],
        'stdoutnok_val': [],
        'prio_chk': 'NOK',
        'result': "",
        'resultok': 0,
        'resultnok': 0,
    }
    """
    A completely empty set for setting an initial subset. 
    """
    
    def __init__(self,**kargs):
        self.setrules()
        self.setkargs(**kargs)
        pass

    def setkargs(self,**kargs):
        """Sets provided parameters.
        
        Applicable for the initial call of self.__init__(), 
        and later modification.
        
        Args:
            **kargs: Parameter specific for the operation,

                stderrok: Match string for STDERR indicating
                    success.

                stderrnok: Match string for STDERR indicating
                    failure.

                stdoutok: Match string for STDOUT indicating
                    success.

                stdoutnok: Match string for STDOUT indicating
                    failure.

                exitval=#exitval: A specific exit value indicating
                    success.

                exitok: Success when exit is 0.

                exitnok: Success when exit is not 0.

                exitign: Ignores exit at all.

                priook: Priority is OK,thus a success state
                    sets the whole case to success.

                prionok: Priority is NOK,thus a failure state
                    sets the whole case to success.

                verbose: Sets verbose for rule application.
                
                debug: Sets debug for rule application.

        Returns:
            When successful returns 'True', else returns either 'False'.

        Raises:
            passed through exceptions:
            
        """
        for k,v in kargs.iteritems():
            if k=='stderrok':
                self.stderrok_val=v
            elif k=='stderrnok':
                self.stderrnok_val=v
            elif k=='stdoutok':
                self.stdoutok_val=v
            elif k=='stdoutnok':
                self.stdoutnok_val=v
            elif k=='exitok':
                self.exitok=v
            elif k=='exitnok':
                self.exitok=v
            elif k=='exitignore':
                self.exitignore=v
            elif k=='priook':
                self.priook=v
            elif k=='priook':
                self.priook=v
            elif k=='exitval':
                self.exit_val=v

            elif k=='verbose':
                self.verbose=v
            elif k=='debug':
                self.debug=v

            else:
                raise Exception('STATE:ERROR:parameter not supported:'+str(k))
        pass

    def setrules(self,*d,**predef):
        """init/reset parameters and previous results
        """
        #
        if d:
            if len(d) >1:
                raise SubprocessUnitException("ERROR:accepts one arg:"+str(d))
            _default = d[0]
        else:
            _default = self.rules_default

        #
        # REMARK: empty and None types may eventually be valid data types,
        #     thus the 77777 is applied, which of course could be valid data
        #     too...
        #
        
        _x = predef.get('default',77777)
        if _x == 77777:
            _x = _default.get('default',77777)
        if _x != 77777:
            self.default = _x
        

        # exit values
        _x = predef.get('exit_chk',77777)
        if _x == 77777:
            _x = _default.get('exit_chk',77777)
        if _x != 77777:
            self.exit_chk = _x

        _x = predef.get('exit_type',77777)
        if _x == 77777:
            _x = _default.get('exit_type',77777)
        if _x != 77777:
            self.exit_type = _x

        _x = predef.get('exit_val',77777)
        if _x == 77777:
            _x = _default.get('exit_val',77777)
        if _x != 77777:
            self.exit_val = _x

        # stderr => stdin
        _x = predef.get('stderr_chk',77777)
        if _x == 77777:
            _x = _default.get('stderr_chk',77777)
        if _x != 77777:
            self.stderr_chk = _x

        _x = predef.get('stderrok_val',77777)
        if _x == 77777:
            _x = _default.get('stderrok_val',77777)
        if _x != 77777:
            self.stderrok_val = _x

        _x = predef.get('stderrnok_val',77777)
        if _x == 77777:
            _x = _default.get('stderrnok_val',77777)
        if _x != 77777:
            self.stderrnok_val = _x

        # stdout => stdin
        _x = predef.get('stdout_chk',77777)
        if _x == 77777:
            _x = _default.get('stdout_chk',77777)
        if _x != 77777:
            self.stdout_chk = _x

        _x = predef.get('stdoutok_val',77777)
        if _x == 77777:
            _x = _default.get('stdoutok_val',77777)
        if _x != 77777:
            self.stdoutok_val = _x

        _x = predef.get('stdoutnok_val',77777)
        if _x == 77777:
            _x = _default.get('stdoutnok_val',77777)
        if _x != 77777:
            self.stdoutnok_val = _x
        
        # weight priority type 
        _x = predef.get('prio_chk',77777)
        if _x == 77777:
            _x = _default.get('prio_chk',77777)
        if _x != 77777:
            self.prio_chk = _x

        # result counter
        _x = predef.get('result',77777)
        if _x == 77777:
            _x = _default.get('result',77777)
        if _x != 77777:
            self.result = _x

        _x = predef.get('resultok',77777)
        if _x == 77777:
            _x = _default.get('resultok',77777)
        if _x != 77777:
            self.resultok = _x

        _x = predef.get('resultnok',77777)
        if _x == 77777:
            _x = _default.get('resultnok',77777)
        if _x != 77777:
            self.resultnok = _x


        pass
    
    def apply(self,ret):
        """apply rules and weight the result
        """
        
        #
        # check string patterns on STDERR
        #
        if self.stderr_chk: # patterns for STDERR are provided
            if ret[1] in self.stderrnok_val:
                self.resultnok += 1
            if ret[1] in self.stderrok_val:
                self.resultok += 1
        
        #
        # check string patterns on STDOUT
        #
        if self.stdout_chk: # patterns for STDOUT are provided
            if ret[1] in self.stdoutnok_val:
                self.resultnok += 1
            if ret[1] in self.stdoutok_val:
                self.resultok += 1

        #
        # check exit value - store condition for later correlation with priorities
        # True: the requested exit value is matched
        # False: did not match the requested exit value
        #
        self.exitcond = True
        if self.exit_chk: # use exit values
            if self.exit_type == "OK": # check whether present is OK condition 
                if ret[0] == 0:
                    self.exitcond = True
                else:
                    self.exitcond = False
        
            elif self.exit_type == "NOK": # check whether present is NOK condition
                if ret[0] > 0:
                    self.exitcond = True
                else:
                    self.exitcond = False
        
            elif self.exit_type == "VAL": # check whether present is predefined value
                if self.exit_val == ret[0]:
                    self.exitcond = True
                else:
                    self.exitcond = False
        
            # self.exit_type == "IGN": # may not occur

        
        #
        # interpret the presence of specific partial results into overall resulting test status
        #
        if self.prio_chk == "OK": # ignore NOK, when at least one OK defined
            if self.resultok > 0:
                self.result = True
            elif self.exit_chk and self.exitcond: # by exit-cond
                self.result = True
            elif self.resultnok > 0: # any is NOK
                self.result = self.resultnok
            else:
                if self.default == 'OK':
                    self.result = True
                else:
                    self.result = False

        elif self.prio_chk == "NOK": # ignore OK, when at least one NOK defined
            if self.resultnok > 0: # NOKs are present
                self.result = False
            elif self.exit_chk and not self.exitcond: # by exit-cond
                self.result = False
            elif self.resultok > 0: # any is OK
                self.result = True
            else: # nothing is clear
                if self.default == 'OK':
                    self.result = True
                else:
                    self.result = False

        return  self.result

    def __str__(self):
        ret = ""
        ret += "\nSUnitRules.default       = "+str(self.default)
        ret += "\nSUnitRules.exit_chk      = "+str(self.exit_chk) # not ignore
        ret += "\nSUnitRules.exit_type     = "+str(self.exit_type)
        ret += "\nSUnitRules.exit_val      = "+str(self.exit_val)
        ret += "\nSUnitRules.prio_chk      = "+str(self.prio_chk)
        ret += "\nSUnitRules.result        = "+str(self.result)
        ret += "\nSUnitRules.resultok      = "+str(self.resultok)
        ret += "\nSUnitRules.resultnok     = "+str(self.resultnok)
        ret += "\nSUnitRules.stderr_chk    = "+str(self.stderr_chk)
        ret += "\nSUnitRules.stderrok_val  = "+str(self.stderrok_val)
        ret += "\nSUnitRules.stderrnok_val = "+str(self.stderrnok_val)
        ret += "\nSUnitRules.stdout_chk    = "+str(self.stdout_chk)
        ret += "\nSUnitRules.stdoutok_val  = "+str(self.stdoutok_val)
        ret += "\nSUnitRules.stdoutnok_val = "+str(self.stdoutnok_val)
        return ret

class SubprocessUnit(SystemCalls):
    """Wraps and checks results from execution of subprocesses.
    
    """
    def __init__(self,**kargs):
        """Prepares the caller interface for subprocesses.
        
        The initial setup also includes the preparation of the result 
        cache for the response data from stdout and stderr.

        Args:
            **kargs: Parameter specific for the operation,
                see **setkargs**.

        Returns:
            When successful returns 'True', else returns either 'False', or
            raises an exception.
            Success is the complete addition only, thus one failure returns
            False.

            *REMARK*
                When errors occur in buffered mode the
                output from the called process is possibly
                not completely cached. In that case
                switch to 'dialogue' mode in order to get an 
                unbuffered console display.

        Raises:
            passed through exceptions:
        
        """
        super(SubprocessUnit,self).__init__(**kargs)
        
        self.rules = SUnitRules(**kargs) 
        self.out = None 
        
        self.setkargs(**kargs)
        pass
    
    def apply(self,res=None):
        """Applies the linked rule set onto the res-data.

        Args:
            res: Result data to be filtered by a filter of type
            'epyunit.SUnitRules'.
            
        Returns:
            When successful returns 'True', else either 'False', or
            raises an exception.

        Raises:
            passed through exceptions:
            
        """
        if self.rules:
            return self.rules.apply(res)
        pass
    
    def setkargs(self,**kargs):
        """Sets provided parameters.
        
        Applicable for the initial call of self.__init__(), 
        and later modification.
        
        Args:
            **kargs: Parameter specific for the operation,

                rules: Sets the rules object to used.

                verbose: Sets verbose for rule data flow.
                
                debug: Sets debug for rule data flow.

        Returns:
            When successful returns 'True', else returns either 'False', or
            raises an exception.

        Raises:
            passed through exceptions:
            
        """
        for k,v in kargs.iteritems():
            if k=='rules':
                self.rules = v
            elif k=='verbose':
                self.verbose=v
            elif k=='debug':
                self.debug=v

            else:
                raise Exception('STATE:ERROR:parameter not supported:'+str(k))
        pass

    def get_proceed(self,s): 
        """Verifies valid proceed type."""
        if s in ('print','trace', 'doit'):
            return s
        else:
            raise Exception('STATE:ERROR:proceed not supported:'+str(s))

    def __str__(self):
        ret = super(SubprocessUnit,self).__str__()
        ret += "\nSubprocessUnit.bufsize      = "+str(self.bufsize)
        return ret



