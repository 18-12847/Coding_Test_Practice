import sys
input = sys.stdin.readline
while True:
    try:
        n = int(input().rstrip())
        a, cnt = 1, 1
        while a % n != 0:
            a = a * 10 + 1
            cnt += 1
        print(cnt)
    except:
        break