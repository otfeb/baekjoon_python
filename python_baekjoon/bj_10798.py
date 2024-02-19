result = ""
cnt = 0         # 새로 한줄이 전부 -1일 경우를 찾기 위해

tdlist = [[-1 for i in range(15)] for j in range(5)]

for i in range(5):
    s = list(input())
    for j in range(len(s)):
        tdlist[i][j] = s[j]

for i in range(15):
    for j in range(5):
        if tdlist[j][i] == -1:
            cnt += 1
            continue
        result += tdlist[j][i]
    if cnt == 5:
        break
    cnt = 0

print(result)