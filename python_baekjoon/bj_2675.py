t = int(input())

for i in range(t):
    a = ""

    line = list(input().split())
    r = int(line[0])
    s = line[1]

    for j in range(len(s)):
        a += s[j]*r

    print(a)




