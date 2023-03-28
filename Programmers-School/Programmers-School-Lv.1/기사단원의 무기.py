def p_cnt(n):
    if n == 1:
        return 1
    p_tot = 0
    for i in range(1, int(n ** 0.5)+1): 
        if n % i == 0:
            p_tot += 1
    if n ** 0.5 == n // n ** 0.5:
        return p_tot * 2 - 1
    else:
        return p_tot * 2
def solution(number, limit, power):
    tmp = [p_cnt(i) for i in range(1, number+1)]
    for i in range(len(tmp)):
        if tmp[i] > limit:
            tmp[i] = power
    return sum(tmp)