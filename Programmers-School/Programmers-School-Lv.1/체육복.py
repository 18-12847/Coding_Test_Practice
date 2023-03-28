def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                reserve[j] = 0
                lost[i] = 0
    t_lost = [lost[i] for i in range(len(lost)) if lost[i] != 0]
    t_reserve = [reserve[i] for i in range(len(reserve)) if reserve[i] != 0]
    l_cnt = 0
    for i in t_lost:
        if i == 1 and i + 1 in t_reserve:
            l_cnt += 1
            t_reserve[t_reserve.index(i+1)] = 0
        elif i > 1 and i - 1 in t_reserve:
            l_cnt += 1
            t_reserve[t_reserve.index(i-1)] = 0
        elif i + 1 in t_reserve:
            l_cnt += 1
            t_reserve[t_reserve.index(i+1)] = 0
    return n - (len(t_lost) - l_cnt)