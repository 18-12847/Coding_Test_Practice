def solution(food):
    tmp, ans = [0], ""
    for i in range(1, len(food)):
        tmp.append(food[i] // 2)
    for i in range(len(tmp)):
        ans += str(i) * tmp[i]
    return ans + "0" + ans[::-1]