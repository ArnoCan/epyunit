"""Distribute 'epyunit', a generic unit test wrapper for commandline interfaces.

   Installs 'epyunit', adds/modifies the following helper features to standard
   'setuptools' options.

   Args:
      build_doc: Creates Sphinx based documentation with embeded javadoc-style
          API documentation, html only.

      build_sphinx: Creates documentation for runtime system by Sphinx, html only.
         Calls 'callDocSphinx.sh'.

      build_epydoc: Creates standalone documentation for runtime system by Epydoc, 
         html only.

      project_doc: Install a local copy into the doc directory of the project.

      instal_doc: Install a local copy of the previously build documents in 
          accordance to PEP-370.

      test: Runs PyUnit tests by discovery.

      usecases: Runs PyUnit UseCases by discovery, a lightweight
          set of unit tests.

      --no-install-required: Suppresses installation dependency checks, 
          requires appropriate PYTHONPATH.
      --offline: Sets online dependencies to offline, or ignores online
          dependencies.

      --exit: Exit 'setup.py'.

      --help-filesysobjects: Displays this help.

   Returns:
      Results for success in installed 'epyunit'.

   Raises:
      ffs.

"""
# priority is offline here - needs manual 'bootstrap', thus dropped ez_setup for now
# import ez_setup
# ez_setup.use_setuptools()

#import sys
#from polybori.plot import THEN

#
#*** common source header
#
__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.12'
__uuid__='9de52399-7752-4633-9fdc-66c87a9200b8'

_NAME = 'epyunit'

# some debug
if __debug__:
    __DEVELTEST__ = True

#
#***
#
import os,sys
from setuptools import setup #, find_packages
import fnmatch
import re, shutil, tempfile


#
#*** ===>>> setup.py helper
#
def find_files(srcdir, *wildcards, **kw):
    """Assembles a list of package files for package_files.

        Args:
            srcdir: Source root.
            *wildcards: list of globs.
            **kw: Additional control of resolution:
                single_level: Flat only.
                subpath: Cut topmost path elements from listelements,
                    special for dictionaries.
                nopostfix: Drop filename postfix.
                packages: List packages only, else files.
                yield_folders:
        Returns:
            Results in an list.

        Raises:
            ffs.

    """
    def all_files(root, *patterns, **kw):
        ret=[]
        single_level = kw.get('single_level', False)
        subpath = kw.get('subpath', False)
        nopostfix = kw.get('nopostfix', True)
        packages = kw.get('packages', True)
        yield_folders = kw.get('yield_folders', True)

        for path, subdirs, files in os.walk(root):
            if yield_folders:
                files.extend(subdirs)
            files.sort( )

            if subpath:
                path=re.sub(r'^[^'+os.sep+']*'+os.sep, '',path)

            for name in files:
                if name in ('.gitignore', '.git', '.svn'):
                    continue

                for pattern in patterns:
                    if fnmatch.fnmatch(name, pattern):
                        if packages:
                            if not name == '__init__.py':
                                continue
                            ret.append(path)
                            continue
                        if nopostfix:
                            name=os.path.splitext(name)[0]

                        ret.append(os.path.join(path, name))

            if single_level:
                break
        return ret

    file_list = all_files(srcdir, *wildcards,**kw)
    return file_list

def usage():
    if __name__ == '__main__':
        import pydoc
        #FIXME: literally displayed '__main__'
        print pydoc.help(__name__)
    else:
        help(str(os.path.basename(sys.argv[0]).split('.')[0]))

#
#* shortcuts
#

exit_code = 0

# custom doc creation by sphinx-apidoc
if 'build_sphinx' in sys.argv or 'build_doc' in sys.argv:
    try:
        os.makedirs('build'+os.sep+'apidoc'+os.sep+'sphinx')
    except:
        pass

    print "#---------------------------------------------------------"
    exit_code = os.system('./callDocSphinx.sh') # create apidoc
    print "#---------------------------------------------------------"
    print "Called/Finished callDocSphinx.sh => exit="+str(exit_code)
    if 'build_sphinx' in sys.argv:
        sys.argv.remove('build_sphinx')

# common locations
src0 = os.path.normpath("build/apidoc/sphinx/_build/html")
dst0 = os.path.normpath("build/apidoc/"+str(_NAME))    

# custom doc creation by sphinx-apidoc with embeded epydoc
if 'build_doc' in sys.argv:

    # copy sphinx to mixed doc
    if not os.path.exists(src0):
        raise Exception("Missing generated sphinx document source:"+str(src0))
    if os.path.exists(dst0):
        shutil.rmtree(dst0)
    shutil.copytree(src0, dst0)
    
    print "#---------------------------------------------------------"
    exit_code = os.system('epydoc --config docsrc/epydoc.conf') # create apidoc
    print "#---------------------------------------------------------"
    print "Called/Finished epydoc --config docsrc/epydoc.conf => exit="+str(exit_code)

    def _sed(filename, pattern, repl, flags=0):
        pattern_compiled = re.compile(pattern,flags)
        fname = os.path.normpath(filename)
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as ftmp:
            with open(fname) as src_file:
                for line in src_file:
                    ftmp.write(pattern_compiled.sub(repl, line))
    
        shutil.copystat(fname, ftmp.name)
        shutil.move(ftmp.name, fname)


    pt = '<a target="moduleFrame" href="toc-everything.html">Everything</a>'
    rp  = r'<a href="../index.html" target="_top">Home</a>'
    rp += r' - '
    rp += r'<a href="./index.html" target="_top">Top</a>'
    rp += r' - '
    rp += pt

    fn = dst0+'/epydoc/toc.html'
    _sed(fn, pt, rp, re.MULTILINE)

    pt = '<h4>Next topic</h4>'
    rp  = r'<h4>API</h4><p class="topless"><a href="epydoc/index.html" title="API">Programming Interface - Epydoc</a></p>'
    rp += pt

    fn = dst0+'/index.html'
    _sed(fn, pt, rp, re.MULTILINE)

    pt = '<h4>Previous topic</h4>'
    rp  = r'<h4>API</h4><p class="topless"><a href="epydoc/index.html" title="API">Programming Interface - Epydoc</a></p>'
    rp += pt


    patchlist = [
        'usecases.html',
        'rules_logic.html',
        'shortcuts.html',
        'rules_shortcuts.html',
        'subprocessunit.html',
        'epyunit.html',
        'systemcalls.html',
        'software_design.html',
    ]
    for px in patchlist:
        fn = dst0+os.sep+px
        _sed(fn, pt, rp, re.MULTILINE)
    
    sys.argv.remove('build_doc')

  

# custom doc creation by epydoc
if 'build_epydoc' in sys.argv:
    try:
        os.makedirs('build'+os.sep+'apidoc'+os.sep+'epydoc')
    except:
        pass
    
    print "#---------------------------------------------------------"
    exit_code = os.system('epydoc --config docsrc/epydoc-standalone.conf') # create apidoc
    print "#---------------------------------------------------------"
    print "Called/Finished epydoc --config docsrc/epydoc-standalone.conf => exit="+str(exit_code)
    sys.argv.remove('build_epydoc')


# install local project doc
if 'project_doc' in sys.argv:
    print "# project_doc.sh..."

    dstroot = os.path.normpath("doc/en/html/man3/")+os.sep
    
    try:
        os.makedirs(dstroot)
    except:
        pass

    if os.path.exists(dst0):
        if os.path.exists(dstroot+str(_NAME)):
            shutil.rmtree(dstroot+str(_NAME))
        shutil.copytree(dst0, dstroot+str(_NAME))


    src0 = os.path.normpath("build/apidoc/sphinx/_build/html")
    if os.path.exists(src0):
        if os.path.exists(dstroot+str(_NAME)+".sphinx"):
            shutil.rmtree(dstroot+str(_NAME)+".sphinx")
        shutil.copytree(src0, dstroot+str(_NAME)+".sphinx")

    src0 = os.path.normpath("build/apidoc/epydoc")
    if os.path.exists(src0):
        if os.path.exists(dstroot+str(_NAME)+".epydoc"):
            shutil.rmtree(dstroot+str(_NAME)+".epydoc")
        shutil.copytree(src0, dstroot+str(_NAME)+".epydoc")

    print "#"
    idx = 0
    for i in sys.argv: 
        if i == 'install_doc': break
        idx += 1
    
    print "#"
    print "Called/Finished PyUnit tests => exit="+str(exit_code)
    print "exit setup.py now: exit="+str(exit_code)
    sys.argv.remove('project_doc')

# install user doc
if 'install_doc' in sys.argv:
    print "# install_doc.sh..."

    # set platform
    if sys.platform in ('win32'):
        dstroot = os.path.expandvars("%APPDATA%/Python/doc/en/html/man3/")
    else:
        dstroot = os.path.expanduser("~/.local/doc/en/html/man3/")
    dstroot = os.path.normpath(dstroot)+os.sep
    
    try:
        os.makedirs(dstroot)
    except:
        pass

    if os.path.exists(dst0):
        if os.path.exists(dstroot+str(_NAME)):
            shutil.rmtree(dstroot+str(_NAME))
        shutil.copytree(dst0, dstroot+str(_NAME))


    src0 = os.path.normpath("build/apidoc/sphinx/_build/html")
    if os.path.exists(src0):
        if os.path.exists(dstroot+str(_NAME)+".sphinx"):
            shutil.rmtree(dstroot+str(_NAME)+".sphinx")
        shutil.copytree(src0, dstroot+str(_NAME)+".sphinx")

    src0 = os.path.normpath("build/apidoc/epydoc")
    if os.path.exists(src0):
        if os.path.exists(dstroot+str(_NAME)+".epydoc"):
            shutil.rmtree(dstroot+str(_NAME)+".epydoc")
        shutil.copytree(src0, dstroot+str(_NAME)+".epydoc")

    print "#"
    idx = 0
    for i in sys.argv: 
        if i == 'install_doc': break
        idx += 1
    
    print "#"
    print "Called/Finished PyUnit tests => exit="+str(exit_code)
    print "exit setup.py now: exit="+str(exit_code)
    sys.argv.remove('install_doc')

# call of complete test suite by 'discover'
if 'tests' in sys.argv or 'test' in sys.argv:
    if os.path.dirname(__file__)+os.pathsep not in os.environ['PATH']:
        p0 = os.path.dirname(__file__)
        os.putenv('PATH', p0+os.pathsep+os.getenv('PATH',''))
        print "# putenv:PATH[0]="+str(p0)
    
    print "#"
    print "# REMINDER: Do not forget to start the PyDev/Eclipse RemoteDebugServer"
    print "#"
    print "# Check 'inspect' paths - call in: tests"
    exit_code  = os.system('python -m unittest discover -s tests -p CallCase.py') # traverse tree
    print "# Check 'inspect' paths - call in: tests.libs"
    exit_code += os.system('python -m unittest discover -s tests.libs -p CallCase.py') # traverse tree
    print "# Check 'inspect' paths - call in: tests.libs.SystemCalls"
    exit_code += os.system('python -m unittest discover -s tests.libs.SystemCalls -p CallCase.py') # traverse tree
    print "#"
    print "Called/Finished PyUnit tests => exit="+str(exit_code)
    print "exit setup.py now: exit="+str(exit_code)
    try:
        sys.argv.remove('test')
    except:
        pass
    try:
        sys.argv.remove('tests')
    except:
        pass
    

# call of complete UseCases by 'discover'
if 'usecases' in sys.argv or 'usecase' in sys.argv:
    if os.path.dirname(__file__)+os.pathsep not in os.environ['PATH']:
        p0 = os.path.dirname(__file__)
        os.putenv('PATH', p0+os.pathsep+os.getenv('PATH',''))
        print "# putenv:PATH[0]="+str(p0)
    
    print "#"
    print "# REMINDER: Do not forget to start the PyDev/Eclipse RemoteDebugServer"
    print "#"
    print "#"
    print "# Check 'inspect' paths - call in: UseCases"
    exit_code = os.system('python -m unittest discover -s UseCases -p CallCase.py') # traverse tree
    print "#"
    print "Called/Finished PyUnit tests => exit="+str(exit_code)
    print "exit setup.py now: exit="+str(exit_code)
    try:
        sys.argv.remove('usecase')
    except:
        pass
    try:
        sys.argv.remove('usecases')
    except:
        pass

# # call of complete test suite by 'discover'
# if 'test' in sys.argv:
#     print "#"
#     exit_code = os.system('python -m unittest discover -s tests -p CallCase.py') # traverse tree
#     print "#"
#     print "Called/Finished PyUnit tests => exit="+str(exit_code)
#     print "exit setup.py now: exit="+str(exit_code)
#     sys.argv.remove('test')

# Intentional HACK: ignore (online) dependencies, mainly foreseen for developement
__no_install_requires = False
if '--no-install-requires' in sys.argv:
    __no_install_requires = True
    sys.argv.remove('--no-install-requires')

# Intentional HACK: offline only, mainly foreseen for developement
__offline = False
if '--offline' in sys.argv:
    __offline = True
    __no_install_requires = True
    sys.argv.remove('--offline')

# Execution failed - Error.
if exit_code != 0:
    sys.exit(exit_code)

# Help on addons.
if '--help-epyunit' in sys.argv:
    usage()
    sys.exit(0)

# Exit here.
if '--exit' in sys.argv:
    sys.exit(0)

# if epyunit-specials only
if len(sys.argv)==1:
    sys.exit(exit_code)

#
#*** <<<=== setup.py helper
#


#
#*** setup.py configuration
#
_name='epyunit'

_description=("The 'epyunit' package provides a wrapper for unit tests of commandline interfaces, " 
              "and the automation of debugging with PyDev for external processes. "
              "The package could be used either from the comandline, or integrated into Eclipse "
              "with PyDev."
              )

# def read(fname):
#     return open(os.path.join(os.path.dirname(__file__), fname)).read()
_README = os.path.join(os.path.dirname(__file__), 'README')
_long_description = open(_README).read() + 'nn'

_platforms='any'

_classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: Free To Use But Restricted",
    "License :: OSI Approved :: Artistic License",
    "Natural Language :: English",
    "Operating System :: Microsoft :: Windows :: Windows 7",
    "Operating System :: OS Independent",
    "Operating System :: POSIX :: BSD :: OpenBSD",
    "Operating System :: POSIX :: Linux",
    "Operating System :: POSIX",
    "Operating System :: MacOS :: MacOS X",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",    
    "Programming Language :: Python :: 2.7",    
    "Programming Language :: Unix Shell",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities",
]

_keywords  = ' Python PyUnit PyDev Eclipse CLI command line'
_keywords += ' test unit unittest regression regressiontest fileobjects commandline'
_keywords += ' debug pydevd.py automation'

_packages = ["epyunit"]
_scripts = ["bin/epyunit", ]

_package_data = {
    'epyunit': ['README','ArtisticLicense20.html', 'licenses-amendments.txt',
                'myscript.sh',
            ],
}

#_download_url="https://github.com/ArnoCan/epyunit/"
_download_url="https://sourceforge.net/projects/epyunit/files/"

_url='https://sourceforge.net/projects/epyunit/'

_install_requires=[
    'inspect',
    're',
    'glob',
    'subprocess',
    'pyfilesysobjects',
    'pysourceinfo',
#    'termcolor'
]

_test_suite="tests.CallCase"

if __debug__:
    if __DEVELTEST__:
        print "#---------------------------------------------------------"
        print "packages="+str(_packages)
        print "#---------------------------------------------------------"
        print "package_data="+str(_package_data)
        print "#---------------------------------------------------------"



#
#*** ===>>> setup.py helper
#

# Intentional HACK: ignore (online) dependencies, mainly foreseen for developement
if __no_install_requires:
    print "#"
    print "# Changed to offline mode, ignore install dependencies completely."
    print "# Requires appropriate PYTHONPATH."
    print "# Ignored dependencies are:"
    print "#"
    for ir in _install_requires:
        print "#   "+str(ir)
    print "#"
    _install_requires=[]

#
#*** <<<=== setup.py helper
#


#
#*** do it now...
#
setup(name=_name,
      version=__version__,
      author=__author__,
      author_email=__author_email__,
      classifiers=_classifiers,
      description=_description,
      download_url=_download_url,
      install_requires=_install_requires,
      keywords=_keywords,
      license=__license__,
      long_description=_long_description,
      platforms=_platforms,
      url=_url,
      scripts=_scripts,
      packages=_packages,
      package_data=_package_data
)
