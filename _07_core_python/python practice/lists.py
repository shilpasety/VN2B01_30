Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
squares = [1,4,9,16,25]
sqares
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    sqares
NameError: name 'sqares' is not defined. Did you mean: 'squares'?
squares
[1, 4, 9, 16, 25]
print(squares)
[1, 4, 9, 16, 25]
squares[0]
1
sqares[-1]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    sqares[-1]
NameError: name 'sqares' is not defined. Did you mean: 'squares'?
squares[-1]
25
squares[2:]
[9, 16, 25]
squares[:-3]
[1, 4]
squares[-3:]
[9, 16, 25]
squares + [36,49,64,91,100]
[1, 4, 9, 16, 25, 36, 49, 64, 91, 100]
string = 'shilpa
SyntaxError: unterminated string literal (detected at line 1)
string ='shilpa'
string[0]
's'
string[0]='a'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    string[0]='a'
TypeError: 'str' object does not support item assignment
cubes = [1,8,27,65,125]
4 ** 3
64
cubes [3] = 64
cubes
[1, 8, 27, 64, 125]
cubes.append(216)
cubes.append ( 7 **3 )
cube
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    cube
NameError: name 'cube' is not defined. Did you mean: 'cubes'?
cubes
[1, 8, 27, 64, 125, 216, 343]
letters = ['a', 'b', 'c', 'd','e','f']
letters
['a', 'b', 'c', 'd', 'e', 'f']
letters [2:4]
['c', 'd']
letters [2:4] =['C','D']
letters
['a', 'b', 'C', 'D', 'e', 'f']
letters [2:4] =[ ]
letters
['a', 'b', 'e', 'f']
letters.clear()
letters
[]
numbers = [2,4,6,8,10]
numbers
[2, 4, 6, 8, 10]
numbers[ : ]
[2, 4, 6, 8, 10]
numbers [ : ] = [ ]
numbers
[]
print (numbers)
[]
len (numbers)
0
letters = ['a','b','c','d']
len(letters)
4
x= [1,2,3]
y= ['a', 'b', 'c', 'd']
nest = [x,y]
nest
[[1, 2, 3], ['a', 'b', 'c', 'd']]
nest[0]
[1, 2, 3]
nest[1]
['a', 'b', 'c', 'd']
nest[0][3]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    nest[0][3]
IndexError: list index out of range
nest[1][3]
'd'
print(x,y)
[1, 2, 3] ['a', 'b', 'c', 'd']
print(x+y)
[1, 2, 3, 'a', 'b', 'c', 'd']
x
[1, 2, 3]
nest = [x+y]
nest
[[1, 2, 3, 'a', 'b', 'c', 'd']]
nest [5]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    nest [5]
IndexError: list index out of range
len(nest)
1
nest[0]
[1, 2, 3, 'a', 'b', 'c', 'd']
nest[1]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    nest[1]
IndexError: list index out of range
x,y = 0,1
x+y
1
x*y
0
x-y
-1
