import re
def solution(baby):
    ans = ["aya", "ma", "woo", "ye"]
    for i in range(len(ans)):
        for j in range(len(baby)):
            if ans[0] in baby[j]:
                if ans[0] * 2 in baby[j]:
                    continue
                else:
                    baby[j] = re.sub(ans[0], "1", baby[j])
        ans.pop(0)
    return sum([1 for i in range(len(baby)) if set(baby[i]) == {'1'}])