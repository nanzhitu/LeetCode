"""
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
"""

"""
Solution 1
"""

"""
def removeElement_1(nums, val):
    '''
    :type nums: List[int]
    :type val: int
    :rtype: int
    '''
    count = nums.count(val)
    for i in range(count):
        nums.remove(val)
    print nums 
        
    return len(nums)
"""

"""
Solution 2
"""
def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    pos = 0
    for i in nums:
        if(i != val):
            nums[pos] = i
            pos+=1

    return pos


numList = [2,3,1,4,2,3,2,4,7,2,9,2]
#numList = [2,2]
#numList = []
val = 2

print removeElement(numList, val)
