import sys
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline().rstrip()))]
for i in range(len(lst)):
    cnt = 1
    for j in range(len(lst)):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt += 1
    print(cnt, end = " ")