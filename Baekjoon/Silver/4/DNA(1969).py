import sys
from collections import defaultdict
input = sys.stdin.readline
n, m = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(n)]
tot, s = 0, ""
for i in range(m):
    dic = defaultdict(int)
    for j in range(n):
        dic[lst[j][i]] += 1
    for k in sorted(dic.items(), key = lambda x: (-x[1], x[0])):
        s += k[0]
        break
    tot += n - max(dic.values())
print(s, tot, sep = "\n")