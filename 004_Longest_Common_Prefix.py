

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    restr = ""
    if(len(strs) == 0):
        return restr
    diff = True
    for i in range(len(strs[0])):
        str_0 = strs[0][i]
        for str_other in strs[1:]:
            if len(str_other) <= i or str_other[i] != str_0:
                diff = False
        if diff == True:
            restr = restr + str_0
        else:
            break    
    return restr
    
str=["aaaa","aaaaa","a"]

print longestCommonPrefix(str)
