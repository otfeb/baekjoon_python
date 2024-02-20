# 몫이 1이 될때까지 계속 나누고 생겨난 나머지를 거꾸로 출력

s = ""
stack = []
n, b = map(int, input().split())

while n != 0:
    if n%b > 9:
        stack.append(chr(55+(n%b)))
        n = n//b
    else:
        stack.append(n%b)
        n = n//b

while len(stack) != 0:
    s += str(stack.pop())

print(s)

