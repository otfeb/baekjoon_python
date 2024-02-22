t = int(input())
score = 0
sum = 0

for i in range(t):
    line = list(input())

    for j in range(len(line)):
        if line[j] == 'O':
            score += 1
            sum += score
        else:
            score = 0
            
    print(sum)
    sum = 0
    score = 0
        