def solution(n):
    ans, tot = [], 0
    while n > 2:
        tmp = n % 3
        n //= 3
        ans.append(tmp)
    ans.append(n)
    for i in range(len(ans)):
        tot += ans[i] * (3 ** (len(ans) - i - 1))
    return tot