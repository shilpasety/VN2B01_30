lines = []
print("Enter the data in a few lines::")
while True:
    l = input()
    if l:
        lines.append(l.lower())
    else:
        break

for l in lines:
    print(l)
