import sys
tot = int(sys.stdin.readline())
n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    tot -= a * b
if tot == 0:
    print("Yes")
else:
    print("No")