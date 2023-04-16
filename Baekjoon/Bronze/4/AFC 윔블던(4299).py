import sys
n, m = map(int, sys.stdin.readline().split())
a = (n + m) // 2
b = n - a
if n < m:
    print("-1")
elif a + b == n and a - b == m:
    print(int(a), int(b))
else:
    print("-1")