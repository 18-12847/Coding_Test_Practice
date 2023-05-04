import sys
cnt = 1
while True:
    l, p, v = map(int, sys.stdin.readline().split())
    if [l, p, v] == [0, 0, 0]:
        break
    print(f"Case {cnt}: {v // p * l + (l if (v % p) > l else v % p)}")
    cnt += 1