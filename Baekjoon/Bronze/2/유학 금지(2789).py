import sys
a = sys.stdin.readline().rstrip()
for i in a:
    if i not in "CAMBRIDGE":
        print(i, end = "")