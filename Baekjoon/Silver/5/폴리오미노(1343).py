import sys
s = sys.stdin.readline().rstrip().replace("XXXX", "AAAA").replace("XX", "BB")
print(-1 if "X" in s else s)