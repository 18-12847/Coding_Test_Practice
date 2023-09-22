import sys
from itertools import product
input = sys.stdin.readline
n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
for i in product(lst, repeat = m):
    print(*i)