Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x,y,z=10
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    x,y,z=10
TypeError: cannot unpack non-iterable int object
x,y,z=t
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x,y,z=t
NameError: name 't' is not defined
s ={1,1,2,3,2}
s
{1, 2, 3}
s={23,45,23,34,12}
w
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    w
NameError: name 'w' is not defined
s
{34, 12, 45, 23}
s.update(s)
s
{34, 12, 45, 23}
set()
set()
set()= { }
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
set() == { }
False
s = { }
s
{}
unorder = {2,3,1,2,4,5,1}
unorder
{1, 2, 3, 4, 5}
1 in unorder
True
6 in unorder
False
a= set('abracadabra')
b= set('alacazam')
print (a)
{'r', 'd', 'c', 'b', 'a'}
a
{'r', 'd', 'c', 'b', 'a'}
b
{'c', 'm', 'l', 'z', 'a'}
a-b
{'d', 'b', 'r'}
b-a
{'l', 'z', 'm'}
a | b
{'r', 'd', 'c', 'b', 'm', 'l', 'z', 'a'}
a&b
{'c', 'a'}
a ^ b
{'b', 'r', 'm', 'z', 'l', 'd'}
z in b
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    z in b
NameError: name 'z' is not defined
'z' in b
True
