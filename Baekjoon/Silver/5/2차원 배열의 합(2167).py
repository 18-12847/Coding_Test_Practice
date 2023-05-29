import sys
n, m = map(int, sys.stdin.readline().split())
lst1 = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
k = int(sys.stdin.readline().rstrip())
lst2 = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
for i in lst2:
    tot = 0
    for j in range(i[0], i[2] + 1):
        tot += sum(lst1[j-1][i[1]-1:i[3]])
    print(tot)