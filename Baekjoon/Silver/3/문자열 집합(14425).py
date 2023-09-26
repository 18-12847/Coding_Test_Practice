import sys
input = sys.stdin.readline
from collections import defaultdict
dic = defaultdict(int)
n, m = map(int, input().split())
for _ in range(n):
    dic[input().rstrip()] = 0
for _ in range(m):
    s = input().rstrip()
    if s in dic:
        dic[s] += 1
print(sum(dic.values()))