import sys, math
a, b = map(int, sys.stdin.readline().split())
gcd = math.gcd(a, b)
print(int(a * b / gcd))