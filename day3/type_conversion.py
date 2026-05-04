Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> type(a)
<class 'int'>
>>> float(a)
10.0
>>> complex(a)
(10+0j)
>>> str(a)
'10'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> bool(a)
True
>>> #float conversion
>>> b = 5.0
>>> int(b)
5
>>> complex(b)
(5+0j)
>>> str(b)
'5.0'
>>> list(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
>>> tuble(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuble(b)
NameError: name 'tuble' is not defined. Did you mean: 'tuple'?
>>> tuple(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
>>> set(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
>>> dict(b)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
c = 7i + 8j
SyntaxError: invalid decimal literal
c = 7 + 8j
type(c)
<class 'complex'>
int(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(7+8j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
bool(c)
True
#list
l = [1,2,3]
int(l)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(list)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    complex(list)
TypeError: complex() first argument must be a string or a number, not 'type'
str(l)
'[1, 2, 3]'
tuple(l)
(1, 2, 3)
set(l)
{1, 2, 3}
dict(l)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
str = "python"
int(str)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    int(str)
ValueError: invalid literal for int() with base 10: 'python'
d = '1'
int(d)
1
float(d)
1.0
complex(d)
(1+0j)
list(d)
['1']
list(str)
['p', 'y', 't', 'h', 'o', 'n']
tuple(str)
('p', 'y', 't', 'h', 'o', 'n')
set(str)
{'t', 'n', 'h', 'y', 'o', 'p'}
dict(str)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    dict(str)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(str)
True
#tuple
tup
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    tup
NameError: name 'tup' is not defined

s = (2,3)
int(s)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(s)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(s)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'tuple'
str(s)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    str(s)
TypeError: 'str' object is not callable
str(s)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    str(s)
TypeError: 'str' object is not callable
list(s)
[2, 3]
set(s)
{2, 3}
dict(s)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(s)
True
#set
e = { 1,2,2}
e
{1, 2}
int(e)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    int(e)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(e)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    float(e)
TypeError: float() argument must be a string or a real number, not 'set'
complex(e)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    complex(e)
TypeError: complex() first argument must be a string or a number, not 'set'
list(e)
[1, 2]
tuple(e)
(1, 2)
dict(e)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    dict(e)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(e)
True
dict = {"Name: "xy"}
        
SyntaxError: unterminated string literal (detected at line 1)
dict = {"name": 'xy'}
        
int(dict)
        
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    int(dict)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(dict)
        
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    float(dict)
TypeError: float() argument must be a string or a real number, not 'dict'
str(dict)
        
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    str(dict)
TypeError: 'str' object is not callable
complex(dict)
        
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    complex(dict)
TypeError: complex() first argument must be a string or a number, not 'dict'
list(dict)
        
['name']
tuple(dict)
        
('name',)
set(dict)
        
{'name'}
bool(dict)
        
True
a = True
        
int(a)
        
1
float(a)
        
1.0
complex(a)
        
(1+0j)
list(a)
        
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    list(a)
TypeError: 'bool' object is not iterable
tuple(a)
        
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    tuple(a)
TypeError: 'bool' object is not iterable
set(a)
        
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    set(a)
TypeError: 'bool' object is not iterable
dict(a)
        
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    dict(a)
TypeError: 'dict' object is not callable
