import sys
ans = [int(sys.stdin.readline().rstrip()) for _ in range(5)]
tot = 0
for i in ans:
    if i < 40:
        tot += 40
    else:
        tot += i
print(int(tot / 5))