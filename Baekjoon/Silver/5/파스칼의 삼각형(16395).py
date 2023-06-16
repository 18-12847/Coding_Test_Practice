import sys
n, k = map(int, sys.stdin.readline().split())
lst, cnt = [[1], [1, 1]], 0
for i in range(2, n):
    lst.append([])
    for j in range(i + 1):
        if j == 0:lst[i].append(1)
        elif j == i:lst[i].append(1)
        else:lst[i].append(lst[i-1][j-1] + lst[i-1][j])
print(lst[n-1][k-1])