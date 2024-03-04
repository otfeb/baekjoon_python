t = int(input())

for i in range(t):
    s = list(map(int, input().split()))
    a = s[0]
    b = s[1]%4
    if b == 0:
        b = 4
        
    if (a**b)%10 == 0:
        print(10)
    else:
        print((a ** b) % 10)