import re
def solution(new_id):
    tmp = new_id.lower()
    tmp = re.sub(r"[^a-z0-9-_.]","",tmp)
    for i in range(len(tmp)+1, 1, -1):
        dot = "." * i
        tmp = tmp.replace(dot,".")
    tmp = list(tmp)
    if tmp[0] == ".":
        tmp.pop(0)
    if len(tmp) > 0 and tmp[-1] == ".":
        tmp.pop()
    if len(tmp) == 0:
        tmp = ["a"]
    if len(tmp) > 15:
        tmp = tmp[:15]
    if tmp[-1] == ".":
        tmp.pop()
    if len(tmp) < 3:
        while len(tmp) != 3:
            tmp.append(tmp[-1])
    return "".join(tmp)