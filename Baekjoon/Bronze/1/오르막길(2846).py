import sys
n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
tmp, tot, minn, flag = [], [], 0, False
for i in range(n):
    if lst[i] > minn and lst[i] > lst[i - 1]:
        tmp.append(lst[i])
        minn = min(tmp)
        flag = True
    else:
        if len(tmp) > 1:
            tot.append(tmp[-1] - tmp[0])
        tmp = []
        minn = lst[i]
        tmp.append(minn)
        flag = False
if flag:
    tot.append(tmp[-1] - minn)
print(max(tot) if tot else 0)