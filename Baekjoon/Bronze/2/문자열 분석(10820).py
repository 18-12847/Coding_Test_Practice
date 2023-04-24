import sys
for i in sys.stdin.readlines():
    a, b, c, d = 0, 0, 0, 0
    for j in i.rstrip("\n"):
        if j.islower():
            a += 1
        elif j.isupper():
            b += 1
        elif j.isdigit():
            c += 1
        else:
            d += 1
    print(a, b, c, d)