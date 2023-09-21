import sys
from itertools import permutations
input = sys.stdin.readline
n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
for i in permutations(lst, m):
    print(*i)