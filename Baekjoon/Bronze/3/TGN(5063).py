import sys
for i in range(int(sys.stdin.readline().rstrip())):
    r, e, c = map(int, sys.stdin.readline().split())
    if r + c < e:
        print("advertise")
    elif r + c == e:
        print("does not matter")
    else:
        print("do not advertise")