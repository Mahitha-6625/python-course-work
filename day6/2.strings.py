Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'python programming lang'
>>> s.startswith('p')
True
>>> s.startswith('P')
False
>>> s.endswith('.ing')
False
>>> s.endswith('lang')
True
>>> s.isalpha()
False
>>> 'afghrt'.isalpha()
True
>>> 'python3.14'.isalpha()
False
>>> 'pyThon'.isalpha()
True
>>> 'python'.alnum()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    'python'.alnum()
AttributeError: 'str' object has no attribute 'alnum'. Did you mean: 'isalnum'?
>>> 'python'.isalnum()
True
>>> '123456'.alnum()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    '123456'.alnum()
AttributeError: 'str' object has no attribute 'alnum'. Did you mean: 'isalnum'?
'123456'.isalnum()
True
'python'.isalnum()
True
'PYTHON'.isalnum()
True
'PYTHON'.isalnum()
True
'Python 123'.isalnum()
False
'Python.123'.isalnum()
False
'p'.islower()
True
'python'.islower()
True
'pYthon'.islower()
False
'pYthon'.isupper()
False
'python 123'.islower()
True
'PYTHON 123'.isupper()
True
'   '.isspace()
True
'python 123   '.isspace()
False
s
'python programming lang'
s.title()
'Python Programming Lang'
s.istitle()
False
'123myvar'.isindentifier()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    '123myvar'.isindentifier()
AttributeError: 'str' object has no attribute 'isindentifier'. Did you mean: 'isidentifier'?
'123myvar'.isidentifier()
False
'if'.isidentifier()
True
'12.3'.isdecimal()
False
'123'.isdecimal()
True
'12345'.isdigit()
True
'1/2'.isnumeric()
False
'五'.isnumeric()
True
'VIII'.isnumeric()
False
