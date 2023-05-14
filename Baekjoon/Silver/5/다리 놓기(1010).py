import sys, math
for i in range(int(sys.stdin.readline().rstrip())):
    n, m = map(int, sys.stdin.readline().split())
    print(int(math.factorial(max(n, m)) / (math.factorial(max(n, m) - min(n, m)) * math.factorial(min(n, m)))))