import sys
s = "".join(sorted(sys.stdin.readline().rstrip(), reverse = True))
print(-1 if int(s) % 30 else s)