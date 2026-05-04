Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
name = input()
mahitha
name
'mahitha'
type(name)
<class 'str'>
name = input("Enter the name:")
Enter the name:mahitha
name
'mahitha'
age = input()
10
age
'10'
age = int(input("Enter the integer:"))
Enter the integer:12
age
12
price = float(input("Enter the float:"))
Enter the float:12.3
price
12.3
'dsfg sfdgh fdghjuk dfgh'.split(' ')
['dsfg', 'sfdgh', 'fdghjuk', 'dfgh']
'1 2 3 4 5 6'.split()
['1', '2', '3', '4', '5', '6']
'java,python,html,css,javascript'.split(',java python css c++ html)
                                        
SyntaxError: unterminated string literal (detected at line 1)
'java,python,html,css,javascript'.split(',java python css c++ html')
                                        
['java,python,html,css,javascript']
'java,python,html,css,javascript'.split(',')
                                        
['java', 'python', 'html', 'css', 'javascript']
lang = input("Enter the lang:").split()
                                        
Enter the lang:java html css python
lang
                                        
['java', 'html', 'css', 'python']
name = input("Enter the name:").split(',')
                                        
Enter the name:mahitha priya bhavana
name
                                        
['mahitha priya bhavana']
name = input("Enter the name:").split(',')
                                        
Enter the name:mahitha,priya,bhavana
name
                                        
['mahitha', 'priya', 'bhavana']
numbers = input("Enter the numbers:").split()
                                        
Enter the numbers:1 2 3 3
numbers
                                        
['1', '2', '3', '3']
map(int,['1','2','3','4']))
SyntaxError: unmatched ')'
map(int,['1','2','3','4'])
<map object at 0x10ca5ed10>
list(map(int,['1','2','3','4']))
[1, 2, 3, 4]
numbers = list(map(int,input("Enter the nums:").split()))
Enter the nums:4 6 8 9 966 9565423 23456 678
numbers
[4, 6, 8, 9, 966, 9565423, 23456, 678]
numbers = list(map(float,input("Enter the nums").split()))
Enter the nums546 78.3 13.2 4 5 1 3 7.8
numbers
[546.0, 78.3, 13.2, 4.0, 5.0, 1.0, 3.0, 7.8]
numbers = tuple(map(int,input("Enter the nums:").split()))
Enter the nums:1 2
numbers
(1, 2)
numbers = tuple(map(float,input("Enter the nums:").split()))
Enter the nums:12.3 46.5
numbers
(12.3, 46.5)
numbers = tuple(input().split())
dfghj gyuhj bnm
names
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    names
NameError: name 'names' is not defined. Did you mean: 'name'?
numbers
('dfghj', 'gyuhj', 'bnm')
numbers = set(map(float,input("Enter the nums:").split()))
Enter the nums:5467 6789
numbers
{5467.0, 6789.0}
numbers = set(map(int,input("Enter the nums:")).split()))
SyntaxError: unmatched ')'
numbers = set(map(int,input("Enter the nums:")).split())
Enter the nums:1 2 3 4 5
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    numbers = set(map(int,input("Enter the nums:")).split())
AttributeError: 'map' object has no attribute 'split'
numbers = set(map(int,input("Enter the nums:").split()))
Enter the nums:1 2 3 4 5
numbers
{1, 2, 3, 4, 5}
a,b,c
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a,b,c
NameError: name 'a' is not defined
a,b,c = {1,2,3}
a
1
1
1
b
2
c
3
a,b,c = list(map(int,input().split()))
1 2 3
a
1
b
2
c
3
email,password = ['@gmail.com','pass@123']
email,password = input().split()
mahithadondeti@gmail.com @123
email
'mahithadondeti@gmail.com'
password
'@123'
a = eval
a = eval(input())
12
a
12
a = eval(input())
34567.5678
a
34567.5678
a=eval(input())
srtyuvgjhbknlbk
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a=eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'srtyuvgjhbknlbk' is not defined
a = eval(input("Enter the input:"))
Enter the input:'sfdghjk'
a
'sfdghjk'
a = eval(input("Enter the input: "))
Enter the input: [1,1,1,2,3]
q
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    q
NameError: name 'q' is not defined
a
[1, 1, 1, 2, 3]
a = eval(input("Enter the input: "))
Enter the input: (1,2,30
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a = eval(input("Enter the input: "))
  File "<string>", line 1
    (1,2,30
    ^
SyntaxError: '(' was never closed
a = eval(input("Enter the input: "))
     
Enter the input: (1,2,3)
a
     
(1, 2, 3)
a = eval(input("Enter the input: "))
     
Enter the input: {1,2,3,4}
a
     
{1, 2, 3, 4}
a = eval(input("Enter the input: "))
     
Enter the input: {1:1,2:3,4:5,6:7}
a
     
{1: 1, 2: 3, 4: 5, 6: 7}
a = eval(input("Enter the input: "))
     
Enter the input: True
a
     
True
a,b,c = 10,10.3,'python'
     
a
     
10
b
     
10.3
c
     
'python'
print(a,b,c)
     
10 10.3 python
print('a=',a,'b=',b,'c=',c)
     
a= 10 b= 10.3 c= python
print('a=',a,'b=',b,'c=',c,sep='')
     
a=10b=10.3c=python
>>> print('a=',a,'b=',b,'c=',c,sep='\n')
...      
a=
10
b=
10.3
c=
python
>>> print('a=',a,'b=',b,'c=',c,sep='@@@')
...      
a=@@@10@@@b=@@@10.3@@@c=@@@python
>>> print('a=',a,'b=',b,'c=',c,sep='@@@',end='\n\n')
...      
a=@@@10@@@b=@@@10.3@@@c=@@@python

>>> print('a=',a,'b=',b,'c=',c,sep='@@@',end='..................')
...      
a=@@@10@@@b=@@@10.3@@@c=@@@python..................
>>> print(f'{a} b={b} c={c}')
...      
10 b=10.3 c=python
>>> print('a=%d b=%f c =%s'%(a,b,c))
...      
a=10 b=10.300000 c =python
>>> print('a=%d b=%.2f c=%s'(a,b,c))
...      
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    print('a=%d b=%.2f c=%s'(a,b,c))
TypeError: 'str' object is not callable
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
...      
a=10 b=10.30 c=python
>>> print('a={} b={} c={}'.format(a,b,c))
...      
a=10 b=10.3 c=python
>>> print('a={} b={} c={}'.format(b,c,a))
...      
a=10.3 b=python c=10
>>> print('a={2} b={0} c={1}'.format(a,b,c))
...      
a=python b=10 c=10.3
