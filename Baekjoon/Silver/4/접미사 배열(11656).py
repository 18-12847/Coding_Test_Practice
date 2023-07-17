import sys
s = sys.stdin.readline().rstrip()
print(*sorted([s[i:] for i in range(len(s))]), sep = "\n")