import sys
tot = []
for i in range(int(sys.stdin.readline().rstrip())):
    lst = sorted(list(map(int, sys.stdin.readline().split())))
    if len(set(lst)) == 1:
        tot.append(10000 + lst[0] * 1000)
    elif len(set(lst)) == 3:
        tot.append(max(lst) * 100)
    else:
        tot.append(1000 + lst[1] * 100)
print(max(tot))