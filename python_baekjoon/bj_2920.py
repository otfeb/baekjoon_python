s = list(map(int, input().split()))
asc = 1
des = 1

for i in range(1, len(s)):
    if s[0] == 1 and s[i] == s[i-1] + 1:
        asc += 1
    elif s[0] == 8 and s[i] == s[i-1] - 1:
        des += 1

if asc == len(s):
    print("ascending")
elif des == len(s):
    print("descending")
else:
    print("mixed")


