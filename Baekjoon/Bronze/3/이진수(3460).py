import sys
t = int(sys.stdin.readline().rstrip())
for i in range(t):
    n = list(reversed(list(bin(int(sys.stdin.readline().rstrip())))[2:]))
    for j in range(len(n)):
        if n[j] == "1":
            print(j, end = " ")