
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    List = []
    nums.sort()

    """
    zero = []
    posi = []
    nega = []
    for i in nums:
        if i == 0 :
            zero.append(i)
        elif i > 0:
            posi.append(i)
        else:
            nega.append(i)

    nega.reverse()
    print zero, posi,nega
    
    if len(zero) > 2:             #[0,0,0]
        List.append([0,0,0])
        
    for i,tempi in enumerate(posi):      #[a,0,-a]
        if i > 0 and tempi == posi[i - 1]:
            print "111:   " 
            continue
        for j,tempj in enumerate(nega):
            print " " + str(tempi) + " : " + str(tempj)
            if tempi + tempj == 0:
                List.append([tempi,0,tempj])
                break
            if tempi + tempj < 0:
                break
    """
    for i,tempi in enumerate(nums):
        if i > 0 and tempi == nums[i-1]:
            continue
        L = i + 1
        R = len(nums) -1
        while L < R :
            if nums[L] + nums[R] + tempi == 0:
                List.append([tempi,nums[L],nums[R]])
                while L < R and nums[L] == nums[L+1]:
                    L = L + 1
                while L < R and nums[R] == nums[R-1]:
                    R = R - 1
                L = L + 1
                R = R - 1
            elif nums[L] + nums[R] + tempi < 0:
                L = L + 1
            else:
                R = R - 1
    return List

lists = [-1,0,2,-1,3,0,-1,5,-3,0,7,0,-4,1]
#lists = [-1,0,1,2,-1,-4]

print threeSum(lists)
