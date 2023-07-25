import sys
from collections import defaultdict
dic = defaultdict(int)
for i in range(int(sys.stdin.readline().rstrip())):
    dic[sys.stdin.readline().rstrip()] += 1
print(sorted(dic.items(), key = lambda x : (-x[1], x[0]))[0][0])