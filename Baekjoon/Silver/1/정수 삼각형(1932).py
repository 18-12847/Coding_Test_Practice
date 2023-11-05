import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    for j in range(i + 1):
        if not j:
            lst[i][j] += lst[i-1][j]
        elif j == i:
            lst[i][j] += lst[i-1][j-1]
        else:
            lst[i][j] += max(lst[i-1][j], lst[i-1][j-1])
print(max(lst[-1]))