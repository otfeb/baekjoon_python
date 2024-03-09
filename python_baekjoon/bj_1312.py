a,b,n = map(int, input().split())

# 25 % 7 = 4
# 4 * 10 = 40
# 40 // 7 = 5 -> 소수점 첫째 자리
# 이런식으로 원하는 소수점 자리까지 반복

for i in range(n):
    a = (a%b) * 10
    result = a//b

print(result)

