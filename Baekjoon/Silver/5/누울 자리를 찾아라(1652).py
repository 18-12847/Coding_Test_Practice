import sys
n = int(sys.stdin.readline().rstrip())
lst = [sys.stdin.readline().rstrip() for _ in range(n)]
row, col = 0, 0
for i in lst:
    tmp = i.split("X")
    for j in tmp:
        if len(j) > 1:
            row += 1
lst2 = [list(lst[i]) for i in range(n)]
for i in range(n):
    for j in range(n):
        lst2[i][j] = lst[n-j-1][i]
for i in lst2:
    tmp = "".join(i).split("X")
    for j in tmp:
        if len(j) > 1:
            col += 1
print(row, col)