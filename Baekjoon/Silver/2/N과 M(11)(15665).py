import sys
from itertools import product
input = sys.stdin.readline
n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
check = set()
for i in product(lst, repeat = m):
    check.add(i)
for i in sorted(check):
    print(*i)