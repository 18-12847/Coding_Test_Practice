def solution(d):
    tmp, ans = [], []
    tot = 0
    for i in range(1, len(d)):
        if d[i].isdigit():
            tmp.append(d[tot:i])
            tot = i
    tmp.append(d[tot:])
    for i in range(len(tmp)):
        if tmp[i].isdigit():
            tmp[i] += tmp[i+1]
            tmp[i+1] = ""
    tot = 1
    for i in range(len(tmp)):
        if len(tmp[i]) == 0:
            continue
        if len(tmp[i]) == 2:
            tot *= int(tmp[i][0])
            if tmp[i][1] == "S":
                ans.append(tot)
                tot = 1
            elif tmp[i][1] == "D":
                ans.append(tot ** 2)
                tot = 1
            elif tmp[i][1] == "T":
                ans.append(tot ** 3)
                tot = 1
        if len(tmp[i]) == 3:
            if tmp[i][-1:] == "#":
                tot *= int(tmp[i][0])
                if tmp[i][1] == "S":
                    ans.append(-tot)
                    tot = 1
                elif tmp[i][1] == "D":
                    ans.append(-(tot ** 2))
                    tot = 1
                elif tmp[i][1] == "T":
                    ans.append(-(tot ** 3))
                    tot = 1
            elif tmp[i][-1:] == "*":
                tot *= int(tmp[i][0])
                if tmp[i][1] == "S":
                    ans.append(tot * 2)
                    if i > 0:
                        ans[i-1] *= 2
                    tot = 1
                elif tmp[i][1] == "D":
                    ans.append((tot ** 2) * 2)
                    if i > 0:
                        ans[i-1] *= 2
                    tot = 1
                elif tmp[i][1] == "T":
                    ans.append((tot ** 3) * 2)
                    if i > 0:
                        ans[i-1] *= 2
                    tot = 1
            elif tmp[i][1:2].isdigit():
                tot *= int(tmp[i][0:2])
                if tmp[i][2:3] == "S":
                    ans.append(tot)
                    tot = 1
                elif tmp[i][2:3] == "D":
                    ans.append(tot ** 2)
                    tot = 1
                elif tmp[i][2:3] == "T":
                    ans.append(tot ** 3)
                    tot = 1
        if len(tmp[i]) == 4:
            tot *= int(tmp[i][0:2])
            if tmp[i][-1:] == "#":
                if tmp[i][2:3] == "S":
                    ans.append(-tot)
                    tot = 1
                elif tmp[i][2:3] == "D":
                    ans.append(-(tot ** 2))
                    tot = 1
                elif tmp[i][2:3] == "T":
                    ans.append(-(tot ** 3))
                    tot = 1
            elif tmp[i][-1:] == "*":
                if tmp[i][2:3] == "S":
                    ans.append(tot * 2)
                    if i > 0:
                        ans[i-1] *= 2
                    tot = 1
                elif tmp[i][2:3] == "D":
                    ans.append((tot ** 2) * 2)
                    if i > 0:
                        ans[i-1] *= 2
                    tot = 1
                elif tmp[i][2:3] == "T":
                    ans.append((tot ** 3) * 2)
                    if i > 0:
                        ans[i-1] *= 2
                    tot = 1
    return sum(ans)