import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = sorted(list(map(int, input().split())))
x = int(input().rstrip())
left, right, cnt = 0, n - 1, 0
while left < right:
    if lst[left] + lst[right] == x:
        cnt += 1
        left += 1
        right -= 1
    elif lst[left] + lst[right] > x:
        right -= 1
    else:
        left += 1
print(cnt)