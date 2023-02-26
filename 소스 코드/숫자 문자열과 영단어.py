def solution(s):
    ans = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8 , "nine" : 9}
    tmp, tmp1 = [], []
    for i in range(len(s)):
        if s[i].isalpha():
            tmp.append(s[i])
            if "".join(tmp) in ans:
                tmp1.append("".join(tmp))
                tmp = []
        else:
            tmp1.append(s[i])
    for i in range(len(tmp1)):
        if tmp1[i].isdigit():
            tmp.append(str(int(tmp1[i])))
        else:
            tmp.append(str(ans[tmp1[i]]))
    return int("".join(tmp))