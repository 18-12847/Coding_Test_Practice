import sys
a, b, c = map(int, sys.stdin.readline().split())
print(a * b - c) if a * b >= c else print("0")