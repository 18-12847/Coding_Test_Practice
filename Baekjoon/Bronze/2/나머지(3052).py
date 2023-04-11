import sys
cnt, ans = 0, []
for _ in range(10):
    n = int(sys.stdin.readline())
    ans.append(n % 42)
print(len(list(set(ans))))