import sys, math
for _ in range(int(sys.stdin.readline().rstrip())):
    lst = list(map(int, sys.stdin.readline().split()))
    tot = 0
    for i in range(1, lst[0]):
        for j in range(i + 1, lst[0] + 1):
            tot += math.gcd(lst[i], lst[j])
    print(tot)