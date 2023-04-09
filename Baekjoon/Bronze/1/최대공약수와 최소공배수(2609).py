import math
import sys
a, b = map(int, sys.stdin.readline().split())
g = math.gcd(a, b)
print(g)
print(int(g * (a / g) * (b / g)))