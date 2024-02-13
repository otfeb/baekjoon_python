s = input()
x = s.split()
n = int(x[0])
m = int(x[1])

cnt = 0

a = input()
# 기본 배열
arr = list(map(int,a.split()))

# 누적합 배열
accArr = []
for i in range(n):
    if i == 0:
        accArr.append(arr[i])
    else:
        accArr.append(accArr[i-1]+arr[i])

for i in range(n):
    for j in range(i, n):
        if i == j:
            if arr[i] % m == 0:
                cnt += 1
        else:
            if (accArr[j] - accArr[i-1]) % m == 0:
                cnt += 1
        

print(cnt)




            
