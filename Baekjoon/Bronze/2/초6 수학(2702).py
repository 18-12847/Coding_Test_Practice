import sys, math
for i in range(int(sys.stdin.readline().rstrip())):
    a, b = map(int, sys.stdin.readline().split())
    print(int(a * b / math.gcd(a, b)), math.gcd(a, b))