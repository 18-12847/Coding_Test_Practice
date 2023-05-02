import sys
cnt = [0] * 10001
for i in range(int(sys.stdin.readline().rstrip())):
    cnt[int(sys.stdin.readline().rstrip())] += 1
for i in range(10001):
    if cnt[i]:
        for _ in range(cnt[i]):
            print(i)