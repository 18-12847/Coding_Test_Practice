import sys
s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""
n, b = map(int, sys.stdin.readline().split())
while n > 1:
    ans += s[n % b]
    n //= b
ans += s[n]
print(ans[::-1].lstrip("0"))