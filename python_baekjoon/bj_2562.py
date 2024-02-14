num = [0] * 9
max = 0
cnt = 0

for i in range(9):
    num[i] = int(input())
    if max < num[i]:
        max = num[i]
        cnt = i + 1

print(max)
print(cnt)