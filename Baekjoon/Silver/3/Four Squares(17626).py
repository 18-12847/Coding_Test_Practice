import sys #브루트포스
input = sys.stdin.readline
n = int(input().rstrip())
dp = [i*i for i in range(1, 224)]
if n in dp:
    print(1)
    exit()
for i in range(int(n ** 0.5)):
    if n - dp[i] in dp:
        print(2)
        exit()
for i in range(int(n ** 0.5)):
    for j in range(int(n ** 0.5)):
        if n - dp[i] - dp[j] in dp:
            print(3)
            exit()
print(4)

# pypy로 해야 통과(dp)
# n = int(input().rstrip())
# dp = [0] + [4] * n
# for i in range(1, int(n ** 0.5) + 1):
#     for j in range(i * i, n + 1):
#         dp[j] = min(dp[j], dp[j - i * i] + 1)
# print(dp[n])