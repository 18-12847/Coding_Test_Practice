import sys
for i in range(int(sys.stdin.readline().rstrip())):
    lst = list(sys.stdin.readline().split())
    tot = float(lst[0])
    for j in range(1, len(lst)):
        if lst[j] == "@":
            tot *= 3
        elif lst[j] == "%":
            tot += 5
        else:
            tot -= 7
    print("{:.2f}".format(tot))