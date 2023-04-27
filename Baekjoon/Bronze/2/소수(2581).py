import sys
m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
lst = [False, False] + [True] * 9999
for i in range(2, int(10000 ** 0.5) + 1):
    for j in range(i + i, 10001, i):
        lst[j] = False
ans = [i for i in range(m, n + 1) if lst[i]]
if ans:
    print(sum(ans), ans[0], sep = "\n")
else:
    print("-1")