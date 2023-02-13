def solution(price, money, count):
    return abs(money - (price * sum([i for i in range(1, count+1)])))if money - (price * sum([i for i in range(1, count+1)])) < 0 else 0