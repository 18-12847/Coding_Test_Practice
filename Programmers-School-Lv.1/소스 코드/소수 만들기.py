def solution(nums):
    tmp = [False, False] + [True] * (2999)
    for i in range(2, int(3000 ** 0.5) + 1):
        if tmp[i]:
            for j in range(i * 2, 3001, i):
                tmp[j] = False
    ans = []
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                ans.append(nums[i] + nums[j] + nums[k])
    cnt = 0
    for i in ans:
        if tmp[i] == True:
            cnt += 1
    return cnt            