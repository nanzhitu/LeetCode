#encoding=utf-8
import sys
'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
Note:
The input is assumed to be a 32-bit signed integer.
Your function should return 0 when the reversed integer overflows.
'''

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
