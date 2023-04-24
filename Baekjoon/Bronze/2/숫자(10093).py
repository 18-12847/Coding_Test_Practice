import sys
a, b = list(map(int, sys.stdin.readline().split()))
print(0 if abs(b - a) - 1 < 0 else abs(b - a) - 1)
for i in range(min(a, b) + 1, max(a, b)):
    print(i, end = " ")