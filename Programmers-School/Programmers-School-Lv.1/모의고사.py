def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans, tmp = [1, 2, 3], [0, 0, 0]
    for i in range(len(answers)):
        if a[i % len(a)] == answers[i]:
            tmp[0] += 1
        if b[i % len(b)] == answers[i]:
            tmp[1] += 1
        if c[i % len(c)] == answers[i]:
            tmp[2] += 1
    if tmp[0] == tmp[1] == tmp[2]:
        return ans
    elif tmp.count(max(tmp)) == 2:
        ans.pop(tmp.index(min(tmp)))
        return ans
    return [tmp.index(max(tmp))+1]