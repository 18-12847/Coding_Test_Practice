import sys
input = sys.stdin.readline
def rec(cur):
    global ans
    if ans == a:
        return
    if cur > a:
        return
    ans = max(cur, ans)
    for i in range(b):
        rec(cur*10 + lst[i])
        
a, b = map(int, input().split())
lst = sorted(list(map(int, input().split())))[::-1]
ans = 0
rec(0)
print(ans)

# import sys
# from itertools import product
# input = sys.stdin.readline
# a, b = map(int, input().split())
# lst = sorted(list(map(int, input().split())))[::-1]
# for i in range(len(str(a)), -1, -1):
#     for j in product(lst, repeat = i):
#         if a >= int("".join(list(map(str, j)))):
#             print(int("".join(list(map(str, j)))))
#             exit()

# rec(0) - ans: 0
# ├─ rec(1) - ans: 1
# │   ├─ rec(11) - ans: 11
# │   │   ├─ rec(111) - ans: 111
# │   │   ├─ rec(115) - ans: 115
# │   │   └─ rec(117) - ans: 117
# │   ├─ rec(15) - ans: 117
# │   │   ├─ rec(151) - ans: 151
# │   │   ├─ rec(155) - ans: 155
# │   │   └─ rec(157) - ans: 157
# │   └─ rec(17) - ans: 157
# │       ├─ rec(171) - ans: 171
# │       ├─ rec(175) - ans: 175
# │       └─ rec(177) - ans: 177
# ├─ rec(5) - ans: 177
# │   ├─ rec(51) - ans: 177
# │   │   ├─ rec(511) - ans: 511
# │   │   ├─ rec(515) - ans: 515
# │   │   └─ rec(517) - ans: 517
# │   ├─ rec(55) - ans: 517
# │   │   ├─ rec(551) - ans: 551
# │   │   ├─ rec(555) - ans: 555
# │   │   └─ rec(557) - ans: 557
# │   └─ rec(57) - ans: 557
# │       ├─ rec(571) - ans: 571
# │       ├─ rec(575) - ans: 575
# │       └─ rec(577) - ans: 577
# └─ rec(7) - ans: 577
#     ├─ rec(71) - ans: 577
#     │   ├─ rec(711) - ans: 577
#     │   ├─ rec(715) - ans: 577
#     │   └─ rec(717) - ans: 577
#     ├─ rec(75) - ans: 577
#     │   ├─ rec(751) - ans: 577
#     │   ├─ rec(755) - ans: 577
#     │   └─ rec(757) - ans: 577
#     └─ rec(77) - ans: 577
#         ├─ rec(771) - ans: 577
#         ├─ rec(775) - ans: 577
#         └─ rec(777) - ans: 577