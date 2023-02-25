def solution(s, n):
    tmp = sorted([s[i][n] for i in range(len(s))])
    ans = []
    s.sort()
    for i in range(len(s)):
        for j in range(len(s)):
            if tmp[i] == s[j][n]:
                ans.append(s[j])
                s.pop(s.index(s[j]))
                break
    return ans