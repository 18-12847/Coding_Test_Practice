import sys
n, m, l = map(int, sys.stdin.readline().split())
lst = [i + 1 for i in range(n)]
tot = [0] * n
cnt = 0
while max(tot) != m:
    if tot[cnt] % 2:
        tot[cnt] += 1
        cnt = (cnt + l) % n
    else:
        tot[cnt] += 1
        cnt = (cnt - l) % n
print(sum(tot) - 1)