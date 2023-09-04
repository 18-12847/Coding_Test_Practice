import sys
input = sys.stdin.readline
c, r = map(int, input().split())
a, b, tot = c, r, c * r
k = int(input().rstrip())
lst = [[0 for i in range(c)] for i in range(r)]
c -= 1
cnt, i, j = 1, r-1, 0
flag = [True, False, False, False]
while cnt <= tot:
    if flag[0] and not flag[3]:
        for x in range(r):
            lst[i-x][j] = cnt
            cnt += 1
        i = j
        r -= 1
        flag[0], flag[1] = False, True
        
    elif flag[1] and not flag[0]:
        for y in range(c):
            lst[j][j+y+1] = cnt
            cnt += 1
        j += c
        c -= 1
        flag[1], flag[2] = False, True

    elif flag[2] and not flag[1]:
        for x in range(r):
            lst[i+x+1][j] = cnt
            cnt += 1
        i += r
        r -= 1
        flag[2], flag[3] = False, True

    elif flag[3] and not flag[2]:
        for y in range(c):
            lst[i][j-y-1] = cnt
            cnt += 1
        j -= c
        c -= 1
        i -= 1
        flag[3], flag[0] = False, True
lst = lst[::-1]
for i in range(b):
    for j in range(a):
        if lst[i][j] == k:
            print(j+1, i+1)
            exit()
else:
    print(0)