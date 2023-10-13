import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if lst[i] < lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - len(set(dp)))

#아래 코드가 왜 훨씬 빠를까
import sys
input = sys.stdin.readline

def main():
    n = int(input().rstrip())
    lst = list(map(int, input().split()))
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if lst[i] < lst[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(n - len(set(dp)))

if __name__ == "__main__":
    main()