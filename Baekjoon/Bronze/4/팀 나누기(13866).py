import sys
ans = list(map(int, sys.stdin.readline().split()))
print(abs((max(ans) + min(ans)) - (sum(ans) - max(ans) - min(ans))))