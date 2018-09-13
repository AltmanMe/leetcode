def twoSum(nums, target):
    for idx, num in enumerate(nums):
        r = target - num
        if r in nums:
            if nums.index(r) != idx:
                return [idx, nums.index(r)]

"""
构造字典
dic = dict()
for idx, num in enumerate(nums):
    dic[num] = idx
字典中会自动覆盖重复的 key-value 

如果使用 bruteforce 解法，时间复杂度为 O(n2) TimeLimited Error
"""
