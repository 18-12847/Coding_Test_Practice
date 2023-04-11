import sys
ans = [1, 1, 2, 2, 2, 8]
tmp = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(len(ans)):
    ans[i] -= tmp[i]
print(*ans, sep=" ")