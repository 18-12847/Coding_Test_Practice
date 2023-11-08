import sys
input = sys.stdin.readline
n, r, c = map(int, input().split())
tot = 0
while n:
    n -= 1
    half = 2 ** n
    if r < half and c < half:
        tot += half ** 2 * 0
    elif r < half and c >= half:
        tot += half ** 2 * 1
        c -= half
    elif r >= half and c < half:
        tot += half ** 2 * 2
        r -= half
    else:
        tot += half ** 2 * 3
        r -= half
        c -= half
print(tot)