import sys

s1 = []     # stack 1
s2 = []     # stack 2

s = input()
m = int(input())

for i in s:
    s1.append(i)

for i in range(m):
    command = list(sys.stdin.readline().split())
    c1 = command[0]

    if c1 == 'L':
        if len(s1) != 0:
            pop = s1.pop()
            s2.append(pop)
    elif c1 == 'D':
        if len(s2) != 0:
            pop = s2.pop()
            s1.append(pop)
    elif c1 == 'B':
        if len(s1) != 0:
            s1.pop()
    else:
        s1.append(command[1])

s2.reverse()
s3 = s1 + s2

for i in s3:
    print(i, end='')