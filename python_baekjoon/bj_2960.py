n, k = map(int, input().split())
cnt = 0
arr = []

for i in range(n):
    if i == 0:
        continue
    arr.append(i+1)

for i in range(len(arr)):
    if cnt == k:
        break
    x = arr[i]
    if x == 0:
        continue
    for j in range(len(arr)):
        if arr[j] == 0:
            continue
        elif arr[j] % x == 0:
            cnt += 1
            if cnt == k:
                print(arr[j])
                break
            arr[j] = 0
            