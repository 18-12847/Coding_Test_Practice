import sys
from collections import defaultdict
for i in range(int(sys.stdin.readline().rstrip())):
    a = int(sys.stdin.readline().rstrip())
    lst1 = list(map(int, sys.stdin.readline().split()))
    dic = defaultdict(int)
    for i in lst1:
        dic[i] += 1
    a = int(sys.stdin.readline().rstrip())
    lst2 = list(map(int, sys.stdin.readline().split()))
    for i in lst2:
        print(1 if dic[i] else 0)