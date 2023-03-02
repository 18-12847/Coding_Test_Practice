def solution(a, b, n):
    tmp, cnt = 0, 0
    while n > a-1:
        tmp = n // a
        n = n - (a * tmp) + (tmp * b)
        cnt += tmp * b
    return cnt