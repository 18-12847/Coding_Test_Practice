import sys
from collections import defaultdict
n, m = map(int, sys.stdin.readline().split())
dic = defaultdict(str)
for i in range(n):
    s = sys.stdin.readline().split()
    dic[s[0]] = s[1]
for i in range(m):
    print(dic[sys.stdin.readline().rstrip()])