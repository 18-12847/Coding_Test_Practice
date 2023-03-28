def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        arr1[i] = bin(arr1[i] | arr2[i])
    for i in range(n):
        tmp = []
        if len(arr1[i])-2 < n:
            for _ in range(n-(len(arr1[i])-2)):
                tmp.append(" ")
        for j in range(2, len(arr1[i])):
            if arr1[i][j] == "1":
                tmp.append("#")
            elif arr1[i][j] == "0":
                tmp.append(" ")
        ans.append("".join(tmp))
    return ans