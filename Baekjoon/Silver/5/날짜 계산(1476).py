import sys
lst = list(map(int, sys.stdin.readline().split()))
cnt, a, b, c = 1, 1, 1, 1
for _ in range(7980):
    if [a, b, c] == lst:
        print(cnt)
        break    
    a, b, c = a + 1, b + 1, c + 1
    cnt += 1
    if a == 16:
        a = 1
    if b == 29:
        b = 1
    if c == 20:
        c = 1