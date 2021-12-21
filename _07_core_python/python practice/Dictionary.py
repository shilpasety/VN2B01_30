Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=5
y=x
x
5
y
5
x=10
x
10
y
5
id (x)
76162859536
id(y)
76162859376
type(x)
<class 'int'>
PI = 3.15
PI
3.15
type(PI)
<class 'float'>
x
10
y
5
z=y
z
5
id(z)
76162859376
id(5)
76162859376
id(10)
76162859536
di = {'Shilpa':'Java', 'Asha':'C','Pranaya':'Python'}
di
{'Shilpa': 'Java', 'Asha': 'C', 'Pranaya': 'Python'}
di['Shilpa']
'Java'
di['Shilpa']='Perl'
di
{'Shilpa': 'Perl', 'Asha': 'C', 'Pranaya': 'Python'}
di.copy()
{'Shilpa': 'Perl', 'Asha': 'C', 'Pranaya': 'Python'}
di.get('Asha')
'C'
di.keys('Shilpa', 'Pranaya')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    di.keys('Shilpa', 'Pranaya')
TypeError: dict.keys() takes no arguments (2 given)
di.keys()
dict_keys(['Shilpa', 'Asha', 'Pranaya'])
di.pop()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    di.pop()
TypeError: pop expected at least 1 argument, got 0
di.pop('Asha')
'C'
di
{'Shilpa': 'Perl', 'Pranaya': 'Python'}
di.popitem()
('Pranaya', 'Python')
di
{'Shilpa': 'Perl'}
di.update('Shilpa') = 'Ruby'
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
di.update()
di
{'Shilpa': 'Perl'}
di.update([1,2])
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    di.update([1,2])
TypeError: cannot convert dictionary update sequence element #0 to a sequence
di.update(['Asha':'C', 'Advaitha':'Python'])
SyntaxError: invalid syntax
di.values()
dict_values(['Perl'])
di = {'shilpa' : 'Java', 'Python': ['Pychram', 'Eclipse', 'VSC']}
di
{'shilpa': 'Java', 'Python': ['Pychram', 'Eclipse', 'VSC']}
di['python']
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    di['python']
KeyError: 'python'
di['Python']
['Pychram', 'Eclipse', 'VSC']
di['Python']['Eclipse'] =['spyder']
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    di['Python']['Eclipse'] =['spyder']
TypeError: list indices must be integers or slices, not str
di[0]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    di[0]
KeyError: 0
di.get()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    di.get()
TypeError: get expected at least 1 argument, got 0
di.get('shilpa')
'Java'
di.key('Python')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    di.key('Python')
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
di.keys()
dict_keys(['shilpa', 'Python'])
di.pop('shilpa')
'Java'
di
{'Python': ['Pychram', 'Eclipse', 'VSC']}
di.popitem()
('Python', ['Pychram', 'Eclipse', 'VSC'])
di
{}
