import sys
lst = [sys.stdin.readline().rstrip() for _ in range(int(sys.stdin.readline().rstrip()))]
cnt = 0
for i in lst:
    tmp = []
    tmp.append(i[0])
    flag = True
    for j in i:
        if j in tmp and j != tmp[-1]:
            flag = False
            break
        else:
            tmp.append(j)
    if flag:
        cnt += 1
print(cnt)