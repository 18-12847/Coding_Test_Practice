import sys
n = int(sys.stdin.readline().rstrip())
lst = sorted(list(map(int, sys.stdin.readline().split())))
print(lst[-1] - lst[0])