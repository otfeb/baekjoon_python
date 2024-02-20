arr = [[0 for i in range(100)] for j in range(100)]

n = int(input())
pLen = 10
area = 0

for i in range(n):
    s = list(map(int, input().split()))
    x = s[0]
    y = s[1]

    for i in range(x, x+pLen):
        for j in range(y, y+pLen):
            arr[i-1][j-1] = 1

for i in range(100):
    for j in range(100):
        if arr[i-1][j-1] == 1:
            area += 1

print(area)
    
