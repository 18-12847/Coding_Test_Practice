import re
def solution(today, terms, pri):
    check = int(re.sub(r"[.]","",today))
    d_terms = {}
    for i in terms:
        d_terms[i.split()[0]] = int(i.split()[1])
    day_list, pri_list = [], []
    for i in pri:
        day_list.append(i.split()[0])
        pri_list.append(i.split()[1])
    ans = []
    for i in range(len(day_list)):
        t_year, t_month, t_day = day_list[i].split(".")
        t_year = int(t_year)
        t_month = int(t_month) + d_terms[pri_list[i]]
        t_day = int(t_day) - 1
        if t_day == 0:
            t_month -= 1
            t_day = 28
        if t_month > 12 and t_month % 12 == 0:
            t_year += (t_month // 12) - 1
            t_month = 12
        elif t_month > 12:
            t_year += (t_month // 12)
            t_month %= 12
        elif t_month == 0:
            t_month = 12
            t_year -= 1
        ans.append(str(t_year)+str(t_month).zfill(2)+str(t_day).zfill(2))
    final = []
    for i in range(len(ans)):
        if int(ans[i]) < check:
            final.append(i+1)
    return final