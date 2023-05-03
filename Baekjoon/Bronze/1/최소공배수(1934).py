import sys, math
for i in range(int(sys.stdin.readline().rstrip())):
    a, b = map(int, sys.stdin.readline().split())
    gcd = math.gcd(a, b)
    print(int(a * b / gcd))