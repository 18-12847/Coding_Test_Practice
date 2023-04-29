import sys
n, m = map(int, sys.stdin.readline().split())
lst = [i for i in range(1, n + 1)]
for a in range(1, m+1):
    i, j = map(int, sys.stdin.readline().split())
    tmp = list(reversed(lst[i-1:j]))
    for b in range(i, j + 1):
        lst[b-1] = tmp[b-i]
print(*lst)