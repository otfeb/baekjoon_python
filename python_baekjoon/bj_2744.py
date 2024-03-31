s = list(input())

for i in s:
    if i.isupper():
        print(i.lower(), end='')
    else:
        i.upper()
        print(i.upper(), end='')

