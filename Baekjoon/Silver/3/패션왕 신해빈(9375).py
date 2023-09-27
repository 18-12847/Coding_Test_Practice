import sys
input = sys.stdin.readline
from collections import defaultdict
for _ in range(int(input().rstrip())):
    dic = defaultdict(int)
    cnt = 1
    for _ in range(int(input().rstrip())):
        name, kind = input().split()
        dic[kind] += 1
    for i in dic:
        cnt *= (dic[i] + 1)
    print(cnt - 1)