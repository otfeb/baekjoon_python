a = int(input())
b = int(input())
n = int(input())

num = a/b

if a%b != 0:
    num2 = round(num,n+1)
    result = list(str(num2))
    ans = result[len(result)-2]
    if ans == '.':
        print(0)
    else:
        print(ans)
else:
    print(0)

