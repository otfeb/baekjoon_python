# n 입력
# n개의 자연수 입력 -> 리스트에 넣기
# m 입력
# m개의 자연수 입력하면서 리스트에 존재하는지 확인
# 2중 for문 불가 / if ~ in 역시 O(n) 이므로 반복문과 함께 사용 불가
# 2진탐색(O(logn)) 이므로 O(Nlogn) 으로 풀어야함

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
compare = list(map(int, input().split()))

start = 0
end = n-1

for i in range(m):
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == compare[i]:
            print(1)
            break
        elif arr[mid] > compare[i]:
            end = mid - 1
        else:
            start = mid + 1
    if arr[mid] == compare[i]:
        continue

    print(0)

