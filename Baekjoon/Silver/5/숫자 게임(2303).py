import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = [list(map(int, input().split())) for _ in range(n)]
ans = []
for i in lst:
    big = 0
    for a in range(5):
        for b in range(a+1, 5):
            for c in range(b+1, 5):
                tot = (i[a] + i[b] + i[c]) % 10
                if tot >= big:
                    big = tot
    ans.append(big)
for i in range(n-1, -1, -1):
    if ans[i] == max(ans):
        print(i+1)
        break