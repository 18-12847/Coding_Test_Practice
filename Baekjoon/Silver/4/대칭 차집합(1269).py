import sys
a, b = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
print(len(a) + len(b) - (len(set(a) & set(b)) * 2))