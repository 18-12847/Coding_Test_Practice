import sys
n = int(sys.stdin.readline())
for _ in range(n):
    ans = ""
    r, s = sys.stdin.readline().split()
    s = list(s)
    for i in s:
        ans += i * int(r)
    print(ans)