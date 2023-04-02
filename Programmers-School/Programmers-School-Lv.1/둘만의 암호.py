def solution(s, skip, index):
    tmp = "abcdefghijklmnopqrstuvwxyz"
    for i in list(skip):
        tmp = tmp.replace(i,"")
    return "".join([tmp[(tmp.find(i) + index) % len(tmp)] for i in s])