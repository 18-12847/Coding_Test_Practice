import sys
n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
ans = [False, False] + [True] * 999
for i in range(2, int(1000 ** 0.5) + 1):
    for j in range(i + i, 1001, i):
        ans[j] = False
print(sum([1 for i in lst if ans[i]]))