
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i,num in enumerate(nums):
            if (target - num) in nums[i+1:]:
                return [i, nums[i+1:].index(target -num)+i+1]
                #yield [i, nums[i+1:].index(target -num)+i+1]
    #return [0,0]
    return [0,0]

target = 10
nums = [6, 13, 11, 5,15,3,5,6,2,5,8,1,9,5]

#target = 6
#nums = [3,2,4]
#for i in twoSum(nums, target):
#    print i 

print twoSum(nums, target)
