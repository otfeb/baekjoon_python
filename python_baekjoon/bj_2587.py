avg = 0
mid = 0
arr = []

for i in range(5):
    arr.append(int(input()))

arr.sort()

for i in arr:
    avg += i

avg = avg // 5
mid = arr[2]

print(avg)
print(mid)