Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
t = ()
t = tuple()
type(t)
<class 'tuple'>
t = (1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t = (1,2.3,'string',[1,2,3],{1,2,3},(1,2,3),{1:1,2:2},False}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
t = (1,2.3,'string',[1,2,3],{1,2,3},(1,2,3),{1:1,2:2},False)
t
(1, 2.3, 'string', [1, 2, 3], {1, 2, 3}, (1, 2, 3), {1: 1, 2: 2}, False)
l =(1,1,1,1,1)
l
(1, 1, 1, 1, 1)
a + b
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a + b
NameError: name 'a' is not defined
a =(1,2,3)
b = (4,5,6)
a + b
(1, 2, 3, 4, 5, 6)
a * 3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
a
(1, 2, 3)
t
(1, 2.3, 'string', [1, 2, 3], {1, 2, 3}, (1, 2, 3), {1: 1, 2: 2}, False)
t[1:4]
(2.3, 'string', [1, 2, 3])
t[-5:]
([1, 2, 3], {1, 2, 3}, (1, 2, 3), {1: 1, 2: 2}, False)
t[-3:]
((1, 2, 3), {1: 1, 2: 2}, False)
t[2]
'string'
t[-1]
False
'string' in s
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    'string' in s
NameError: name 's' is not defined
'string' in t
True
(1,2,3) in t
True
(7,8) in t
False
len(t)
8
t = (1,2,3,4,5,6,7,8)
max(t)
8
min(t)
1
sorted(t)
[1, 2, 3, 4, 5, 6, 7, 8]
>>> t.count(l)
0
>>> t.count(1)
1
>>> a,b = 1,2
>>> a
1
>>> b
2
>>> a = (1,2,3,4)
>>> w,x,y,z = a
>>> w
1
>>> x
2
>>> y
3
>>> z
4
>>> sum(a)
10
>>> a
(1, 2, 3, 4)
>>> t
(1, 2, 3, 4, 5, 6, 7, 8)
>>> t = (1,2,3,[4,5])
>>> t[3]
[4, 5]
>>> t[3].append(10)
>>> t
(1, 2, 3, [4, 5, 10])
>>> t[3].pop()
10
>>> t
(1, 2, 3, [4, 5])
