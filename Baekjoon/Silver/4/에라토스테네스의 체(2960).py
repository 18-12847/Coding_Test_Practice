import sys
n, k = map(int, sys.stdin.readline().split())
lst = [0, 0] + [1] * (n - 1)
cnt = 0
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if lst[j] == 0:
            continue
        cnt += 1
        lst[j] = 0
        if cnt == k:
            print(j)
            exit()