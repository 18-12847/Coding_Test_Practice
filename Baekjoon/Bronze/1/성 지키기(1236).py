import sys
n, m = map(int, sys.stdin.readline().split())
lst = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
cnt = 0
for i in lst:
    if i.count("X") == 0:
        cnt += 1
cnt1 = 0
for i in range(m):
    tmp = 0
    for j in range(n):
        if lst[j][i] == "X":
            tmp += 1
    if tmp == 0:
        cnt1 += 1
print(max(cnt, cnt1))