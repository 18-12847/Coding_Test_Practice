def solution(k, m, score):
    score.sort(reverse=True)
    tot = 0
    for i in range(m-1, len(score) - (len(score) % m), m):
        tot += (score[i] * m)
    return tot