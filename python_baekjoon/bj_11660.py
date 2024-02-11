nm = input().split()
n = int(nm[0])
m = int(nm[1])
sum = 0

arr = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    numbers = input().split()
    for j in range(n):
        arr[i][j] = int(numbers[j])

print(arr)


    
