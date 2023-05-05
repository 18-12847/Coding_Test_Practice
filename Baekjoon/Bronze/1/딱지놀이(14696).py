import sys
for i in range(int(sys.stdin.readline().rstrip())):
    a = list(map(int, sys.stdin.readline().split()))[1:]
    b = list(map(int, sys.stdin.readline().split()))[1:]
    if a.count(4) > b.count(4):
        print("A")
    elif a.count(4) == b.count(4) and a.count(3) > b.count(3):
        print("A")
    elif a.count(4) == b.count(4) and a.count(3) == b.count(3) and a.count(2) > b.count(2):
        print("A")
    elif a.count(4) == b.count(4) and a.count(3) == b.count(3) and a.count(2) == b.count(2) and a.count(1) > b.count(1):
        print("A")
    elif a.count(4) == b.count(4) and a.count(3) == b.count(3) and a.count(2) == b.count(2) and a.count(1) == b.count(1):
        print("D")
    else:
        print("B")