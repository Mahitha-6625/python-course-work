d = dict()
type(d)
<class 'dict'>
d = {'name': 'sreeya', 'batch':52, 'skills':['python','html','css']}
d
{'name': 'sreeya', 'batch': 52, 'skills': ['python', 'html', 'css']}
d['name'] = 'mahitha'
d
{'name': 'mahitha', 'batch': 52, 'skills': ['python', 'html', 'css']}
d['course'] = 'mahitha'
d
{'name': 'mahitha', 'batch': 52, 'skills': ['python', 'html', 'css'], 'course': 'mahitha'}
s = {}
type(s)
<class 'dict'>
s[1] = 'int'
s
{1: 'int'}
s[1.2] = 'float'
s
{1: 'int', 1.2: 'float'}
s['demo'] = 'string'
s
{1: 'int', 1.2: 'float', 'demo': 'string'}
s([1,2,3]) = 'float'
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
s[[1,2,3]] = 'list'
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s[[1,2,3]] = 'list'
TypeError: unhashable type: 'list'
s[(1,2,3)] = 'tuple'
s
{1: 'int', 1.2: 'float', 'demo': 'string', (1, 2, 3): 'tuple'}
s[False] = 1
s
{1: 'int', 1.2: 'float', 'demo': 'string', (1, 2, 3): 'tuple', False: 1}
# keys in the dictionary can be immutable datatypes i.e int,float,complex,tuple,boolean
#membership
'name' in d
True
'mahitha' in d
False
d
{'name': 'mahitha', 'batch': 52, 'skills': ['python', 'html', 'css'], 'course': 'mahitha'}
d['name']
'mahitha'
d['course']
'mahitha'
d.get('age')
d.get('course')
'mahitha'
d.get('name','name is not present')
'mahitha'
d.get('age','age is not present')
'age is not present'
d['course'] = PFS
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    d['course'] = PFS
NameError: name 'PFS' is not defined
>>> d['course'] = 'PFS'
>>> d
{'name': 'mahitha', 'batch': 52, 'skills': ['python', 'html', 'css'], 'course': 'PFS'}
>>> d['age'] = 23
>>> d
{'name': 'mahitha', 'batch': 52, 'skills': ['python', 'html', 'css'], 'course': 'PFS', 'age': 23}
>>> #to add multiple key-value
>>> d.update({'k1':'v1','k2':'v2', 'k3':'v3'})
>>> d
{'name': 'mahitha', 'batch': 52, 'skills': ['python', 'html', 'css'], 'course': 'PFS', 'age': 23, 'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
>>> d.popitem()
('k3', 'v3')
>>> d
{'name': 'mahitha', 'batch': 52, 'skills': ['python', 'html', 'css'], 'course': 'PFS', 'age': 23, 'k1': 'v1', 'k2': 'v2'}
>>> d.popitem()
('k2', 'v2')
>>> d.popitem()
('k1', 'v1')
>>> d
{'name': 'mahitha', 'batch': 52, 'skills': ['python', 'html', 'css'], 'course': 'PFS', 'age': 23}
>>> d.pop('name')
'mahitha'
>>> d
{'batch': 52, 'skills': ['python', 'html', 'css'], 'course': 'PFS', 'age': 23}
>>> del d['batch']
d
{'skills': ['python', 'html', 'css'], 'course': 'PFS', 'age': 23}

d.clear()
d.keys()
d.values()
d.items()
sorted(d)
len(d)
max(d)
min(d)
d.get('name')
d.setdefault('name',' ')
d.setdefault('name',' ')

