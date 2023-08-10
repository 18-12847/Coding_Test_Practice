import sys
input = sys.stdin.readline
lst = sorted([list(map(int, input().split())) for _ in range(int(input().rstrip()))], key = lambda x: (x[0], x[1]))
tot = 0
for i in lst:
    tot = max(tot, i[0])
    tot += i[1]
print(tot)    