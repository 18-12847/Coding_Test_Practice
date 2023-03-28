def solution(s):
    return True if sorted(s)[-1].isdigit() and (len(s) == 4 or len(s) == 6) else False