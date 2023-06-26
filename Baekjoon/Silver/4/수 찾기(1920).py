import sys
from collections import defaultdict
n = int(sys.stdin.readline().rstrip())
lst1 = list(map(int, sys.stdin.readline().split()))
dic = defaultdict(int)
for i in lst1:
    dic[i] += 1
n = int(sys.stdin.readline().rstrip())
lst2 = list(map(int, sys.stdin.readline().split()))
for i in lst2:
    if dic[i]:
        print(1)
    else:
        print(0)