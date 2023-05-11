import sys, math
a, b = map(int, sys.stdin.readline().split(":"))
gcd = math.gcd(a, b)
print(f"{int(a / gcd)}:{int(b / gcd)}")