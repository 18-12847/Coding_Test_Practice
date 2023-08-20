import sys
from collections import defaultdict
input = sys.stdin.readline
a = input().rstrip()
lst = list(map(int, input().split()))
dic = defaultdict(list)
cnt = 0
for i in sorted(lst):
    dic[i].append(cnt)
    cnt += 1
for i in lst:
    print(dic[i][0], end = " ")
    dic[i].pop(0)