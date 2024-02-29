# 문자열 입력
# 명령어 개수 입력
# 초기 커서(idx) : 문자열 길이 - 1
# 명령어 개수 만큼 명령 반복
# if 명령어 == 'L' : idx - 1 (idx == 0 이면 무시)
# if 명령어 == 'R' : idx + 1 (idx == 맨끝 이면 무시)
# if 명령어 == 'B' : del 배열[idx] (idx == 0 이면 무시)
# if 명령어 == 'P $' : 배열.insert(idx, '$')

arr = list(input())
n = int(input())
cursor = len(arr)

for i in range(n):
    command = input()
    if command == 'L':
        if cursor > 0:
            cursor -= 1   
    elif command == 'D':
        if cursor < len(arr):
            cursor += 1
    elif command == 'B':
        if cursor > 0:
            del arr[cursor-1]
            cursor -= 1
    else:
        put = command.split()
        if cursor == 0:
            arr.insert(0, put[1])
        else:
            arr.insert(cursor+1, put[1])
        cursor += 1

for i in arr:
    print(i, end='')
