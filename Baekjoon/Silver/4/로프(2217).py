import sys
input = sys.stdin.readline
lst = [int(input().rstrip()) for _ in range(int(input().rstrip()))]
ans = [(i + 1) * val for i, val in enumerate(sorted(lst)[::-1])]
print(max(ans))