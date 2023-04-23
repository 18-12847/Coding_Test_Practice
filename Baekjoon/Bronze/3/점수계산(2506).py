import sys
n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
cnt, tot = 0, 0
for i in range(n):
    if lst[i] == 1:
        tot += 1
        cnt += tot
    else:
        tot = 0
print(cnt)