import sys
input = sys.stdin.readline
s = input().rstrip()
s_len = len(s)
inp = input().rstrip()
tot, i = 0, 0
while i <= s_len - len(inp):
    if s[i:i+len(inp)] == inp:
        tot += 1
        i += len(inp)
    else:
        i += 1
print(tot)