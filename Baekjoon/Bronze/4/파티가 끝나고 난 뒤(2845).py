import sys
a, b = map(int, sys.stdin.readline().split())
ans = list(map(int, sys.stdin.readline().split()))
for i in range(len(ans)):
    ans[i] -= a * b
print(*ans)