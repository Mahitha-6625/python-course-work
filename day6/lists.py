Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
l = [1,2,3,3]
l
[1, 2, 3, 3]
l = []
type(l)
<class 'list'>
l = [6,9.0,'fghd', [], {}, {1:},True]
SyntaxError: expression expected after dictionary key and ':'
l = [6,9.0,'fghd', [], {}, {1:1},True]
l
[6, 9.0, 'fghd', [], {}, {1: 1}, True]
a=[1,2,3,4]
b = [5,6,7,8]
c = a + b
c
[1, 2, 3, 4, 5, 6, 7, 8]
a * 8
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
names = ['mahitha','bhavana','dhatri']
names
['mahitha', 'bhavana', 'dhatri']
names[0]
'mahitha'
names[2]
'dhatri'
names[1]
'bhavana'
names[-1]
'dhatri'
names[-2]
'bhavana'
names[-3]
'mahitha'
names.append('sreeya')
names
['mahitha', 'bhavana', 'dhatri', 'sreeya']
names[1:3]
['bhavana', 'dhatri']
names[::2]
['mahitha', 'dhatri']
names[::1]
['mahitha', 'bhavana', 'dhatri', 'sreeya']
names[-3:]
['bhavana', 'dhatri', 'sreeya']
names[:3]
['mahitha', 'bhavana', 'dhatri']
'mahitha' in names
True
'bhavana' not in names
False
len(names)
4
max(names)
'sreeya'
min(names)
'bhavana'
names[1] = 'Bhavana'
names[0] = 'Mahitha'
names
['Mahitha', 'Bhavana', 'dhatri', 'sreeya']
names.insert(3,'keerthy')
names
['Mahitha', 'Bhavana', 'dhatri', 'keerthy', 'sreeya']
names.extend(['asif', 'mehaboob', 'sameer'])
names
['Mahitha', 'Bhavana', 'dhatri', 'keerthy', 'sreeya', 'asif', 'mehaboob', 'sameer']
names.pop()
'sameer'
names.pop()
'mehaboob'
names.remove('asif')
names
['Mahitha', 'Bhavana', 'dhatri', 'keerthy', 'sreeya']
del names[4]
del
SyntaxError: invalid syntax
names
['Mahitha', 'Bhavana', 'dhatri', 'keerthy']
names.clear()
names
[]
names =['Mahitha', 'Bhavana', 'dhatri', 'keerthy']
names
['Mahitha', 'Bhavana', 'dhatri', 'keerthy']
names.index(1)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    names.index(1)
ValueError: 1 is not in list
names.index('mahitha')
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    names.index('mahitha')
ValueError: 'mahitha' is not in list
names.index('z')
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    names.index('z')
ValueError: 'z' is not in list
list = [1,2,1,1,1,2,3,6,6,6]
list.count(1)
4
list(2)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    list(2)
TypeError: 'list' object is not callable
list.sort(1)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    list.sort(1)
TypeError: sort() takes no positional arguments
list.sort()
list
[1, 1, 1, 1, 2, 2, 3, 6, 6, 6]
list.sorted()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    list.sorted()
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
list.sorted(1)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    list.sorted(1)
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
sorted(1)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    sorted(1)
TypeError: 'int' object is not iterable
sorted(list)
[1, 1, 1, 1, 2, 2, 3, 6, 6, 6]
list.sort(reverse = True)
list
[6, 6, 6, 3, 2, 2, 1, 1, 1, 1]
list.reverse()
list
[1, 1, 1, 1, 2, 2, 3, 6, 6, 6]
a = [1,2,3,4,5]
b = a
>>> b.append[10]
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    b.append[10]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> b.append(10)
>>> b
[1, 2, 3, 4, 5, 10]
>>> a
[1, 2, 3, 4, 5, 10]
>>> id(a)
4510762880
>>> id(b)
4510762880
>>> c = a.copy()
>>> id(a)
4510762880
>>> id(c)
4510776576
>>> sum(a)
25
>>> len(a)
6
>>> any([0,0.0,'',set(),{},(),[],False])
False
>>> any([1,0.0,'',set(),{},(),[],False])
True
>>> all([1,0.0,'',set(),{},(),[],False])
False
>>> all([1,2,3,5,True,9.5])
True
