n, m = list(map(int,input().split()))
arr = [0] * n

for i in range(n):
    arr[i] = i+1

for i in range(m):
    a, b = list(map(int,input().split()))
    temp = arr[a-1]
    arr[a-1] = arr[b-1]
    arr[b-1] = temp

for i in arr:
    print(i, end=" ")
