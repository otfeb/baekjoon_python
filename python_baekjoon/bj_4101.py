while True:
    s = input()
    if s == '0 0':
        break

    a, b = map(int, s.split())

    if a > b:
        print('Yes')
    else:
        print('No')