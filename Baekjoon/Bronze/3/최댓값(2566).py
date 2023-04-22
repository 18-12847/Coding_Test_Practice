import sys
lst = [list(map(int, sys.stdin.readline().split())) for i in range(9)]
maxx, x, y = 0, 0, 0
for idx, val in enumerate(lst):
    if maxx < max(lst[idx]):
        maxx = max(lst[idx])
        x, y = idx, lst[idx].index(max(lst[idx]))
print(maxx)
print(x + 1, y + 1)