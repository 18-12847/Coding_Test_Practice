import sys
n = int(sys.stdin.readline().rstrip())
cnt1 = 0
def dp(n):
    global cnt1
    lst = [0, 1]
    for i in range(2, n + 1):
        cnt1 += 1
        lst.append(lst[i - 2] + lst[i - 1])
    return lst[-1]
print(dp(n), cnt1 - 1)