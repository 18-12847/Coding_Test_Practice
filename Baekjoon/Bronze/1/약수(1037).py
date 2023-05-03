import sys
n = int(sys.stdin.readline().rstrip())
lst = sorted(list(map(int, sys.stdin.readline().split())))
print(lst[0] * lst[-1] if len(lst) > 1 else lst[0] ** 2)