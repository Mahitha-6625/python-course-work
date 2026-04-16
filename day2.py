Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
length = 10
width = 5
area = length * width
if area > 30:
    print("Large area")
else:
    print("small area")

    
Large area
'''length - id
   =      - op
   width - id
   10 - li
   area - id
   * - op
   if - keyword
   30 - literal
   : - punctuator
   print() - identifier
   "large area" - li
   else - keyword
   "small area" - li
'''
'length - id\n   =      - op\n   width - id\n   10 - li\n   area - id\n   * - op\n   if - keyword\n   30 - literal\n   : - punctuator\n   print() - identifier\n   "large area" - li\n   else - keyword\n   "small area" - li\n'
x = 10
print(x)
10
age =25
# def greet():
age = 25
age
25
_name = "John"
_name
'John'
score1 = 88
score1
88
1age = 30
SyntaxError: invalid decimal literal
def = 5
SyntaxError: invalid syntax
# x = 10
''' This is a mutiline comment '''
' This is a mutiline comment '
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> print(len(keyword.kwlist))
35
>>> price = 45000
>>> product_name = "Laptop"
>>> in_stock = True
>>> print(product_name, price, in_stock)
Laptop 45000 True
>>> a, b, c = 10, 20, 30
>>> print(a,b,c)
10 20 30
>>> x = y = z
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    x = y = z
NameError: name 'z' is not defined
>>> x = y = z = 100
>>> print(x, y,z)
100 100 100
>>> x = 5
>>> x = 10
>>> print(x)
10
>>> a, b = 5, 10
>>> a, b = b, a
>>> print(a,b)
10 5
>>> x = 100
>>> del x
>>> print(x)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
