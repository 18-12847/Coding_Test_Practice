import sys
for i in range(int(sys.stdin.readline().rstrip())):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    lst = [i for i in range(1, n + 1)]
    for a in range(k):
        for b in range(1, n):
            lst[b] += lst[b - 1]
    print(lst[n - 1])