def solution(id_list, report, k):
    #k번 이상 신고 정지
    dic, rp_dic = {}, {}
    for i in id_list:
        dic[i] = [] #유저가 신고한 아이디
        rp_dic[i] = 0 #신고당한 유저 카운터용
    report = list(set(report))
    for i in report: #각 유저가 신고한 유저
        dic[i.split()[0]].append(i.split()[1])
    for i in dic: 
        for j in range(len(dic[i])):
            rp_dic[dic[i][j]] += 1 #각 유저가 신고당한 횟수
    kill_id = []
    for i in rp_dic:
        if rp_dic[i] >= k:
            kill_id.append(i) #정지 대상 아이디
    print(kill_id)
    s_mail = []
    for i in dic:
        cnt = 0
        for j in kill_id:
            if j in dic[i]:
                cnt += 1
        s_mail.append(cnt)
    return s_mail