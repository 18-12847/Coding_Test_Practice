import math
def solution(n):
    return (int(math.sqrt(n))+1) ** 2 if math.ceil(math.sqrt(n)) ** 2 == float(n) else -1