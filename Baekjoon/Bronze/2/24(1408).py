import sys
a = list(map(int, sys.stdin.readline().rstrip().split(":")))
b = list(map(int, sys.stdin.readline().rstrip().split(":")))
tot = (b[0] * 3600 + b[1] * 60 + b[2]) - (a[0] * 3600 + a[1] * 60 + a[2])
if tot < 0:
    tot += (3600 * 24)
print(f"{str(tot // 3600).zfill(2)}:{str((tot - (tot // 3600) * 3600) // 60).zfill(2)}:{str(tot % 60).zfill(2)}")