alpha = [0] * 26
c = 97
cnt = 0

for i in range(26):                     # 소문자 알파벳 배열
    alpha[i] = chr(c)
    c += 1

n = int(input())

for i in range(n):
    s = list(input())

    complete = 1
    boolArr = [False] * 26              # 불리언 배열

    for j in range(len(s)):
        if j == 0:
            temp = s[j]
            continue
        else:
            idx = alpha.index(s[j])
            if boolArr[idx] == True:
                complete = 0
                break
            else:
                if temp == s[j]:
                    continue
                else:
                    preidx = alpha.index(temp)
                    if boolArr[preidx] == False:
                        boolArr[preidx] = True
                        temp = s[j]

    if complete == 1:
        cnt += 1

print(cnt)