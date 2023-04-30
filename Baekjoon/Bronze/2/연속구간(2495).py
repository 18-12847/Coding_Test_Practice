import sys
lst = [sys.stdin.readline().rstrip() for _ in range(3)]
for i in lst:
    tot = 1
    tmp = 1
    for j in range(1, len(i)):
        if i[j] == i[j-1]:
            tot += 1
        else:
            if tmp < tot:
                tmp = tot
            tot = 1
    print(tot if tmp < tot else tmp)