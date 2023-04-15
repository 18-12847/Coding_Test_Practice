import sys
n = int(sys.stdin.readline())
cnt = 0
if n < 10:
    n *= 10
tmp = n
while True:
    a = tmp // 10
    b = tmp % 10
    tmp = b * 10 + (a + b) % 10 
    cnt += 1
    if n == tmp:
        break
print(cnt)

import sys
n = int(sys.stdin.readline())
cnt = 0
tmp = n
while True:
    a, b = tmp // 10, tmp % 10
    tmp = b * 10 + (a + b) % 10 
    cnt += 1
    if n == tmp:
        break
print(cnt)

import sys
n = int(sys.stdin.readline())
cnt, tmp = 0, n
while True:
    tmp = tmp % 10 * 10 + (tmp // 10 + tmp % 10) % 10 
    cnt += 1
    if n == tmp:
        break
print(cnt)