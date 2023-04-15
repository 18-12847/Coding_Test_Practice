import sys
n, m = map(int, sys.stdin.readline().split())
ans = []
for _ in range(n):
    ans.append(sys.stdin.readline().rstrip())
for i in range(len(ans)):
    print(ans[i][::-1])