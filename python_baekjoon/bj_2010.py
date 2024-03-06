import sys

n = int(input())
plug = 1

for i in range(n):
    m = int(sys.stdin.readline())
    plug += m-1

print(plug)


