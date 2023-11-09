import sys
input = sys.stdin.readline
cnt = 1
n = int(input().rstrip())
lst = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x: (x[1], x[0]))
start, end = lst[0][0], lst[0][1]
for i in range(1, n):
    s, e = lst[i][0], lst[i][1]
    if end <= s:
        cnt += 1
        start, end = s, e
print(cnt)