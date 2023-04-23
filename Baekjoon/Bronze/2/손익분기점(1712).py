import sys
a, b, c = map(int, sys.stdin.readline().split())
print(a // (c - b) + 1 if c - b > 0 else -1)