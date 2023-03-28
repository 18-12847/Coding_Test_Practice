def solution(t, p):
    ans, cnt = [], 0
    t = list(t)
    for i in range(len(t)-len(p)+1):
        ans.append(int("".join(t[i:i+len(p)])))
    p = int(p)
    for i in ans:
        if i <= p:
            cnt += 1
    return cnt