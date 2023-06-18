import sys
a, b, n = map(int, sys.stdin.readline().split())
for _ in range(n):
    a = (a % b) * 10
print(a // b)