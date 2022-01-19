'''Write a Python program to convert month name to a number of days. Go to the editor
Expected Output:

List of months: January, February, March, April, May, June, July, August
, September, October, November, December
Input the name of Month: February
No. of days: 28/29 days '''
while True:
    m = input("Enter month name:")
    if m.lower()=='january':
        print('31 days')
        break
    elif m.lower()=='february':
        print('28/29 days')
        break
    elif m.lower()=='march':
        print('31 days')
        break
    elif m.lower()=='april':
        print('30 days')
        break
    elif m.lower()=='may':
        print('31 days')
        break
    elif m.lower()=='june':
        print('30 days')
        break
    elif m.lower()=='july':
        print('31 days')
        break
    elif m.lower()=='august':
        print('31 days')
        break
    elif m.lower()=='september':
        print('30 days')
        break
    elif m.lower()=='october':
        print('31 days')
        break
    elif m.lower()=='november':
        print('30 days')
        break
    elif m.lower()=='december':
        print('31 days')
        break
    else:
        print('Sorry! It\'s not a month name')
        print("Try again")
