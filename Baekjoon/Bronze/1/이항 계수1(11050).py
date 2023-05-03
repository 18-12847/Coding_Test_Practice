import sys
from itertools import combinations
n, k = map(int, sys.stdin.readline().split())
lst = [i + 1 for i in range(n)]
print(len(list(combinations(lst, k))))