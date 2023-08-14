import sys, math
input = sys.stdin.readline
n = int(input().rstrip())
tot = 0
if n < 100:
    print(n)
else:
    for i in range(100, n + 1):
        i = str(i)
        if (int(i[0]) - int(i[1]) == int(i[1]) - int(i[2])) or (int(i[0]) - int(i[1]) == int(i[1]) - int(i[2])):
            tot += 1
    print(tot + 99)