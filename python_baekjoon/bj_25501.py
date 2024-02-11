cnt = 1

def recursion(s, l, r):
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: cnt += 1  
    return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

# print('ABBA:', isPalindrome('ABBA'))
# print('ABC:', isPalindrome('ABC'))
t = int(input())

for i in range(t):
    s = input()
    print(isPalindrome(s)+" "+cnt)
    cnt = 1
