import sys
ans = [int(sys.stdin.readline()) for _ in range(5)]
print(min(ans[0:3]) + min(ans[3:]) - 50)