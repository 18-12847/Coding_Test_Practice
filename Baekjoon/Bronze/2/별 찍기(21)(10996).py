import sys
n = int(sys.stdin.readline().rstrip())
s1, s2 = "", ""
for i in range(n):
    if not(i % 2):
        s1 += "*"
        s2 += " "
    else:
        s1 += " "
        s2 += "*"
if n == 1:
    print("*")
else:
    for i in range(n * 2):
        if not(i % 2):
            print(s1)
        else:
            print(s2)