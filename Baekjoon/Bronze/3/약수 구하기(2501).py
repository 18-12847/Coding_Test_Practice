import sys
a, b = map(int, sys.stdin.readline().split())
ans = [i for i in range(1, a + 1) if a % i == 0]
if len(ans) < b:
    print("0")
else:
    print(ans[b-1])