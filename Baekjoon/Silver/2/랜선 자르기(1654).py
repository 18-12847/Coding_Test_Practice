import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = [int(input().rstrip()) for _ in range(n)]
left, right = 1, max(lst)
ans = 0
while left <= right:
    tot = 0
    mid = (left + right) // 2
    for i in lst:
        tot += i // mid
    if tot < m:
        right = mid - 1
    else:
        ans = mid
        left = mid + 1
print(ans)