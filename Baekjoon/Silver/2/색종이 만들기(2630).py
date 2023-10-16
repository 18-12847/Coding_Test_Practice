import sys
input = sys.stdin.readline

def div(x, y, n):
    start = lst[y][x]
    half = n // 2
    for i in range(y, y + n):
        for j in range(x, x + n):
            if start != lst[i][j]:
                div(x, y, half)
                div(x, y + half, half)
                div(x + half, y, half)
                div(x + half, y + half, half)
                return
    if not start:
        ans[0] += 1
    else:
        ans[1] += 1

n = int(input().rstrip())
lst = [list(map(int, input().split())) for _ in range(n)]
ans = [0, 0]
div(0, 0, n)
print(*ans, sep = "\n")