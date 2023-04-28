import sys
n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
ans = []
for i in range(0, n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if lst[i] + lst[j] + lst[k] <= m:
                ans.append(lst[i] + lst[j] + lst[k])
print(max(ans))