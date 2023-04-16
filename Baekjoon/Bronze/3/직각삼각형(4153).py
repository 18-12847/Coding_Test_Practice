import sys
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a + b + c == 0: break
    print("right") if max(a, b, c) ** 2 == min(a, b, c) ** 2 + ((a + b + c) - max(a, b, c) - min(a, b, c)) ** 2 else print("wrong")