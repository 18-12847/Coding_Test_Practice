import sys
ans = []
for _ in range(6):
    ans.append(int(sys.stdin.readline()))
print(sum(ans) - min(ans[0:4]) - min(ans[4:]))