import sys
for _ in range(int(sys.stdin.readline().rstrip())):
    lst = [False] * 101
    t = int(sys.stdin.readline().rstrip())
    for i in range(1, t + 1):
        for j in range(i, t + 1, i):
            if not lst[j]:
                lst[j] = True
            else:
                lst[j] = False
    print(lst.count(True))