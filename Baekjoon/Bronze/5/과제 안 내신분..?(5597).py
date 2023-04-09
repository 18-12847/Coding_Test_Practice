import sys
tmp = [i for i in range(1, 31)]
for i in range(28):
    a = int(sys.stdin.readline())
    del tmp[tmp.index(a)]
print(*tmp, sep="\n")