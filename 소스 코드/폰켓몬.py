def solution(nums):
    tmp = int(len(nums) / 2)
    nums = list(set(nums))
    if len(nums) < tmp:
        return len(nums)
    else:
        return tmp