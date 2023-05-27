import sys
s = sys.stdin.readline().rstrip()
a, b = s.split("1"), s.split("0")
print(min(len(a) - a.count(""), len(b) - b.count("")))