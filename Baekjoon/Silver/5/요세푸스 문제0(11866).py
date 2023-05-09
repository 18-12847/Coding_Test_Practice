import sys
n, k = map(int, sys.stdin.readline().split())
lst = [i + 1 for i in range(n)]
tmp = k - 1
ans = "<"
for _ in range(n - 1):
    ans += str(lst.pop(tmp)) + ", "
    tmp = (tmp + k - 1) % len(lst)
ans += str(lst.pop()) + ", "
print(ans[:-2] + ">")