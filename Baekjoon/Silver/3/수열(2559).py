import sys
input = sys.stdin.readline
n, k = map(int, input().split())
lst = list(map(int, input().split()))
left, right, tot = 0, k, sum(lst[:k])
ans = tot
while right < n:
    tot += lst[right] - lst[left] #포인터가 증가하면 오른쪽을 더해주고 왼쪽을 빼준다
    ans = max(tot, ans)
    left += 1
    right += 1
print(ans)