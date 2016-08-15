# -*- coding: utf-8 -*-
from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.12'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import sys,re
from types import NoneType

version = '{0}.{1}'.format(*sys.version_info[:2])
if version < '2.7': # pragma: no cover
    raise Exception("Requires Python-2.7.* or higher")

from epyunit.SystemCalls import SystemCalls

_parentrepr = re.compile(ur'[{](.*[^}])}')
"""
static precompiled 're' for parent '__repr__'.
"""

#
# enums for priority type 
#
_P_OK = 0 
"""
hasSuccess
"""

_P_NOK = 1
"""
hasFailure
"""

_P_WEIGHT = 3
"""
simple counter compare, bigger wins: (resultok, resultnok), else default
"""
_prioenums = {0:'_P_OK',1:'_P_NOK',3:'_P_WEIGHT', }

#
# enums for exit type 
#
_E_IGN = 4
"""
exittype: ignore
"""

_E_OK = 8
"""
exittype: OK
"""

_E_NOK = 16
"""
exittype: NOK
"""

_E_VAL = 32
"""
exittype: value
"""
_exitenums = {4:'_E_IGN', 8:'_E_OK', 16:'_E_NOK',32:'_E_VAL', }


class SProcUnitRulesException(Exception):
    """Application error of unittest rules.
    """
    pass

class SubprocessUnitException(Exception):
    """Failure of subprocess call.
    """
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

        '_exitcond': False,
        '_exitret': 0,

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
        self.stderrnok = []; """list of 're' patterns indicating error on STDERR"""
        self.stderrok = []; """list of 're' patterns indicating success on STDERR"""
        self.stdoutnok = []; """list of 're' patterns indicating success on STDOUT"""
        self.stdoutok = []; """list of 're' patterns indicating success on STDOUT"""

        #
        # the actual matched strings
        #
        self.stderrnok_matched = []; """list of actually matched failure strings on STDERR"""
        self.stderrok_matched = []; """list of actually matched success strings on STDERR"""
        self.stdoutnok_matched = []; """list of actually matched failure strings on STDOUT"""
        self.stdoutok_matched = []; """list of actually matched success strings on STDOUT"""

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
        self.result_cnt = 0
        self.resultok_cnt = 0
        self.resultnok_cnt = 0
        self.result = self.rules_default['result']
        self.resultok = self.rules_default['resultok']
        self.resultnok = self.rules_default['resultnok']

        # exit value match
        self.exitign = self.rules_default['exitign']
        self.exittype = self.rules_default['exittype']
        self.exitval = self.rules_default['exitval']

        # stderr match pattern
        self.stderrchk = self.rules_default['stderrchk']
        lx=len(self.stderrnok)
        for x in range(lx): #@UnusedVariable
            self.stderrnok.pop()
        self.stderrnok.extend(self.rules_default['stderrnok'])

        lx=len(self.stderrok)
        for x in range(lx): #@UnusedVariable
            self.stderrok.pop()
        self.stderrok.extend(self.rules_default['stderrok'])
        
        # stderr matched strings
        lx=len(self.stderrnok_matched)
        for x in range(lx): #@UnusedVariable
            self.stderrnok_matched.pop()
        self.stderrnok_cnt = 0

        lx=len(self.stderrok_matched)
        for x in range(lx): #@UnusedVariable
            self.stderrok_matched.pop()
        self.stderrok_cnt = 0

        
        # stdout match pattern
        self.stdoutchk = self.rules_default['stdoutchk']
        lx=len(self.stdoutnok)
        for x in range(lx): #@UnusedVariable
            self.stdoutnok.pop()
        self.stdoutnok.extend(self.rules_default['stdoutnok'])

        lx=len(self.stdoutok)
        for x in range(lx): #@UnusedVariable
            self.stdoutok.pop()
        self.stdoutok.extend(self.rules_default['stdoutok'])

        # stdout matched strings
        lx=len(self.stdoutnok_matched)
        for x in range(lx): #@UnusedVariable
            self.stdoutnok_matched.pop()
        self.stdoutnok_cnt = 0

        lx=len(self.stdoutok_matched)
        for x in range(lx): #@UnusedVariable
            self.stdoutok_matched.pop()
        self.stdoutok_cnt = 0

        self._exitcond = self.rules_default['_exitcond']
        self._exitret = self.rules_default['_exitret']

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
                
                    False|'nok': Success when exit is not 0.

                    True|'ok': Success when exit is 0.
                    
                    'value': Success when exit is equal <exit-value>.

                exitval=<exit-value>: A specific exit value indicating
                    success.

                ignorecase:

                    True: see *re.IGNORECASE*, when set

                    False: default:=unset

                multiline: 

                    True: see *re.MULTILINE*, when set

                    False: default:=unset

                priotype:
                    
                    False|'nok': One failure state sets the whole case 
                        to failure. This is the default.

                    True|'ok': One success state sets the whole case 
                        to success.
                    
                    'weight': Choose larger values of counters.

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
            elif k=='priotype': # weight priority type,current 2 values
                if v in (True,) :
                    self.priotype = _P_OK
                elif v in (False,):
                    self.priotype = _P_NOK
                elif v.lower() in ('ok',) :
                    self.priotype = _P_OK
                else:
                    self.priotype = _P_NOK

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
                if v:
                    self.exittype = _E_IGN
                else:
                    if self.exittype == _E_IGN:
                        self.exittype = self.rules_default['exittype'] 
                self.exitign = v
                _cnt += 1
            elif k=='exittype':
                if v in (True,) :
                    self.exittype = _E_OK
                elif v in (False,) :
                    self.exittype = _E_NOK
                elif v.lower() in ('ok',) :
                    self.exittype = _E_OK
                elif v.lower() in ('value','val',) :
                    self.exittype = _E_VAL
                else:
                    self.exittype = _E_NOK
                _cnt += 1
            elif k=='exitval':
                self.exittype = _E_VAL
                self.exitval = int(v)
                _cnt += 1

            #
            # mactch on: STDERR
            #
            elif k=='stderrnok':
                self.stderrchk = True
                if not type(v) is list:
                    _v = [v]
                else:
                    _v = v
                for _ci in _v:
                    if _ci and type(_ci) in (str, unicode,):
                        _ci = re.compile(_ci,self.cflags)
                    if _ci:
                        self.stderrnok.append(_ci)
                _cnt += 1

            elif k=='stderrok':
                self.stderrchk = True
                if not type(v) is list:
                    _v = [v]
                else:
                    _v = v
                for _ci in _v:
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
                if not type(v) is list:
                    _v = [v]
                else:
                    _v = v
                for _ci in _v:
                    if _ci and type(_ci) in (str, unicode,):
                        _ci = re.compile(_ci,self.cflags)
                    if _ci:
                        self.stdoutnok.append(_ci)
                _cnt += 1

            elif k=='stdoutok':
                self.stdoutchk = True
                if not type(v) is list:
                    _v = [v]
                else:
                    _v = v
                for _ci in _v:
                    if _ci and type(_ci) in (str, unicode,):
                        _ci = re.compile(_ci,self.cflags)
                    if _ci:
                        self.stdoutok.append(_ci)
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
        _result = self.default


        #-----------------------------
        # ***   filter and count   ***
        #-----------------------------

        #
        # filter string patterns on STDERR
        #
        if self.stderrchk: # patterns for STDERR are provided
            for _r in self.stderrok:
                _mx = ret[2]
                if type(_mx) == list:
                    _mx = '\n'.join(_mx)
                _m = _r.search(_mx,self.cflags)
                if type(_m) is NoneType:
                    continue
                self.stderrok_matched.append(_mx)
                self.stderrok_cnt += 1
                self.resultok_cnt += 1
            for _r in self.stderrnok:
                _mx = ret[2]
                if type(_mx) == list:
                    _mx = '\n'.join(_mx)
                _m = _r.search(_mx,self.cflags)
                if type(_m) is NoneType:
                    continue
                self.stderrnok_matched.append(_mx)
                self.stderrnok_cnt += 1
                self.resultnok_cnt += 1
        
        #
        # filter string patterns on STDOUT
        #
        if self.stdoutchk: # patterns for STDOUT are provided
            for _r in self.stdoutok:
                _mx = ret[1]
                if type(_mx) == list:
                    _mx = '\n'.join(_mx)
                _m = _r.search(_mx,self.cflags)
                if type(_m) is NoneType:
                    continue
                self.stdoutok_matched.append(_mx)
                self.stdoutok_cnt += 1
                self.resultok_cnt += 1
            for _r in self.stdoutnok:
                _mx = ret[1]
                if type(_mx) == list:
                    _mx = '\n'.join(_mx)
                _m = _r.search(_mx,self.cflags)
                if type(_m) is NoneType:
                    continue
                self.stdoutnok_matched.append(_mx)
                self.stdoutnok_cnt += 1
                self.resultnok_cnt += 1

        # sumup
        self.result_cnt = self.resultok_cnt + self.resultnok_cnt
        

        #
        # filter exit
        #
        # check exit value - store condition for later correlation with priorities
        # True: the requested exit value is matched
        # False: did not match the requested exit value
        #
        self._exitcond = True
        self._exitret = ret[0]
        if self.exittype == _E_IGN: # ignore exit values
            pass # exitconf == True
        elif self.exittype == _E_OK: # check whether current exit is OK 
            self._exitcond = ret[0] == 0
        elif self.exittype == _E_NOK: # check whether current exit is NOK
            self._exitcond = ret[0] > 0
        elif self.exittype == _E_VAL: # check whether present is predefined value
            self._exitcond = self.exitval == ret[0]


        #----------------------------------
        # ***   priotype and countres   ***
        #----------------------------------

        #
        # interpret the presence of specific partial results into overall resulting test status
        #
        
        #
        # any failure dominates
        #
        if self.priotype == _P_NOK: # ignore OK, when at least one NOK defined/failure occured
            if self.resultnok_cnt and self.resultnok_cnt >= self.resultnok: # threshold for expected failures
                _result = False
            elif self.resultok_cnt and self.resultok_cnt < self.resultok: # threshold for required success
                _result = False
            elif self.exitign: # no more failure criteria expected
                if self.stderrok and self.stderrok_cnt  == 0 or self.stdoutok and self.stdoutok_cnt == 0:
                    _result = False # no provided success criteria matched, thus define as failure 
                else: 
                    _result = True # no failure criteria was provided, thus define as success
            else:
                _result = self._exitcond


        #
        # any success dominates
        #
        elif self.priotype == _P_OK: # ignore NOK, when at least one OK defined
            if self.resultok_cnt and self.resultok_cnt >= self.resultok: # OK counter threshold match
                _result = True
            elif self.resultnok_cnt and self.resultnok_cnt < self.resultnok: # any is NOK
                _result = True            
            elif self.exitign: # no more success criteria expected
                if self.stderrok and self.stderrok_cnt or self.stdoutok and self.stdoutok_cnt:
                    _result = True 
                elif self.stderrnok and self.stderrnok_cnt == 0 or self.stdoutnok and not self.stdoutnok_cnt == 0:
                    _result = True
                else: 
                    _result = False

#                 if self.stderrnok and self.stderrnok_cnt or self.stdoutnok and self.stdoutnok_cnt:
#                     _result = False # no provided failure criteria matched, thus define as success 
#                 else: 
#                     _result = True # no failure criteria was provided, thus define as failure
            else:
                _result = self._exitcond

        #
        # weight the success and failures
        #
        elif self.priotype == _P_WEIGHT: # weight counters
            pass
        
        return  _result

    def states(self):
        """State values of current applied unittest.
        
        The applied parameters are available by 'repr()'.

        Args:
            ret: Tuple received from 'SystemCalls'.
                
        Returns:
            Returns the state of the last 'apply' operation.
            this is the result of the 'filter' and 'countres'
            described in the manual by the syntax-tree::

              r = {
                '_exitcond' = self._exitcond,   # resulting after applied self.exittype
                'exit' = self._exitret, # see _exitcond 
                'stderrnok' = self.stderrnok_matched,
                'stderrok' = self.stderrok_matched,
                'stdoutnok' = self.stdoutnok_matched,
                'stdoutok' = self.stdoutok_matched,

                'result' = self.result_cnt,
                'resultnok' = self.resultnok_cnt,
                'resultok' = self.resultok_cnt,
              }


        Raises:
            passed through exceptions:
        
          
        """
        _r = {}
        _r['_exitcond'] = self._exitcond
        _r['exit'] = self._exitret

        _r['stderrnok'] = self.stderrnok_matched
        _r['stderrok'] = self.stderrok_matched
        _r['stdoutnok'] = self.stdoutnok_matched
        _r['stdoutok'] = self.stdoutok_matched

        _r['result'] = self.result_cnt
        _r['resultnok'] = self.resultnok_cnt
        _r['resultok'] = self.resultok_cnt

        return _r
 
    def __str__(self):
        """Prints current rule set.
        """
        def _eenum(t):
            _e = _exitenums.get(t)
            if _e: return  _e+"("+str(t)+")"
            return str(t)

        def _penum(t):
            _e = _prioenums.get(t)
            if _e: return  _e+"("+str(t)+")"
            return str(t)

        ret = ""
        ret += "\ndefault       = "+str(self.default)
        ret += "\nexitign       = "+str(self.exitign)
        ret += "\nexittype      = "+str(_eenum(self.exittype))
        ret += "\nexitval       = "+str(self.exitval)
        ret += "\npriotype      = "+str(_penum(self.priotype))
        ret += "\nresult        = "+str(self.result)
        ret += "\nresultok      = "+str(self.resultok)
        ret += "\nresultnok     = "+str(self.resultnok)
        ret += "\nstderrchk     = "+str(self.stderrchk)
        ret += "\nstderrok      = "+str(self._re_pattern(self.stderrok))
        ret += "\nstderrnok     = "+str(self._re_pattern(self.stderrnok))
        ret += "\nstdoutchk     = "+str(self.stdoutchk)
        ret += "\nstdoutok      = "+str(self._re_pattern(self.stdoutok))
        ret += "\nstdoutnok     = "+str(self._re_pattern(self.stdoutnok))
        return ret

    def _re_pattern(self,pat):
        return [str(xi.pattern) for xi in pat]
        
    def __repr__(self):
        """Represents current rule set.
        """
        ret = "{"
        ret += "'default': "+str(self.default)
        ret += ", 'cflags': "+str(self.cflags)
        ret += ", 'multiline': "+str(self.multiline)
        ret += ", 'ignorecase': "+str(self.ignorecase)
        ret += ", 'unicode': "+str(self.unicode)
        ret += ", 'dotall': "+str(self.dotall)
        ret += ", 'debug': "+str(self.debug)
        ret += ", 'priotype': "+str(self.priotype)
        ret += ", 'result': "+str(self.result)
        ret += ", 'resultok': "+str(self.resultok)
        ret += ", 'resultnok': "+str(self.resultnok)
        ret += ", 'exitign': "+str(self.exitign)
        ret += ", 'exittype': "+str(self.exittype)
        ret += ", 'exitval': "+str(self.exitval)
        ret += ", 'stderrchk': "+str(self.stderrchk)
        ret += ", 'stderrnok': "+str(self.stderrnok)
        ret += ", 'stderrok': "+str(self.stderrok)
        ret += ", 'stdoutchk': "+str(self.stdoutchk)
        ret += ", 'stdoutnok': "+str(self.stdoutnok)
        ret += ", 'stdoutok': "+str(self.stdoutok)
        ret += "}"
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
    
    def displayit(self,ret,**kargs):
        """Displays result list ret in selected format.

        Args:
            ret: Data to be displayed.
            
            **kargs:

                outtarget: The target of display:
                
                    str: return as formatted string
                
                    stdout: print to sys.stdout
                
                    stderr: print to sys.stderr
                
                out: Output for display, valid:
                    
                    csv   : CSV with sparse records
                    
                    pass  : pass through STDOUT and STDERR from subprocess

                    repr  : Python 'repr()'
                    
                    str   : Python 'str()'
                    
                    xml   : XML
                
                default:=self.out

        Returns:
            When successful returns

                outtarget=='str': returns a printable formatted string

                outtarget in ('stdout', 'stderr',): 

                    'True':  for success

                    'False': for failure

        Raises:
            passed through exceptions:
        
        """
        
        return super(SubprocessUnit,self).displayit(ret,**kargs)

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
        for k,v in kargs.iteritems():
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

#FIXME:

    def setruleset(self,ruleset):
        """Assigns the ruleset object as current.
        
        Args:
            ruleset: The ruleset to be applied as unittest.
                Replaces any previous.

        Returns:
            Returns the previous value of ruleset.
            If input is not an instance of 'SProcUnitRules'
            returns 'None'.

        Raises:
            passed through exceptions:
            
        """
        if not isinstance(ruleset,SProcUnitRules):
            return None
        _o = self.rules
        self.rules = ruleset
        return _o

    def getruleset(self):
        """Returns the current ruleset.
        
        Args:
            **kargs: Parameters passed transparently to
                 created SProcUnitRules instance.

                noparent: Suppress call of parent class. 

        Returns:
            Returns the current rules.

        Raises:
            passed through exceptions:
            
        """
        return self.rules

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
        ret += "\n"
        ret += "\nSubprocessUnit.rules      = "+str(self.rules.__name__)
        return ret

    def __repr__(self):
        """Prints the current representation of unit parameters including parent and ruleset.
        """
        ret = super(SubprocessUnit,self).__repr__()
        ret = "{" + _parentrepr.sub(ur'\1', ret)
        ret += ", 'rules': "+self.rules.__class__.__name__
#        ret += ", 'rules': "+str(self.rules.__name__)
        ret += "}"
        return ret
