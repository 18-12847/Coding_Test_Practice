def solution(n):
    ans = [False, False] + [True] * (n-1)
    for i in range(2, int(n ** 0.5)+1):
        if ans[i]:
            for j in range(i * 2, n+1, i):
                ans[j] = False
    return ans.count(True)