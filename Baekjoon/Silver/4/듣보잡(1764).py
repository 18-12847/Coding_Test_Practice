import sys
from collections import defaultdict
n, m = map(int, sys.stdin.readline().split())
dic1 = defaultdict(int)
for i in range(n):
    dic1[sys.stdin.readline().rstrip()] = 1
cnt, ans = 0, []
for i in range(m):
    s = sys.stdin.readline().rstrip()
    if dic1[s]:
        cnt += 1
        ans.append(s)
print(cnt)
print(*sorted(ans), sep = "\n")