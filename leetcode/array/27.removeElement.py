"""
Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5,
with the first five elements of nums
containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
"""


def removeElement(nums, val):
    cur = 0
    for i in range(len(nums)):
        if (nums[i] != val):
            print(str(nums[i]) + " i: "+str(i)+" cur: " + str(cur))
            if(i != cur):
                nums[cur] = nums[i]
            cur += 1
    return (nums, cur)


print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))

# second way remove and decrease array size


def removeElement2(nums, val):
    i = 0
    n = len(nums)
    while(i < n):
        if nums[i] == val:
            nums[i] = nums[n-1]
            n -= 1
        else:
            i += 1
    return nums, n


print(removeElement2([0, 1, 2, 2, 3, 0, 4, 2], 2))
