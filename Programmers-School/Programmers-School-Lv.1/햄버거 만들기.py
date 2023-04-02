def solution(ing):
    stack, cnt = [], 0
    for i in ing:
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                stack.pop()
            cnt += 1    
    return cnt