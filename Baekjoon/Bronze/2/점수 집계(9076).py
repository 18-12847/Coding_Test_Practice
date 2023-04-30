import sys
for i in range(int(sys.stdin.readline().rstrip())):
    lst = sorted(list(map(int, sys.stdin.readline().split())))
    tot = sum(lst) - lst[0] - lst[-1]
    print("KIN" if lst[-2] - lst[1] > 3 else tot)