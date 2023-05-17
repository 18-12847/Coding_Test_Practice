import sys
from collections import defaultdict
lst = [sys.stdin.readline().split() for _ in range(int(sys.stdin.readline().rstrip()))]
dic = defaultdict(list)
for i in lst:
    dic[i[0]] = i[1]
ans = []
for i in dic:
    if dic[i] == "enter":
        ans.append(i)
print(*sorted(ans, reverse = True), sep = "\n")