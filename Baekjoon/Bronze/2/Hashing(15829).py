import sys
ans = " abcdefghijklmnopqrstuvwxyz"
n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()
tot = 0
for idx, val in enumerate(s):
    tot += (ans.find(val) * (31 ** idx))
print(tot % 1234567891)