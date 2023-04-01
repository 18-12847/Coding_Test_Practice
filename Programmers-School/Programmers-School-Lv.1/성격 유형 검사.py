def solution(sur, cho):
    tmp = []
    for i in range(len(sur)):
        if sur[i] == "NA":
            tmp.append("AN")
            if cho[i] > 4:
                cho[i] = 4 - abs(4 - cho[i])
            elif cho[i] < 4:
                cho[i] = 4 + abs(4 - cho[i])
        elif sur[i] == "TR":
            tmp.append("RT")
            if cho[i] > 4:
                cho[i] = 4 - abs(4 - cho[i])
            elif cho[i] < 4:
                cho[i] = 4 + abs(4 - cho[i])
        elif sur[i] == "FC":
            tmp.append("CF")
            if cho[i] > 4:
                cho[i] = 4 - abs(4 - cho[i])
            elif cho[i] < 4:
                cho[i] = 4 + abs(4 - cho[i])
        elif sur[i] == "MJ":
            tmp.append("JM")
            if cho[i] > 4:
                cho[i] = 4 - abs(4 - cho[i])
            elif cho[i] < 4:
                cho[i] = 4 + abs(4 - cho[i])
        else:
            tmp.append(sur[i])
    dic_sur = {"RT":[0,0], "CF":[0,0], "JM":[0,0], "AN":[0,0]}
    dic_cho = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    for i in range(len(tmp)):
        if cho[i] > 4:
            dic_sur[tmp[i]][1] += dic_cho[cho[i]]
        elif cho[i] < 4:
            dic_sur[tmp[i]][0] += dic_cho[cho[i]]
    tmp = ["RT", "CF", "JM", "AN"]
    ans = ""
    for i in tmp:
        if dic_sur[i][0] == dic_sur[i][1]:
            ans += i[0]
        elif dic_sur[i][0] > dic_sur[i][1]:
            ans += i[0]
        elif dic_sur[i][0] < dic_sur[i][1]:
            ans += i[1]
    return ans