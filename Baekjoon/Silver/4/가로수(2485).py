import sys, math
input = sys.stdin.readline
n = int(input().rstrip())
lst = sorted([int(input().rstrip()) for _ in range(n)])
ans = set()
for i in range(1, n):
    ans.add(lst[i] - lst[i-1])
ans = list(ans)
for i in range(1, len(ans)):
    ans[i] = math.gcd(ans[i], ans[i - 1])
print((lst[-1] - lst[0]) // ans[-1] - n + 1)