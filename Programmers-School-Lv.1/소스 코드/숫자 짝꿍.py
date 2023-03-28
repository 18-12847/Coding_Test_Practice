def solution(X, Y):
    a, b, ans = [0] * 10, [0] * 10, [0] * 10
    x, y = list(X), list(Y)
    tmp = ""
    for i in x:
        a[int(i)] += 1
    for j in y:
        b[int(j)] += 1
    for k in range(10):
        if a[k] > 0 and b[k] > 0:
            if a[k] > b[k]:
                ans[k] += b[k]
            else:
                ans[k] += a[k]
    if sum(ans) > 0 and sum(ans) == ans[0]:
        return "0"
    for i in range(9, -1, -1):
        if ans[i] > 0:
            tmp += str(i) * ans[i]
    if sum(ans) == 0:
        return "-1"
    return str(tmp)