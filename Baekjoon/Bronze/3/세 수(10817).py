import sys
ans = list(map(int, sys.stdin.readline().split()))
print(sum(ans) - max(ans) - min(ans))