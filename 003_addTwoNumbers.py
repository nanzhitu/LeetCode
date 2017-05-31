
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def addTwoNumbers( l1, l2):   
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    sign = 0
    Sum = 0
    n = ListNode(0)
    r = n
    while True:
        Sum = 0
        if l1 != None:
            Sum += l1.val
            l1 = l1.next
        if l2 != None:
            Sum += l2.val
            l2 = l2.next
        Sum += sign
        n.next = ListNode(Sum % 10)
        n = n.next
        sign = Sum / 10
        if l1 == None and l2 == None and sign ==0:
            break
    return r.next

l1 = ListNode(4)
i1 = ListNode(5)
i2 = ListNode(8)

l1.next = i1
i1.next = i2

l2 = ListNode(3)
j1 = ListNode(5)
j2 = ListNode(1)

l2.next = j1
j1.next = j2

l3 = addTwoNumbers(l1, l2)

while l3 != None:
    print l3.val
    l3 = l3.next



