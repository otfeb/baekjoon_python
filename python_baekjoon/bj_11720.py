n = int(input())
numbers = input()
numList = list(numbers)

sum = 0

for i in range(n):
    sum += int(numList[i])
print(sum)