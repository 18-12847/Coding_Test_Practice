import sys, math
n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
ans = []
if n == 2:
    n2 = math.gcd(lst[0], lst[1])
    for i in range(1, int(n2 ** 0.5) + 1):
        if n2 % i == 0:
            ans.append(i)
            ans.append(int(n2 / i))
    print(*sorted(set(ans)), sep = "\n")
else:
    n3 = math.gcd(math.gcd(lst[0], lst[1]), lst[2])
    for i in range(1, int(n3 ** 0.5) + 1):
        if n3 % i == 0:
            ans.append(i)
            ans.append(int(n3 / i))
    print(*sorted(set(ans)), sep = "\n")