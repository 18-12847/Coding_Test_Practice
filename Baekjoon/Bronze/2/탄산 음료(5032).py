import sys
e, f, c = map(int, sys.stdin.readline().split())
cnt = 0
while e + f >= c:
    cnt += (e + f) // c
    e = (e + f) // c + (e + f) % c 
    f = 0
print(cnt)