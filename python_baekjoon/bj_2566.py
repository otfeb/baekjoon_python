s = [[0 for col in range(9)] for row in range(9)]

for i in range(9):
    a = list(map(int, input().split()))
    for j in range(9):
        s[i][j] = a[j]

max = 0
x = 0
y = 0

for i in range(9):
    for j in range(9):
        if max < s[i][j]:
            max = s[i][j]
            x = i+1
            y = j+1

if max == 0:
    x = 1
    y = 1

print(max)
print(x,y)
