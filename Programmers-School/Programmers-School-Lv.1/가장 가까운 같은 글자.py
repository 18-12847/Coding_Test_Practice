def solution(s):
    ans = [-1]
    for i in range(1, len(s)):
        for j in range(i-1, -1, -1):
            if s[j] == s[i]:
                tmp = i - j
                break
        else:
            tmp = -1
        ans.append(tmp)
    return ans