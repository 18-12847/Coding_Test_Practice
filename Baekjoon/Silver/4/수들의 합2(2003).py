import sys
a, b = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
cnt, start, end = 0, 0, 0
while start != a and end != a:
    if sum(lst[start:end+1]) == b:
        cnt += 1
        start += 1
        end += 1
    elif sum(lst[start:end+1]) > b:
        start += 1
    else:
        end += 1
print(cnt)