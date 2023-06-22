import sys
h, w = map(int, sys.stdin.readline().split())
lst = [sys.stdin.readline().rstrip() for _ in range(h)]
for i in lst:
    if i[0] == ".":
        cnt = -1
    else:
        cnt = 0
    for j in i:
        if j == "c":
            cnt = 0
            print(cnt, end = " ")
        elif cnt == -1 and j == ".":
            print(cnt, end = " ")
        else:
            cnt += 1
            print(cnt, end = " ")
    print()