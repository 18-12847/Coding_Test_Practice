import sys
from  collections import defaultdict
dic = defaultdict(int)
n = int(sys.stdin.readline().rstrip())
lst = [int(sys.stdin.readline().rstrip()) for i in range(n)]
for i in sorted(set(lst)):
    dic[i] = 0
for i in lst:
    dic[i] += 1
maxx = [0, 0]
for i in dic:
    if maxx[1] < dic[i]:
        maxx = [i, dic[i]]
print(maxx[0])