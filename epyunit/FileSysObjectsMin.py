# -*- coding: utf-8 -*-
"""The 'FileSysObjectsMin' module provides basic file inheritance by directory hierarchies.  

This modules manages the file system based structure semantics for 
the automation of drop-in configurations. Therefore functions and classes
are provided for the modification of the search path and the location of
files and directories. Two examples are:

* The search for files and/or relative paths from a given 
    directory on upwards.
* The extension of search paths with any sub-directory portion 
    from a given directory on upwards.  

These two features already provide for basic inheritance 
features for files in directory hierarchies.

In addition this module supports for the location of files and 
file positions by means of the package 'inspect'.

**REMARK**: For the full set refer to the package:
PyFileSysObjects / https://pypi.python.org/pypi/PyFileSysObjects

"""
from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import os,sys
version = '{0}.{1}'.format(*sys.version_info[:2])
if version < '2.7': # pragma: no cover
    raise Exception("Requires Python-2.7.* or higher")

import inspect 


class FileSysObjectsMinException(Exception):
    pass

class FileSysObjectsMin:
    pass

def setUpperTreeSearchPath(start=None,top=None,plist=None):
    """Extends the search by sys.path for each subdir from 'start' on upward to 'top'.
    
    Prepends a set of search paths into sys.path. The set of search 
    paths contains of each directory beginning with provided start 
    position. This enables a "polymorphic inheritance view" onto the 
    file system structure.
    
    The typical application is the grouping of imported modules/classes
    for test cases by file-inheritance from upper tree. This provides 
    the hierarchical configuration and specialization of test cases 
    with pre-defined default components by multiple levels of 
    configuration files. 

    Args:
        start: Start directory.

            default := caller-file-position.
        
        top: End directory.
        
            default := start

        plist: List to for the storage.
        
            default := sys.path

    Returns:
        When successful returns 'True', else returns either 'False', or
        raises an exception.

    Raises:
        passed through exceptions:
    """
    if plist == None:
        plist = sys.path

    # 0. prep start dir
    if start == '':
        raise FileSysObjectsMinException("Empty top:''")
    elif start == None:
        start = getSourceFilePathName(2) # caller file
    s = os.path.abspath(start)
    if os.path.isfile(start):
        s = os.path.dirname(s) # we need dir
    if not os.path.exists(s):
        raise FileSysObjectsMinException("Missing start:"+str(s)) 

    # 1. prep top dir
    if top == '':
        raise FileSysObjectsMinException("Empty top:''")
    elif top == None:
        plist.insert(0,s)
        return True
    else:
        a = s.split(top)
        
        if len(a) == 1: # top is not in start
            raise FileSysObjectsMinException("Missing top:"+str(top))

        elif a == ['','']: # handles top==start
            plist.insert(0,top)
            return True
        
        elif len(a)>2: # multiple occurances, for not not supported
            raise FileSysObjectsMinException("Ambigious top:"+str(top)) # top more than once in start
        
        else: # exactly 2 - one only
            
            if a[0] == '': # top was prefix
                a = a[1]
                curp = top
                plist.insert(0,curp)
                a = a.split(os.sep)
            
                for p in a:
                    curp = os.path.join(curp,p)
                    if p != '':
                        curp += os.sep
                    plist.insert(0,curp)

            else: # actual top
                curp = os.path.normpath(a[0]+os.sep+top)
                plist.insert(0,curp)

                a = a[1].split(os.sep)
                            
                for p in a:
                    if not p:
                        continue
                    curp = os.path.join(curp,p)
                    if p != '':
                        curp += os.sep
                    plist.insert(0,curp)

    return True

def findRelPathInUpperTree(object,plist=None):
    """Searches the upper tree path list for matching objects in side-branches.
    
    Args:
        object: A relative path to a directory or file.
                Some examples are 'myscript.sh', 'epyunit/myscript.sh', or
                'bin/epyunit'.

        plist: List with path entries to search each, first match wins.
        
            default := sys.path

    Returns:
        When successful returns the absolute pathname, else 'None'.

    Raises:
        passed through exceptions:
    """
    if plist == None:
        plist = sys.path
    for p in plist:
        if os.path.exists(p+os.sep+object):
            return os.path.normpath(os.path.abspath(p+os.sep+object))

    return None

def getSourceFilePathName(spos=1):
    """Returns the pathname of caller source file.

    Args:
        spos: Start position in the stack.

    Returns:
        Returns the filepathname.

    Raises:
        passed through exceptions:
    """
    return inspect.stack()[spos][1]

def getSourceFuncName(spos=1):
    """Returns the name of caller function.

    Args:
        spos: Start position in the stack.

    Returns:
        Returns the filepathname.

    Raises:
        passed through exceptions:
    """
    return inspect.stack()[spos][3]

def getSourceLinenumber(spos=1):
    """Returns the line number of caller.

    Args:
        spos: Start position in the stack.

    Returns:
        Returns the filepathname.

    Raises:
        passed through exceptions:
    """
    return inspect.stack()[spos][2]

def getCallerName(spos=1):
    """Returns the name of the caller.

    Args:
        spos: Start position in the stack.

    Returns:
        Returns the filepathname.

    Raises:
        passed through exceptions:
    """
    return inspect.stack()[spos][0].f_globals['__name__']

def getCallerNameOID(spos=1):
    """Returns the name of the package containing the caller.

    Args:
        spos: Start position in the stack.

    Returns:
        Returns the package name.

    Raises:
        passed through exceptions:
    """
    
    #def caller_name(skip=2):
    """Get a name of a caller in the format module.class.method
    `skip` specifies how many levels of stack to skip while getting caller
    name. skip=1 means "who calls me", skip=2 "who calls my caller" etc.
    An empty string is returned if skipped levels exceed stack height
    """
    _spos = spos
    _sf = inspect.stack()
    if len(_sf) < _spos:
        return None
    _pf = _sf[_spos][0]
    _coid = inspect.getmodule(_pf)
    if _coid:
        _coid = _coid.__name__
    if 'self' in _pf.f_locals:
        _coid += "." + str(_pf.f_locals['self'].__class__.__name__)
    if _pf.f_code.co_name != '<module>':
        _coid += "." + str(_pf.f_code.co_name)
    del _pf
    return _coid

def getCallerPackageName(spos=1):
    """Returns the name of the package containing the caller.

    Args:
        spos: Start position in the stack.

    Returns:
        Returns the package name when defined, else None.

    Raises:
        passed through exceptions:
    """
    _sf = inspect.stack()
    if len(_sf) < spos:
        return None
    module = inspect.getmodule(_sf[spos][0])
    if module:
        return module.__package__
    
def getCallerPackagePathName(spos=1):
    """Returns the pathname to the package directory of the caller.

    Args:
        spos: Start position in the stack.

    Returns:
        Returns the path name to the package.

    Raises:
        passed through exceptions:
    """
    _sf = inspect.stack()
    if len(_sf) < spos:
        return None
    module = inspect.getmodule(_sf[spos][0])
    if module:
        if module.__package__:
            #FIXME: zip-files
            return getCallerModulePathName(spos+1)

def getCallerPackagePythonPath(spos=1):
    """Returns the pathname to the package directory of the caller.

    Intentionally the same as 'getCallerPackagePathName'.
 
    Args:
        spos: Start position in the stack.

    Returns:
        Returns the path name to the package.

    Raises:
        passed through exceptions:
    """
    return os.path.dirname(getCallerPackagePathName(spos+1))

def getCallerPackageFilePathName(spos=1):
    """Returns the name of the package containing the caller.

    Args:
        spos: Start position in the stack.

    Returns:
        Returns the package name.

    Raises:
        passed through exceptions:
    """
    return os.path.dirname(getCallerModuleFilePathName(spos+1))

def getCallerModuleFilePathName(spos=1):
    """Returns the filepathname of the module.

    Args:
        spos: Start position in the stack.

    Returns:
        Returns the filepathname of the caller module.

    Raises:
        passed through exceptions:
    """
    
    _sf = inspect.stack()
    if len(_sf) < spos:
        return None
    module = inspect.getmodule(_sf[spos][0])
    if module:
        return module.__file__

def getCallerModuleName(spos=1):
    """Returns the name of the caller module.

    Args:
        spos: Module name.

    Returns:
        Returns the name of caller module.
        The dotted object path is relative to 
        the actual used sys.path item.  

    Raises:
        passed through exceptions:
    """
    _sf = inspect.stack()
    if len(_sf) < spos:
        return None
    module = inspect.getmodule(_sf[spos][0])
    if module:
        return module.__name__

def getCallerModulePythonPath(spos=1):
    """Returns the prefix item from sys.path used for the caller module.

    Args:
        spos: Module name.

    Returns:
        Returns the name of caller module.

    Raises:
        passed through exceptions:
    """
    _mn = getCallerModuleName(spos+1).split('.')[:-1]
    _mn = os.sep.join(_mn)
    _r = getCallerModulePathName(spos+1).split(_mn)[0]
    if _r[-1] != os.sep: # was rel for split
        _r += os.sep
    return _r    

def getCallerModulePathName(spos=1):
    """Returns the pathname of the module.

    Args:
        m: Module name.

    Returns:
        Returns the filepathname of module.

    Raises:
        passed through exceptions:
    """
    return os.path.dirname(getCallerModuleFilePathName(spos+1))+os.sep

def getPythonPathPrefixMatchFromSysPath(pname,plist=None):
    """Gets the first matching prefix from sys.path.
    
    Foreseen to be used for canonical base reference in unit tests.
    This enables in particular for casual tests where absolute pathnames
    are required.

    Args:
        pname: Pathname.

    Returns:
        Returns the first matching path prefix from sys.path.

    Raises:
        passed through exceptions:
    """
    if not plist:
        plist = sys.path
    for sp in plist:
        if pname.startswith(sp):
            if sp and sp[-1] == os.sep:
                return sp
            return sp+os.sep

def getPythonPathModuleRel(fpname,plist=None):
    """Returns the relative path name of the filepathname.

    Args:
        fpname: The filepathname.

    Returns:
        Returns the path prefix for fpname.

    Raises:
        passed through exceptions:
    """
    if not plist:
        plist = sys.path
    for _sp in plist:
        if fpname.startswith(_sp):
            _r = fpname.replace(_sp,"")
            if _r and _r[0] == os.sep:
                return _r[1:]
            return _r

def getPythonPathForPackage(pname,plist=None):
    """Returns the item from sys.path for package.

    ATTENTION: This version relies on the common
        naming convention of pathnames.

    Args:
        pname: The name of the package.

    Returns:
        Returns the path item.

    Raises:
        passed through exceptions:
    """
    if not plist:
        plist = sys.path    
    _pn = pname.replace('.',os.sep)
    for _sp in sys.path:
        _pp = _sp.split(pname)
        if len(_pp) > 1:
            return _pp[0]
