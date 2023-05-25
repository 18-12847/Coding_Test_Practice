import sys
lst = [list(map(int, sys.stdin.readline().split())) for i in range(int(sys.stdin.readline().rstrip()))]
ans = list(list(0 for _ in range(101)) for _ in range(101))
for i in lst:
    for j in range(i[0], i[0] + 10):
        for k in range(i[1], i[1] + 10):
            ans[j][k] = 1
print(sum([sum(i) for i in ans]))