def solution(x, n):
    return [i for i in range(x, x*(n+1),x)] if not(x == 0) else [x] * n