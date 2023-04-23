import sys
n, m, k = map(int, sys.stdin.readline().split())
print(min(n // 2, m, (n + m - k) // 3))