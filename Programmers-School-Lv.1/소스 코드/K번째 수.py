def solution(array, commands):
    ans, tmp = [], []
    for i in range(len(commands)):
        tmp = sorted(array[commands[i][0] - 1 : commands[i][1]])
        ans.append(tmp[commands[i][2] - 1])
    return ans