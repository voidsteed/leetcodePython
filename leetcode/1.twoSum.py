"""
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def twoSum(nums, target):
    result = []
    hashTable = {}

    for i in range(0, len(nums)):
        rest = target - nums[i]
        if rest in hashTable:
            result.append([hashTable[rest], i])
        hashTable[nums[i]] = i
    return result


print(twoSum([2, 7, 11, 15], 9))
