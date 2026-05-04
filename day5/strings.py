Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#string
s = 'afd'
s
'afd'
type*s)
SyntaxError: unmatched ')'
type(s)
<class 'str'>
s="fghjkl"
s='''gfhjkl;'''
s=''
#string operations
#concat
fname = 'abc'
lname = 'xyz'
fname + lname
'abcxyz'
#repetition
fname * 7
'abcabcabcabcabcabcabc'
fname*20
'abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc'
s = 'python'
s[4]
'o'
s[5]
'n'
s[0]
'p'
s[2]
't'
s[3]
'h'
s[-1]
'n'
s[-2]
'o'
s[-3]
'h'
s[-4]
't'
names='bhavanna mahitha priya'
names[0]
'b'
names[-2]
'y'
names[-16]
'n'
names[-1]
'a'
#slicing
names[0:8]
'bhavanna'

================================ RESTART: Shell ================================
names = "bhavana mahitha priya'
SyntaxError: unterminated string literal (detected at line 1)
names = 'bhavana mahitha priya mehaboob asif'
names[0:7]
'bhavana'
names[8:15]
'mahitha'
names[16;21]
SyntaxError: invalid syntax
names[16:21]
'priya'
names[::-14]
'faa'
names[-15:-20]
''
names[-15:-20]
''
names[-2:-7]
''
names[-2::-7]
'ibytn'
names[-15:-20:-1]
'ayirp'
names[-21:-28:-1]
'ahtiham'
#membership
'mahitha' in names
True
'sreeya' in names
False
'mahitha' not in names
False
#methods
len(names)
35
sorted(names)
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'e', 'f', 'h', 'h', 'h', 'h', 'i', 'i', 'i', 'm', 'm', 'n', 'o', 'o', 'p', 'r', 's', 't', 'v', 'y']
max(names)
'y'
min(names)
' '
ord(a)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    ord(a)
NameError: name 'a' is not defined
ord('a')
97
ord('A')
65
ord(' ')
32
chr(97)
'a'
chr(112)
'p'
chr(105)
'i'
chr(20)
'\x14'
chr(78)
'N'
chr(64)
'@'
chr(48)
'0'
names.uppercase()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    names.uppercase()
AttributeError: 'str' object has no attribute 'uppercase'
names.upper()
'BHAVANA MAHITHA PRIYA MEHABOOB ASIF'
names.lower()
'bhavana mahitha priya mehaboob asif'
names.capitalize()
'Bhavana mahitha priya mehaboob asif'
names.title()
'Bhavana Mahitha Priya Mehaboob Asif'
names.swapcase()
'BHAVANA MAHITHA PRIYA MEHABOOB ASIF'
'Chez Chérie Café'.casefold()
'chez chérie café'
#alignment and formatting methods
names.center(50,'*')
'*******bhavana mahitha priya mehaboob asif********'
names.center(70,'-')
'-----------------bhavana mahitha priya mehaboob asif------------------'
names.ljust(70,'-')
'bhavana mahitha priya mehaboob asif-----------------------------------'
names.rjust(70,'-')
'-----------------------------------bhavana mahitha priya mehaboob asif'
num='65789'
num.zfill(7)
'0065789'
num.zfill(10)
'0000065789'
num.zfill(5)
'65789'
num.zfill(15)
'000000000065789'
names.find('Priya')
-1
names.find('mahitha')
8
names.find('b')
0
names.find('a')
2
names.find('a')
2
names.rfind('m')
22
names.rfind('a')
31
names.index('a')
2
names.rindex('a')
31
names.count('a')
8
names.count('h')
4
names.replace('a','*')
'bh*v*n* m*hith* priy* meh*boob *sif'
names.replace('i','0')
'bhavana mah0tha pr0ya mehaboob as0f'
names.replace('i','0')
'bhavana mah0tha pr0ya mehaboob as0f'
names.replace('mehaboob','sreeya')
'bhavana mahitha priya sreeya asif'
names.replace('aeiou','*')
'bhavana mahitha priya mehaboob asif'
names.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
names.translate(names.maketrans('aeiou','12345'))
'bh1v1n1 m1h3th1 pr3y1 m2h1b44b 1s3f'
names.split()
['bhavana', 'mahitha', 'priya', 'mehaboob', 'asif']
names.split(' ',2)
['bhavana', 'mahitha', 'priya mehaboob asif']
names.rsplit(' ',2)
['bhavana mahitha priya', 'mehaboob', 'asif']
s='python\nprogramming\nlang'
s
'python\nprogramming\nlang'
s.splitlines()
['python', 'programming', 'lang']
l =['python', 'programming', 'lang']
','.join(l)
'python,programming,lang'
n = ['Mahitha', 'Bhavana', 'Priya']
>>> '@'.join(n)
'Mahitha@Bhavana@Priya'
>>> names.partition(' ')
('bhavana', ' ', 'mahitha priya mehaboob asif')
>>> names.partition('P')
('bhavana mahitha priya mehaboob asif', '', '')
>>> names.partition('a')
('bh', 'a', 'vana mahitha priya mehaboob asif')
>>> n.rpartition('a')
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    n.rpartition('a')
AttributeError: 'list' object has no attribute 'rpartition'
>>> names.rpartition('a')
('bhavana mahitha priya mehaboob ', 'a', 'sif')
>>> s ='      hello        world    '
>>> s.strip()
'hello        world'
>>> s.lstrip()
'hello        world    '
>>> s.rstrip()
'      hello        world'
>>> text = '₊✩‧₊˚౨ৎ˚₊✩‧₊'
>>> text.encode()
b'\xe2\x82\x8a\xe2\x9c\xa9\xe2\x80\xa7\xe2\x82\x8a\xcb\x9a\xe0\xb1\xa8\xe0\xa7\x8e\xcb\x9a\xe2\x82\x8a\xe2\x9c\xa9\xe2\x80\xa7\xe2\x82\x8a'
>>> text.decode()
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    text.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
>>> 'b'\xe2\x82\x8a\xe2\x9c\xa9\xe2\x80\xa7\xe2\x82\x8a\xcb\x9a\xe0\xb1\xa8\xe0\xa7\x8e\xcb\x9a\xe2\x82\x8a\xe2\x9c\xa9\xe2\x80\xa7\xe2\x82\x8a'.decode()
SyntaxError: unexpected character after line continuation character
b'\xe2\x82\x8a\xe2\x9c\xa9\xe2\x80\xa7\xe2\x82\x8a\xcb\x9a\xe0\xb1\xa8\xe0\xa7\x8e\xcb\x9a\xe2\x82\x8a\xe2\x9c\xa9\xe2\x80\xa7\xe2\x82\x8a'.decode()
'₊✩‧₊˚౨ৎ˚₊✩‧₊'
