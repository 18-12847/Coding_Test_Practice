import sys
s = sys.stdin.readline().rstrip()
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b = "DEFGHIJKLMNOPQRSTUVWXYZABC"
for i in s:
    print(a[b.find(i)], end = "")