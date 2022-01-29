st = input('Enter string:')
def pal(st):
    rev = st[::-1]
    if st==rev:
        return 'palindrome'
    else:
        return 'Not a palindrome'

print(pal(st))


