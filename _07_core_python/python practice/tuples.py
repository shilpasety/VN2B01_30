Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t= 1,2,3
t
(1, 2, 3)
t= (23,45,'ASha')
t
(23, 45, 'ASha')
t[0]=45
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    t[0]=45
TypeError: 'tuple' object does not support item assignment
t=('Shilpa','Advaitha',45)
t
('Shilpa', 'Advaitha', 45)
t.count()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    t.count()
TypeError: tuple.count() takes exactly one argument (0 given)
t.count('shilpa')
0
t.count(45)
1
t.append(45)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    t.append(45)
AttributeError: 'tuple' object has no attribute 'append'
t + (45,45,45)
('Shilpa', 'Advaitha', 45, 45, 45, 45)
t.count(45)
1
t = (45,45,45)
t.count(45)
3
t= (20, 'shilpa', 20, 'Asha', 'Asha')
t.count('Asha')
2
t.count('shilpa')
1
t.index(20)
0
t.index('shilpa')
1
t.index('Asha')
3
