import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
for i in combinations(lst, m):
    print(*i)