import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline
n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
check = set()
for i in combinations_with_replacement(lst, m):
    check.add(i)
for i in sorted(check):
    print(*i)