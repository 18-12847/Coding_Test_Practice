import sys
from collections import defaultdict
n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
dic = defaultdict(int)
for i in lst:
    dic[i] += 1
n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
for i in lst:
    print(dic[i] if dic[i] else 0, end = " ")