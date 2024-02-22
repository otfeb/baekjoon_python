t = int(input())
cnt = 0
roomNum = 101
result = 0

for i in range(t):
    h, w, n = list(map(int, input().split()))   # height, width, num
    hotel = [[0 for j in range(w)] for k in range(h)]

    for a in range(w):
        if n == cnt:
            break

        for b in range(h-1, -1, -1):
            hotel[b][a] = roomNum
            cnt += 1

            if n == cnt:
               result = roomNum
               break

            roomNum += 100
            
        roomNum = (roomNum - 100 * h) + 1

    print(result)
    result = 0
    cnt = 0
    roomNum = 101