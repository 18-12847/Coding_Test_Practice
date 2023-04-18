import sys
while True:
    a, b = map(int, sys.stdin.readline().split())
    if not a and not b:
        break
    if a < b and not(b % a):
        print("factor")
    elif a > b and not(a % b):
        print("multiple")
    else:
        print("neither")