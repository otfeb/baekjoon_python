a = int(input())
b = int(input())
c = int(input())

list1 = ['0','1','2','3','4','5','6','7','8','9']
list2 = [0,0,0,0,0,0,0,0,0,0]

abcInt = a * b * c
abc = list(str(abcInt))

for i in range(len(abc)):
    for j in range(10):
        if abc[i] == list1[j]:
            list2[j] += 1
            break

for i in list2:
    print(i)
