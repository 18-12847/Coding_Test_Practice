def solution(N, stages):
    stages.sort()
    tmp = [stages.count(i+1) for i in range(N)]
    ans, tot = [], len(stages)
    for i in range(len(tmp)):
        if tmp[i] == 0:
            ans.append(0)
        else:
            ans.append(tmp[i] / tot)
            tot -= tmp[i]
    tmp = []
    for _ in range(len(ans)):
        tmp.append(ans.index(max(ans)) + 1)
        ans[ans.index(max(ans))] = -1
    return tmp