import sys
for _ in range(3):
    tot = sum(list(map(int, sys.stdin.readline().split())))
    if tot == 0:
        print("D")
    elif tot == 1:
        print("C")
    elif tot == 2:
        print("B")
    elif tot == 3:
        print("A")
    elif tot == 4:
        print("E")