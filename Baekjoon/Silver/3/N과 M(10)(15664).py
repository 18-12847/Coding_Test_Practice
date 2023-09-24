import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
check = set()
for i in combinations(lst, m):
    check.add(i)
for i in sorted(check):
    print(*i)