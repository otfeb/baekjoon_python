# t 입력
# t번 문자열 입력
# 문자열 리스트에 담고
# (개수, )개수 비교해서 같으면 YES 다르면 NO 출력

t = int(input())
l = 0
r = 0
v = 0

for i in range(t):
    l = 0
    r = 0
    v = 0
    vps = list(input())
    for j in range(len(vps)):
        if vps[j] == '(':
            l += 1
            v += 1
        else:
            r += 1
            v -= 1
        if v < 0:
            print('NO')
            break
    if v < 0:
        continue
    elif l == r:
        print('YES')
    else:
        print('NO')
