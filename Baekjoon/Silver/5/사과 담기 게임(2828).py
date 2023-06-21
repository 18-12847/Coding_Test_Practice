import sys
n, k = map(int, sys.stdin.readline().split())
n = [i + 1 for i in range(n)]
start, end, cnt = 0, k, 0
for i in range(int(sys.stdin.readline().rstrip())):
    a = int(sys.stdin.readline().rstrip())
    if a < n[start]:
        while a not in n[start:end]:
            start -= 1
            end -= 1
            cnt += 1
    elif a in n[start:end]:
        continue
    else:
        while a not in n[start:end]:
            start += 1
            end += 1
            cnt += 1
print(cnt)