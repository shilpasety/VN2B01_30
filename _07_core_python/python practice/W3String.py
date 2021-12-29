# multiline string can be assigned using 3 single quotes or 3 double quotes.

st="""This is my time to work hard.
I can work happily. Of late I feel programming is fun    
At my office many multitalented are there                 
"""
print(st)

print('---------------')

print("Indexing and slicing")
a = "Hello, world!"
print(a[1])
print(len(a))
print(a[0:13])
print(a[-5:-1])

print('---------------')

if 'work' in st:
    print("Yes, work is in string")

print('---------------')

print("  Modifying the string  ")
b= "  Hello! World! Sai!  "
print(b.upper())
print(b.lower())
print(b.strip())
print(b.replace('l','s'))
print(b.split("!"))

print('---------------')

print("Escape character ")

txt = "We are the so called \"Vikings\" from the North"
print(txt)
si = 'it\'s alright'
print(si)
bs = "This will insert one \\ (backslash)"
print(bs)
hw = 'Hello\nworld!'
print(hw)
tb = "Hello\tworld!"
print(tb)

