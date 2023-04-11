import sys
n = int(sys.stdin.readline())
ans = list(map(int, sys.stdin.readline().split()))
print(ans[ans.index(min(ans))], ans[ans.index(max(ans))])