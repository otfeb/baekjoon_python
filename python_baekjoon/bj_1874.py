n = int(input())
stack = [1]
idx = 0
level = 2
num = 1
arr = [0] * n
result = '+'

for i in range(n):
    arr[i] = int(input())

while len(arr) != 0:
    if level > n+1:
        print('No')
        break
    elif len(stack) == 0:
        stack.append(level)
        result += '+'
        num += 1
        level += 1
        continue
    elif arr[idx] == stack[num-1]:
        rm = stack.pop()
        result += '-'
        arr.remove(rm)
        num -= 1
    else:
        stack.append(level)
        result += '+'
        num += 1
        level += 1

if level == n+1:
    for r in range(len(result)):
        print(result[r])