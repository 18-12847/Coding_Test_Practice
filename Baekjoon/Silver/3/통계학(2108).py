import sys
from collections import defaultdict
input = sys.stdin.readline
dict = defaultdict(int)
n = int(input().rstrip())
lst = sorted([int(input().rstrip()) for _ in range(n)])
for i in lst:
    dict[i] += 1
dict = sorted(dict.items(), key = lambda x:(x[1], -x[0]))[::-1]
print(round(sum(lst)/n))
print(lst[len(lst)//2])
if n == 1:
    print(*lst)
else:
    print(dict[1][0] if dict[0][1] == dict[1][1] else dict[0][0])
print(lst[-1] - lst[0])