import sys
input = sys.stdin.readline
n = int(input().rstrip())
size = 4 * n - 3
lst = [[" " for _ in range(size)] for _ in range(size)]

def 별(n, x, y):
    if n == 1:
        lst[x][y] = "*"
        return
    size = 4 * n - 3
    for i in range(size):
        lst[x][y+i] = "*"
        lst[x+i][y] = "*"
        lst[x+size-1][y+i] = "*"
        lst[x+i][y+size-1] = "*"
    별(n-1, x+2, y+2)
별(n, 0, 0)
for i in lst:
    print("".join(i))