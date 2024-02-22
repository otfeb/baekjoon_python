n = int(input())
p = list(map(int, input().split()))
# 선택정렬
for i in range(1, n):
    insert = i
    value = p[i]
    for j in range(i-1, -1, -1):
        if p[i] >= p[j]:
            insert = j + 1
            break
        if j == 0:
            insert = 0
    for k in range(i, insert, -1):
        p[k] = p[k-1]
    p[insert] = value

# 합 배열
s = [0] * n
s[0] = p[0]
for i in range(1,n):
    s[i] = s[i-1] + p[i]

sum = 0
for j in s:
    sum += j

print(sum)
