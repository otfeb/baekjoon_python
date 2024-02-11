total = int(input())
cnt = int(input())
sum = 0

for i in range(cnt):
    s = input()
    a = s.split()
    pay = int(a[0])
    num = int(a[1])
    sum += pay * num

if total == sum:
    print('Yes')
else:
    print('No')
