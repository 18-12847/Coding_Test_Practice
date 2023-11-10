import sys
input = sys.stdin.readline

def pow(a, b):
    if b == 1:
        return a % c
    p = pow(a, b // 2)
    if b % 2 == 0:
        return p * p % c
    else:
        return p * p * a % c

a, b, c = map(int, input().split())
print(pow(a, b))