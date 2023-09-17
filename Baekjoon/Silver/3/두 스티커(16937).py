import sys
input = sys.stdin.readline
h, w = map(int, input().split())
n = int(input().rstrip())
lst = []
for _ in range(n):
    r, c = map(int, input().split())
    if max(r, c) > max(h, w) or min(r, c) > min(h, w):
        continue
    lst.append([r, c])
if len(lst) == 1:
    print(0)
    exit()
max_area = 0
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        area = lst[i][0] * lst[i][1] + lst[j][0] * lst[j][1]
        if lst[i][0] + lst[j][0] <= h and max(lst[i][1], lst[j][1]) <= w:
            max_area = max(max_area, area)
        if max(lst[i][0], lst[j][0]) <= h and lst[i][1] + lst[j][1] <= w:
            max_area = max(max_area, area)
        if lst[i][1] + lst[j][0] <= h and max(lst[i][0], lst[j][1]) <= w:
            max_area = max(max_area, area)
        if max(lst[i][1], lst[j][0]) <= h and lst[i][0] + lst[j][1] <= w:
            max_area = max(max_area, area)
        if lst[i][0] + lst[j][1] <= h and max(lst[i][1], lst[j][0]) <= w:
            max_area = max(max_area, area)
        if max(lst[i][0], lst[j][1]) <= h and lst[i][1] + lst[j][0] <= w:
            max_area = max(max_area, area)
        if lst[i][1] + lst[j][1] <= h and max(lst[i][0], lst[j][0]) <= w:
            max_area = max(max_area, area)
        if max(lst[i][1], lst[j][1]) <= h and lst[i][0] + lst[j][0] <= w:
            max_area = max(max_area, area)
print(max_area)