import sys
input = sys.stdin.readline
n, m = int(input().rstrip()), int(input().rstrip())
lst = sorted(list(map(int, input().split())))
start, end, cnt = 0, n - 1, 0
while start < end:
    if lst[start] + lst[end] == m:
        cnt += 1
        start += 1
        end -= 1
    elif lst[start] + lst[end] > m:
        end -= 1
    else:
        start += 1
print(cnt)