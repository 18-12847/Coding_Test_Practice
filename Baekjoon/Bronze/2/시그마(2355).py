import sys
n, m = map(int, sys.stdin.readline().split())
print((n + m) * (abs(m - n) + 1) // 2)