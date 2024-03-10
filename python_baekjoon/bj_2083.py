while True:
    s = input()

    if s == "# 0 0":
        break

    s = list(s.split())

    name = s[0]
    age = int(s[1])
    kg = int(s[2])

    if age > 17 or kg >= 80:
        print(name, "Senior")
    else:
        print(name, "Junior")