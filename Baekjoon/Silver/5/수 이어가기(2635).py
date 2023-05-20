import sys
n = int(sys.stdin.readline().rstrip())
lst = [[]]
if n == 1:
    for i in range(1):
        m = n
        tmp = [m, m - i]
        while m > 0:
            tmp.append(tmp[-2] - tmp[-1])
            m -= tmp[-1]
            lst.append(tmp)
else:
    for i in range(1, n + 1):
        m = n
        tmp = [m, m - i]
        while m > 0:
            if tmp[-2] - tmp[-1] > -1:
                tmp.append(tmp[-2] - tmp[-1])
            m -= tmp[-1]
        if len(lst[-1]) < len(tmp):
            lst.append(tmp)
print(len(lst[-1]))
print(*lst[-1])