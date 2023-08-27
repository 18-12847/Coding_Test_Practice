import sys
input = sys.stdin.readline
lst, inp, cnt, ans = [], [], 0, 0
for _ in range(5):
    lst.extend(list(map(int, input().split())))
for _ in range(5):
    inp.extend(list(map(int, input().split())))
flag = [True] * 12
for i in inp:
    lst[lst.index(i)] = 0
    if sum(lst[:5]) == 0 and flag[0]:
        cnt += 1
        flag[0] = False
    if sum(lst[5:10]) == 0 and flag[1]:
        cnt += 1
        flag[1] = False
    if sum(lst[10:15]) == 0 and flag[2]:
        cnt += 1
        flag[2] = False
    if sum(lst[15:20]) == 0 and flag[3]:
        cnt += 1
        flag[3] = False
    if sum(lst[20:25]) == 0 and flag[4]:
        cnt += 1
        flag[4] = False
    if lst[0] + lst[6] + lst[12] + lst[18] + lst[24] == 0 and flag[5]:
        cnt += 1
        flag[5] = False
    if lst[4] + lst[8] + lst[12] + lst[16] + lst[20] == 0 and flag[6]:
        cnt += 1
        flag[6] = False
    if lst[0] + lst[5] + lst[10] + lst[15] + lst[20] == 0 and flag[7]:
        cnt += 1
        flag[7] = False
    if lst[1] + lst[6] + lst[11] + lst[16] + lst[21] == 0 and flag[8]:
        cnt += 1
        flag[8] = False
    if lst[2] + lst[7] + lst[12] + lst[17] + lst[22] == 0 and flag[9]:
        cnt += 1
        flag[9] = False
    if lst[3] + lst[8] + lst[13] + lst[18] + lst[23] == 0 and flag[10]:
        cnt += 1
        flag[10] = False
    if lst[4] + lst[9] + lst[14] + lst[19] + lst[24] == 0 and flag[11]:
        cnt += 1
        flag[11] = False
    ans += 1
    if cnt >= 3:
        print(ans)
        break