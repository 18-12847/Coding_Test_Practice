def solution(s):
    ans = []
    s = s.split(" ")
    for i in range(len(s)):
        tmp = list(s[i])
        for j in range(len(tmp)):
            if j % 2 == 0:
                tmp[j] = tmp[j].upper()
            else:
                tmp[j] = tmp[j].lower()
        ans.append("".join(tmp))
    return " ".join(ans)