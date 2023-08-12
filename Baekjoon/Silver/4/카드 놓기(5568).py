import sys
from itertools import permutations
input = sys.stdin.readline
n = int(input().rstrip())
k = int(input().rstrip())
lst = [int(input().rstrip()) for _ in range(n)]
ans = set()
for i in permutations(lst, k):
    ans.add("".join(map(str, i)))
print(len(ans))