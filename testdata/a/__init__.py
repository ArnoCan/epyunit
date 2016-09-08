"""
Common test data for Use-Cases
==============================
Common data for 'UseCases' and 'tests'. Refer to the package by PYTHONPATH.
The global variable 'testdata.mypath' provides the pathname into 'testdata'.

The following directory tree is provided:
  ::

     testdata
     `a
      |-- a.sh
      |-- a.smod
      |-- A.txt
      |-- b
      |   |-- b.pl
      |   |-- b.pm
      |   |-- b.pod
      |   |-- b.py
      |   |-- b.pyc
      |   |-- b.sh
      |   |-- b.smod
      |   |-- B.txt
      |   |-- c
      |   |   |-- c.pl
      |   |   |-- c.pm
      |   |   |-- c.pod
      |   |   |-- c.py
      |   |   |-- c.pyc
      |   |   |-- c.sh
      |   |   |-- c.smod
      |   |   |-- C.txt
      |   |   |-- d
      |   |   |   |-- d.pl
      |   |   |   |-- d.pm
      |   |   |   |-- d.pod
      |   |   |   |-- d.py
      |   |   |   |-- d.pyc
      |   |   |   |-- d.sh
      |   |   |   |-- d.smod
      |   |   |   |-- D.txt
      |   |   |   |-- __init__.py
      |   |   |   `-- __init__.pyc
      |   |   |-- __init__.py
      |   |   `-- __init__.pyc
      |   |-- __init__.py
      |   |-- __init__.pyc
      |   `-- libb.sh
      |-- b0
      |   |-- b0.pl
      |   |-- b0.pm
      |   |-- b0.pod
      |   |-- b0.py
      |   |-- b0.pyc
      |   |-- b0.sh
      |   |-- b0.smod
      |   |-- B.txt
      |   |-- c
      |   |   |-- c.pl
      |   |   |-- c.pm
      |   |   |-- c.pod
      |   |   |-- c.py
      |   |   |-- c.pyc
      |   |   |-- c.sh
      |   |   |-- c.smod
      |   |   |-- C.txt
      |   |   |-- d
      |   |   |   |-- d.pl
      |   |   |   |-- d.pm
      |   |   |   |-- d.pod
      |   |   |   |-- d.py
      |   |   |   |-- d.pyc
      |   |   |   |-- d.sh
      |   |   |   |-- d.smod
      |   |   |   |-- D.txt
      |   |   |   |-- __init__.py
      |   |   |   `-- __init__.pyc
      |   |   |-- __init__.py
      |   |   `-- __init__.pyc
      |   |-- __init__.py
      |   |-- __init__.pyc
      |   `-- libb0.sh
      |-- b1
      |   |-- b1.pl
      |   |-- b1.pm
      |   |-- b1.pod
      |   |-- b1.py
      |   |-- b1.pyc
      |   |-- b1.sh
      |   |-- b1.smod
      |   |-- B1.txt
      |   |-- c1
      |   |   |-- c1.pl
      |   |   |-- c1.pm
      |   |   |-- c1.pod
      |   |   |-- c1.py
      |   |   |-- c1.pyc
      |   |   |-- c1.sh
      |   |   |-- c1.smod
      |   |   |-- C1.txt
      |   |   |-- d1
      |   |   |   |-- d1.pl
      |   |   |   |-- d1.pm
      |   |   |   |-- d1.pod
      |   |   |   |-- d1.py
      |   |   |   |-- d1.pyc
      |   |   |   |-- d1.sh
      |   |   |   |-- d1.smod
      |   |   |   |-- D1.txt
      |   |   |   |-- __init__.py
      |   |   |   `-- __init__.pyc
      |   |   |-- __init__.py
      |   |   `-- __init__.pyc
      |   |-- __init__.py
      |   |-- __init__.pyc
      |   `-- libb1.sh
      |-- b2
      |   |-- b2.pl
      |   |-- b2.pm
      |   |-- b2.pod
      |   |-- b2.py
      |   |-- b2.pyc
      |   |-- b2.sh
      |   |-- b2.smod
      |   |-- B.txt
      |   |-- c
      |   |   |-- c.pl
      |   |   |-- c.pm
      |   |   |-- c.pod
      |   |   |-- c.py
      |   |   |-- c.pyc
      |   |   |-- c.sh
      |   |   |-- c.smod
      |   |   |-- C.txt
      |   |   |-- d
      |   |   |   |-- d.pl
      |   |   |   |-- d.pm
      |   |   |   |-- d.pod
      |   |   |   |-- d.py
      |   |   |   |-- d.pyc
      |   |   |   |-- d.sh
      |   |   |   |-- d.smod
      |   |   |   |-- D.txt
      |   |   |   |-- __init__.py
      |   |   |   `-- __init__.pyc
      |   |   |-- __init__.py
      |   |   `-- __init__.pyc
      |   |-- c0
      |   |   |-- c0.pl
      |   |   |-- c0.pm
      |   |   |-- c0.pod
      |   |   |-- c0.py
      |   |   |-- c0.pyc
      |   |   |-- c0.sh
      |   |   |-- c0.smod
      |   |   |-- C.txt
      |   |   |-- d
      |   |   |   |-- d.pl
      |   |   |   |-- d.pm
      |   |   |   |-- d.pod
      |   |   |   |-- d.py
      |   |   |   |-- d.pyc
      |   |   |   |-- d.sh
      |   |   |   |-- d.smod
      |   |   |   |-- D.txt
      |   |   |   |-- __init__.py
      |   |   |   `-- __init__.pyc
      |   |   |-- __init__.py
      |   |   `-- __init__.pyc
      |   |-- c1
      |   |   |-- c1.pl
      |   |   |-- c1.pm
      |   |   |-- c1.pod
      |   |   |-- c1.py
      |   |   |-- c1.pyc
      |   |   |-- c1.sh
      |   |   |-- c1.smod
      |   |   |-- C.txt
      |   |   |-- d1
      |   |   |   |-- d1.pl
      |   |   |   |-- d1.pm
      |   |   |   |-- d1.pod
      |   |   |   |-- d1.py
      |   |   |   |-- d1.pyc
      |   |   |   |-- d1.sh
      |   |   |   |-- d1.smod
      |   |   |   |-- D.txt
      |   |   |   |-- __init__.py
      |   |   |   `-- __init__.pyc
      |   |   |-- __init__.py
      |   |   `-- __init__.pyc
      |   |-- c2
      |   |   |-- c2.pl
      |   |   |-- c2.pm
      |   |   |-- c2.pod
      |   |   |-- c2.py
      |   |   |-- c2.pyc
      |   |   |-- c2.sh
      |   |   |-- c2.smod
      |   |   |-- C.txt
      |   |   |-- d
      |   |   |   |-- D1.txt
      |   |   |   |-- D2.txt
      |   |   |   |-- d.pl
      |   |   |   |-- d.pm
      |   |   |   |-- d.pod
      |   |   |   |-- d.py
      |   |   |   |-- d.pyc
      |   |   |   |-- d.sh
      |   |   |   |-- d.smod
      |   |   |   |-- D.txt
      |   |   |   |-- __init__.py
      |   |   |   `-- __init__.pyc
      |   |   |-- __init__.py
      |   |   `-- __init__.pyc
      |   |-- __init__.py
      |   |-- __init__.pyc
      |   `-- libb2.sh
      |-- b3
      |   |-- libb0.sh
      |   |-- libb3
      |   |   |-- a.sh
      |   |   |-- b.sh
      |   |   `-- libb3.sh
      |   |-- libb4
      |   |   |-- a.sh
      |   |   |-- b.sh
      |   |   `-- hook.sh
      |   `-- smods
      |       |-- a
      |       |   |-- a.smod
      |       |   |-- b.smod
      |       |   |-- c
      |       |   |   |-- a.smod
      |       |   |   |-- help.smod
      |       |   |   |-- h.smod
      |       |   |   `-- self.smod
      |       |   |-- help.smod
      |       |   |-- h.smod
      |       |   `-- self.smod
      |       |-- a.smod
      |       |-- b
      |       |   |-- c
      |       |   |   |-- a.smod
      |       |   |   |-- help.smod
      |       |   |   |-- h.smod
      |       |   |   `-- self.smod
      |       |   |-- c.smod
      |       |   |-- help.smod
      |       |   |-- h.smod
      |       |   `-- self.smod
      |       |-- b.smod
      |       |-- c
      |       |   |-- c
      |       |   |   |-- a.smod
      |       |   |   |-- d
      |       |   |   |   |-- a.smod
      |       |   |   |   |-- e
      |       |   |   |   |   |-- a.smod
      |       |   |   |   |   |-- help.smod
      |       |   |   |   |   |-- h.smod
      |       |   |   |   |   `-- self.smod
      |       |   |   |   |-- help.smod
      |       |   |   |   |-- h.smod
      |       |   |   |   `-- self.smod
      |       |   |   |-- help.smod
      |       |   |   |-- h.smod
      |       |   |   `-- self.smod
      |       |   |-- c.smod
      |       |   |-- d
      |       |   |   |-- a.smod
      |       |   |   |-- help.smod
      |       |   |   |-- h.smod
      |       |   |   `-- self.smod
      |       |   |-- help.smod
      |       |   |-- h.smod
      |       |   `-- self.smod
      |       `-- c.smod
      |-- __init__.py
      `-- __init__.pyc

"""

