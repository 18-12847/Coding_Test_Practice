import sys
input = sys.stdin.readline
for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    lst = [list(map(int, input().split())) for _ in range(2)]
    if n > 1:
        lst[0][1] += lst[1][0]
        lst[1][1] += lst[0][0]
        for i in range(2, n):
            lst[0][i] = max(lst[1][i - 1], lst[1][i - 2]) + lst[0][i]
            lst[1][i] = max(lst[0][i - 1], lst[0][i - 2]) + lst[1][i]
    print(max(lst[0][-1], lst[1][-1]))