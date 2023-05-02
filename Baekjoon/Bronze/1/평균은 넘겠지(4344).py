import sys
for i in range(int(sys.stdin.readline().rstrip())):
    n = list(map(int, sys.stdin.readline().split()))
    tot = sum(n[1:]) / n[0]
    cnt = 0
    for i in range(1, n[0] + 1):
        if n[i] > tot:
            cnt += 1
    print("{:.3f}%".format((cnt / n[0]) * 100))