import sys
s = sys.stdin.readline().rstrip()
if s[:len(s) // 2 + 1] == s[:-(len(s) // 2 + 2):-1]:
    print("1")
else:
    print("0")