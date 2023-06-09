import sys
from collections import defaultdict
dic = defaultdict(int)
n, m = map(int, sys.stdin.readline().split())
for _ in range(2):
    for i in list(map(int, sys.stdin.readline().split())):
        dic[i] += 1
for i in sorted(dic):
    print((str(i) + " ") * dic[i], end = "")