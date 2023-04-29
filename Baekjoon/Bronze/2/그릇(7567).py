import sys
s = sys.stdin.readline().rstrip()
tot = 10
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        tot += 5
    else:
        tot += 10
print(tot)