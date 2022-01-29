'''Write a Python program to get next day of a given date. Go to the editor
Expected Output:

Input a year: 2016
Input a month [1-12]: 08
Input a day [1-31]: 23
The next date is [yyyy-mm-dd] 2016-8-24 '''

y = int(input('input a year:'))
m = int(input('input a month[1-12]:'))
d = int(input('input a date[1-31]:'))

print('The next date is [yyyy-mm-dd]:',y,'-',m,'-',d+1)