import sys
inp = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
lst = [["o" for _ in range(101)] for _ in range(101)]
for i in inp:
    for j in range(i[0], i[2]):
        for k in range(i[1], i[3]):
            lst[j][k] = "x"
tot = 0
for i in lst:
    tot += i.count("x")
print(tot)