import sys
for i in range(int(sys.stdin.readline().rstrip())):
    cnt = 0
    a, b = map(int, sys.stdin.readline().split())
    for i in range(a, b + 1):
        cnt += str(i).count("0")
    print(cnt)