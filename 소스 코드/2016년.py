def solution(a, b):
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    ans = [[1, 31], [2, 29], [3, 31], [4, 30], [5, 31], [6, 30], [7, 31], [8, 31], [9, 30], [10, 31], [11, 30], [12, 31]]
    tot = 0
    for i in range(a - 1):
        tot += ans[i][1]
    tot += b
    return day[tot % 7 - 1]