import sys
from collections import defaultdict
input = sys.stdin.readline
dic = defaultdict(int)
tot = 0
for i in range(int(input().rstrip())):
    s = input().rstrip()
    if s == "ENTER":
        dic = defaultdict(int)
    elif dic[s]:
        continue
    else:
        dic[s] = 1
        tot += 1
print(tot)