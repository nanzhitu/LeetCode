#encoding=utf-8
import sys
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    Sum = 0
    symbol = 1
    if x < 0:
        symbol = -1
    temp = x * symbol
    if temp > sys.maxint:
        return 0
    while temp != 0:
        Sum = Sum * 10 + temp % 10
        temp = temp / 10
    if Sum > sys.maxint:
        return 0
    else:
        return Sum*symbol

maxinit = 2147483647

a = 2147483647
print reverse(a)
