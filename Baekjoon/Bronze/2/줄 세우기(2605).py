import sys
n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
ans = [i + 1 for i in range(n)]
for i in range(n):
    if lst[i]:
        ans.insert(i - lst[i], ans.pop(i))
print(*ans)        