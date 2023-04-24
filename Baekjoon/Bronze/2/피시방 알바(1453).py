import sys
n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
print(len(lst) - len(set(lst)))