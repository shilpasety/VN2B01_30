m ='''I am just trying how the multiline works in String.
We need to use double or single quotes three times 
for the multiline string to get printed.'''

print(m)

# Accessing the elements of string

s = 'Work Hard'
for i in s:   # looping through string
    print(i,end=' ')
print()

print(s[8])  # Access the particular character using index value

print(len(s))  #Print the length

print( 'w' in s) # Membership operator
print( 'g' not in s)