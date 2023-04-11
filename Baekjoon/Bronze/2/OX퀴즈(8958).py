import sys
n = int(sys.stdin.readline())
for _ in range(n):
    cnt, tot = 0, 0
    a = list(sys.stdin.readline().rstrip())
    for i in a:
        if i == "O":
            cnt += 1
        else:
            tot += sum([i for i in range(cnt+1)])
            cnt = 0
    print(tot + sum([i for i in range(cnt+1)]))