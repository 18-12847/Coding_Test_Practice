import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = list(map(int, input().split()))
dic = {}
for idx, val in enumerate(sorted(set(lst))):
    dic[val] = idx
for i in lst:
    print(dic[i], end = " ")