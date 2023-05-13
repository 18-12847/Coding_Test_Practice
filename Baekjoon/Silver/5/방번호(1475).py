import sys
from collections import defaultdict
n = sys.stdin.readline().rstrip()
n = n.replace("9", "6")
dic = defaultdict(int)
for i in n:
    dic[int(i)] += 1
dic[6] = dic[6] // 2 + 1 if dic[6] % 2 else dic[6] // 2
print(max([i[1] for i in dic.items()]))