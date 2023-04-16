import sys
a, b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline().rstrip()) * 2
if a + b >= c:
    print(a + b - c)
else:
    print(a + b)