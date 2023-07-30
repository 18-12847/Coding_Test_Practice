import sys
from collections import defaultdict
dic = defaultdict(int)
input = sys.stdin.readline
a, p = input().split()
dic[int(a)] += 1
cnt = 0
flag = False
while True:
    tot = 0
    for i in list(a):
        tot += int(i) ** int(p)
    dic[tot] += 1
    a = str(tot)
    for i in dic:
        if dic[int(i)] == 3:
            flag = True
            break
    if flag:
        break
for i in dic:
    if dic[i] == 1:
        cnt += 1
print(cnt)