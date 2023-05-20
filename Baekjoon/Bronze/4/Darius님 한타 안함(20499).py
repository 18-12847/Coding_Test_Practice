import sys
k, d, a = map(int, sys.stdin.readline().split("/"))
print("hasu" if k + a < d or d == 0 else "gosu")