import sys
from collections import defaultdict
dic = defaultdict(int)
n = int(sys.stdin.readline().rstrip())
for i in list(map(int, sys.stdin.readline().split())):
    dic[i] += 1
m = int(sys.stdin.readline().rstrip())
for j in list(map(int, sys.stdin.readline().split())):
    if dic[j] == 1:
        print("1", end = " ")
    else:
        print("0", end = " ")