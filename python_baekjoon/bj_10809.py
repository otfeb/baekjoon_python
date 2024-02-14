c = 97
arr = [0] * 26
arr2 = [-1] * 26
s = list(input())

for i in range(len(arr)):
    arr[i] = chr(c)
    c += 1

for i in range(len(s)):
    for j in range(len(arr)):
        if s[i] == arr[j]:
            if arr2[j] == -1:
                arr2[j] = i
                break

for i in arr2:
    print(i, end=" ")