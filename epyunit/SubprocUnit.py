# -*- coding: utf-8 -*-
"""The module 'epyunit.SubprocUnit' provides a simple unit test model for subprocess calls.

"""
from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import sys,re
from types import NoneType

version = '{0}.{1}'.format(*sys.version_info[:2])
if version < '2.7': # pragma: no cover
    raise Exception("Requires Python-2.7.* or higher")

#
# enums for priority type 
#
_P_OK = 0 # hasSuccess
_P_NOK = 1 # hasFailure
_P_WEIGHT = 3 # simple counter compare, bigger wins: (resultok, resultnok), else default


#
# enums for exit type 
#
_E_IGN = 4
_E_OK = 8
_E_NOK = 16
_E_VAL = 32


from epyunit.SystemCalls import SystemCalls

class SProcUnitRulesException(Exception):
    pass

class SubprocessUnitException(Exception):
    pass

class SProcUnitRules(object):
    """
    The 'epyunit.SubprocUnit.SProcUnitRules' defines the expected data, and
    the minimal degree of expectation. Therefore a set of parameters 
    constitute a basic rule set, which matches the provided reference data
    on the actual response data.  
    """

    rules_default = {
        # default when ambiguous
        'default': True,
        
        # re flags
        'cflags': 0,
        'multiline': 0,
        'ignorecase': 0,
        'unicode': 0,
        'dotall': 0,
        'debug': 0,

        # priorities
        'priotype': _P_NOK,

        # required result counters
        'result': 0,
        'resultok': 0,
        'resultnok': 0,

        # exit value match
        'exitign': False,
        'exittype': _E_OK,
        'exitval': 0,

        # stderr match
        'stderrchk': False,
        'stderrnok': [],
        'stderrok': [],

        # stdout match
        'stdoutchk': False,
        'stdoutnok': [],
        'stdoutok': [],
    }
    """
    The default rules for OK operations
    """

    def __init__(self,**kargs):
        """Initializes the ruleset and operational parameters.
        
        For parameters refer to called **setrules** and **setkargs**.
        """
        #
        # the re pattern
        #
        self.stderrnok = []
        self.stderrok = []
        self.stdoutnok = []
        self.stdoutok = []

        #
        # the actual matched strings
        #
        self.stderrnok_matched = []
        self.stderrok_matched = []
        self.stdoutnok_matched = []
        self.stdoutok_matched = []
        self.reset()
        
        _args = kargs.copy()
        self.setkargs(**_args) 
        if not _args.get('default'): # for initial default
            self.setrules(**{'default':True}) 
        self.setrules(**_args) 

    def reset(self):
        """A completely empty initial in-place default set for current variables. 
        """
        # default for ambiguity
        self.default = self.rules_default['default']

        # re flags
        self.cflags = self.rules_default['cflags']
        self.multiline = self.rules_default['multiline']
        self.ignorecase = self.rules_default['ignorecase']
        self.unicode = self.rules_default['unicode']
        self.dotall = self.rules_default['dotall']
        self.debug =  self.rules_default['debug']

        # priorities
        self.priotype = self.rules_default['priotype']


        # required results
        self.result = self.rules_default['result']
        self.resultok = self.rules_default['resultok']
        self.resultnok = self.rules_default['resultnok']

        # exit value match
        self.exitign = self.rules_default['exitign']
        self.exittype = self.rules_default['exittype']
        self.exitval = self.rules_default['exitval']

        # stderr match pattern
        self.stderrok_cnt = 0
        self.stderrnok_cnt = 0
        self.stderrchk = self.rules_default['stderrchk']
        lx=len(self.stderrnok)
        for x in range(lx): #@UnusedVariable
            self.stderrnok.pop()
        lx=len(self.stderrok)
        for x in range(lx): #@UnusedVariable
            self.stderrok.pop()
        
        # stderr matched strings
        self.stderrok_cnt = 0
        self.stderrnok_cnt = 0
        lx=len(self.stderrnok_matched)
        for x in range(lx): #@UnusedVariable
            self.stderrnok_matched.pop()
        lx=len(self.stderrok_matched)
        for x in range(lx): #@UnusedVariable
            self.stderrok_matched.pop()

        
        # stdout match pattern
        self.stdoutok_cnt = 0
        self.stdoutnok_cnt = 0
        self.stdoutchk = self.rules_default['stdoutchk']
        lx=len(self.stdoutnok)
        for x in range(lx): #@UnusedVariable
            self.stdoutnok.pop()
        lx=len(self.stdoutok)
        for x in range(lx): #@UnusedVariable
            self.stdoutok.pop()

        # stdout matched strings
        self.stdoutok_cnt = 0
        self.stdoutnok_cnt = 0
        lx=len(self.stdoutnok_matched)
        for x in range(lx): #@UnusedVariable
            self.stdoutnok_matched.pop()
        lx=len(self.stdoutok_matched)
        for x in range(lx): #@UnusedVariable
            self.stdoutok_matched.pop()

        pass

    def setkargs(self,**kargs):
        """Sets supported parameters.
        
        Applicable for the initial call of self.__init__(), 
        and later modification.
        
        Tolerates unknown keyword parameters, pops own.
        
        Args:
            **kargs: Parameter specific for the operation,

                debug: Sets debug for rule application.

                verbose: Sets verbose for rule application.
                
        Returns:
            When successful returns 'True', else returns either 'False',
            or raises an exception.

        Raises:
            passed through exceptions:
            
        """
        _ret = True
        for k,v in kargs.iteritems():
            if k=='debug':
                self.debug=v
            elif k=='verbose':
                self.verbose=v
        return _ret

    def setrules(self,**predef):
        """Initialize and reset parameters and previous results.

        Args:
            **kargs:

                setdefault: Sets the predefined default dictionary, 
                    see 'rules_default'.
                
                debug:

                    True: see *re.DEBUG*, when set

                    False: default:=unset

                dotall:

                    True: see *re.DOTALL*, when set

                    False: default:=unset

                exitign:
                    
                    True: Ignores exit at all.
                    
                    False: Does not ignore exit value.

                exittype:
                
                    True: Success when exit is 0.
                
                    False: Success when exit is not 0.

                exitokval=#exitval: A specific exit value indicating
                    success.

                exitnokval=#exitval: A specific exit value indicating
                    failure.

                ignorecase:

                    True: see *re.IGNORECASE*, when set

                    False: default:=unset

                multiline: 

                    True: see *re.MULTILINE*, when set

                    False: default:=unset

                priotype:
                    
                    True: One success state sets the whole case 
                        to success.
                    
                    False: One failure state sets the whole case 
                        to failure.

                reset: A reset dictionary, see 'rules_reset'.

                result: Required sum of all matches for success, 
                    else failure.

                resultnok: Required sum of NOK matches for failure, 
                    else success.

                resultok: Required sum of OK matches for success, 
                    else failure.

                stderrnok: List of regular expressions for match on
                    STDERR, indicating failure.

                    Could contain app-cached precompiled 're'.

                stderrok: List of regular expressions for match on
                    STDERR, indicating success.

                    Could contain app-cached precompiled 're'.

                stdoutnok: List of regular expressions for match on
                    STDOUT, indicating failure.

                    Could contain app-cached precompiled 're'.

                stdoutok: List of regular expressions for match on
                    STDOUT, indicating success.

                    Could contain app-cached precompiled 're'.

                unicode:

                    True: see *re.UNICODE*, when set

                    False: default:=unset

        Returns:
            When successful returns 'True', else returns either 'False',
            or raises an exception.

        Raises:
            passed through exceptions:       

        """
        _ret = True
        _cnt = 0

        for k,v in predef.iteritems():

            if k=='setdefault': # set predefined default rule set
                # superposes reference values, reset changes in place
                self.stderrnok = self.rules_default['stderrnok']
                self.stderrok = self.rules_default['stderrok']
                self.stdoutnok = self.rules_default['stdoutnok']
                self.stdoutok = self.rules_default['stdoutok']
                self.reset()
                _cnt += 1

            elif k=='reset': # set predefined reset rule set
                self.reset()

            #
            # string match attributes
            #
            elif k=='multiline':
                self.cflags &= re.MULTILINE

            elif k=='ignorecase':
                self.cflags &= re.IGNORECASE

            elif k=='unicode':
                self.cflags &= re.UNICODE

            elif k=='dotall':
                self.cflags &= re.DOTALL

            elif k=='debug':
                self.cflags &= re.DEBUG

            #
            # weight of types
            #
            elif k=='priotype': # weight priority type 
                self.priotype = v

            #
            # required number of matches - first matching counter dominates
            #
            elif k=='result': # sum of result counter
                self.result = v

            elif k=='resultok': # required number of OK for success
                self.resultok = v

            elif k=='resultnok': # required number of NOK for success
                self.resultnok = v

            #
            # mactch on: exit
            #
            elif k=='exitign':
                self.exittype = _E_IGN
                self.exitign = v
                _cnt += 1
            elif k=='exittype':
                if v:
                    self.exittype = _E_OK
                else:
                    self.exittype = _E_NOK
                _cnt += 1
            elif k=='exitval':
                self.exittype = _E_VAL
                self.exitval = v
                _cnt += 1

            #
            # mactch on: STDERR
            #
            elif k=='stderrnok':
                self.stderrchk = True
                for _ci in v:
                    if _ci and type(_ci) in (str, unicode,):
                        _ci = re.compile(_ci,self.cflags)
                    if _ci:
                        self.stderrnok.append(_ci)
                _cnt += 1

            elif k=='stderrok':
                self.stderrchk = True
                for _ci in v:
                    if _ci and type(_ci) in (str, unicode,):
                        _ci = re.compile(_ci,self.cflags)
                    if _ci:
                        self.stderrok.append(_ci)
                _cnt += 1

            #
            # mactch on: STDOUT
            #
            elif k=='stdoutnok':
                self.stdoutchk = True
                for _ci in v:
                    if _ci and type(_ci) in (str, unicode,):
                        _ci = re.compile(_ci,self.cflags)
                    if _ci:
                        self.stdoutnok.append(_ci)
                _cnt += 1

            elif k=='stdoutok':
                self.stdoutchk = True
                for _ci in v:
                    if _ci and type(_ci) in (str, unicode,):
                        _ci = re.compile(_ci,self.cflags)
                    if _ci:
                        self.stdoutnok.append(_ci)
                _cnt += 1

        if not _cnt:
            return False
        return _ret
    
    def apply(self,ret):
        """Apply rules on the input ret and weight the result.
        
        The provided match patterns and values are matched onto the input, and the 
        number of matches is counted.
        
        The number of required matches of sub-patterns has to be defined within the
        regexpr, e.g. by::

            'abv{4}[^v]+'

        this matches on::

            abvvvv

        Args:
            ret: Tuple received from 'SystemCalls'.
                
        Returns:
            When successful returns 'True', else returns either 'False',
            or raises an exception.

        Raises:
            passed through exceptions:
        
        """
        
        #
        # filter string patterns on STDERR
        #
        if self.stderrchk: # patterns for STDERR are provided
            for _r in self.stderrnok:
                _m = _r.match(ret[2])
                if not _m is NoneType:
                    self.stderrnok_cnt += 1
                    self.resultnok += 1
            for _r in self.stderrok:
                _m = _r.match(ret[2])
                if not _m is NoneType:
                    self.stderrok_cnt += 1
                    self.resultok += 1
        
        #
        # filter string patterns on STDOUT
        #
        if self.stdoutchk: # patterns for STDOUT are provided
            for _r in self.stdoutnok:
                _m = _r.match(ret[1])
                if not _m is NoneType:
                    self.resultnok += 1
                    self.stdoutnok_cnt += 1
            for _r in self.stdoutok:
                _m = _r.match(ret[1])
                if not _m is NoneType:
                    self.resultok += 1
                    self.stdoutok_cnt += 1

        #
        # filter exit
        #
        # check exit value - store condition for later correlation with priorities
        # True: the requested exit value is matched
        # False: did not match the requested exit value
        #
        self.exitcond = True
        if self.exittype == _E_IGN: # ignore exit values
            pass
        elif self.exittype == _E_OK: # check whether present is OK condition 
            if ret[0] == 0:
                self.exitcond = True
            else:
                self.exitcond = False
        elif self.exittype == _E_NOK: # check whether present is NOK condition
            if ret[0] > 0:
                self.exitcond = True
            else:
                self.exitcond = False
        elif self.exittype == _E_VAL: # check whether present is predefined value
            if self.exitval == ret[0]:
                self.exitcond = True
            else:
                self.exitcond = False

        
        #
        # interpret the presence of specific partial results into overall resulting test status
        #
        if self.priotype == _P_OK: # ignore NOK, when at least one OK defined
            if self.resultok > 0:
                self.result = True
            elif self.exitcond and self.exittype == _E_IGN: # by exit-cond
                self.result = True
            elif self.resultnok > 0: # any is NOK
                self.result = self.resultnok
            else:
                self.result = self.default

        elif self.priotype == _P_NOK: # ignore OK, when at least one NOK defined
            if self.resultnok > 0: # NOKs are present
                self.result = False
            elif not self.exitign and not self.exitcond: # by exit-cond
                self.result = False
            elif self.resultok > 0: # any is OK
                self.result = True
            else: # nothing is clear
                self.result = self.default

        return  self.result

    def __str__(self):
        """Prints current rule set.
        """
        ret = ""
        ret += "\nSProcUnitRules.default       = "+str(self.default)
        ret += "\nSProcUnitRules.exitign       = "+str(self.exitign)
        ret += "\nSProcUnitRules.exittype      = "+str(self.exittype)
        ret += "\nSProcUnitRules.exitval       = "+str(self.exitval)
        ret += "\nSProcUnitRules.priotype      = "+str(self.priotype)
        ret += "\nSProcUnitRules.result        = "+str(self.result)
        ret += "\nSProcUnitRules.resultok      = "+str(self.resultok)
        ret += "\nSProcUnitRules.resultnok     = "+str(self.resultnok)
        ret += "\nSProcUnitRules.stderrchk     = "+str(self.stderrchk)
        ret += "\nSProcUnitRules.stderrok      = "+str(self.stderrok)
        ret += "\nSProcUnitRules.stderrnok     = "+str(self.stderrnok)
        ret += "\nSProcUnitRules.stdoutchk     = "+str(self.stdoutchk)
        ret += "\nSProcUnitRules.stdoutok      = "+str(self.stdoutok)
        ret += "\nSProcUnitRules.stdoutnok     = "+str(self.stdoutnok)
        return ret

class SubprocessUnit(SystemCalls):
    """Wraps and checks results from execution of subprocesses by objects of class 'SProcUnitRules'.
    
    """
    def __init__(self,**kargs):
        """Prepares the caller interface for subprocess unit tests.
        
        Args:
            **kargs: Parameter specific for the operation,
                passed through to **setkargs**.

        Returns:
            When successful returns 'True'.

        Raises:
            passed through exceptions:
        
        """
        self.rules = None 

        super(SubprocessUnit,self).__init__(**kargs)
        
#         kargs['noparent'] = True
#         self.setkargs(**kargs)
#         kargs.pop('noparent')
    
    def apply(self,res=None):
        """Applies the linked rule set onto the res-data.

        Args:
            res: Result data to be filtered by a filter of type
                'epyunit.SProcUnitRules'.
            
        Returns:
            When a rule set is present and could be applied successful 
            returns 'True', else either 'False', or raises an exception.

        Raises:
            passed through exceptions:

        """
        if self.rules:
            return self.rules.apply(res)
        return False
    
    def setkargs(self,**kargs):
        """Sets provided parameters for the subprocess call context.
        
        Applicable for the initial call of self.__init__(), 
        and later modification. Called for each start of
        a subprocess in order to update optional the specific 
        call context modification.

        Calls the parent method by default, could be supressed
        by option for the update of current objects class only.

        Args:
            **kargs: Parameters specific for the operations.

                noparent: Suppress call of parent class. 

                rules: Sets the rules object to be used.

        Returns:
            When successful returns 'True', else returns either 'False', or
            raises an exception.

        Raises:
            passed through exceptions:
            
        """
        _ret = True
        _args = kargs.copy()
        _noparent = _args.get('noparent',False)
        for k,v in _args.iteritems():
            if k=='rules':
                self.rules = v
                _args.pop(k)
            elif k=='noparent':
                pass
        
        if not _noparent:
            _ret = super(SubprocessUnit,self).setkargs(**_args)
        
        if not self.rules:
            self.rules = SProcUnitRules(**kargs)
        if not self.rules:
            raise SubprocessUnitException("Failed to set rule set.")
        
        return _ret

    def get_proceed(self,s=None): 
        """Verifies valid proceed type.

        Args:
            s: Requested type for validation.
            
        Returns:
            Supported types.

        Raises:
            passed through exceptions:
        
        """
        if s is NoneType:
            return 'subprocunits'
        if s in ('subprocunits',):
            return s
        else:
            return super(SubprocessUnit,self).get_proceed(s)

    def __str__(self):
        """Prints the current unit parameters including parent.
        """
        ret = super(SubprocessUnit,self).__str__()
        ret += "\nSubprocessUnit.bufsize      = "+str(self.bufsize)
        return ret
