import math
def solution(n, m):
    return [math.gcd(n, m), math.gcd(n, m) * n // math.gcd(n, m) * m // math.gcd(n,m) ]