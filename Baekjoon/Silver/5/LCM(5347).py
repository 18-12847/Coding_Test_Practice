import sys, math
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline().rstrip()))]
for i in lst:
    gcd = math.gcd(i[0], i[1])
    print(int(i[0] * i[1] / gcd))