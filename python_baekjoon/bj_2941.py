c_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
s = input()
cnt = 0

for i in range(len(c_alphabet)):
    while s.find(c_alphabet[i]) != -1:     # 인덱스 i번째 크로아티아 알파벳이 문자열에 존재할 경우
        s = s.replace(c_alphabet[i], ' ', 1)
        cnt += 1

s = s.replace(' ','')       # 공백 제거
print(len(s) + cnt)
    




