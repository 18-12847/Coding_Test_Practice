def solution(s):
    ans = []
    t, f = 0, 0
    start, cnt = 0, 0
    for i in range(len(s)):
        x = s[start]
        if x == s[i]:
            t += 1
        else:
            f += 1
        if t == f:
            ans.append(s[start:start+t+f])
            cnt += 1
            start += t+f
            t, f = 0, 0
    if len("".join(ans)) != len(s):
        ans.append(s[start:])
    return len(ans)