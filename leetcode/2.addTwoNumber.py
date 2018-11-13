from utilities.ListNode import ListNode

"""
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain 
a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


def addTwoNumbers(n1, n2):
    result = ListNode(0)
    carry = 0
    while(n1.next != None or n2.next != None or carry):
        curValue = n1.val + n2.val
        carry = curValue / 10
        result = curValue % 10


t1 = ListNode(2)
t2 = ListNode(4)
t3 = ListNode(3)
t1.next = t2
t2.next = t3
e1 = ListNode(7)
e2 = ListNode(0)
e3 = ListNode(8)
e1.next = e2
e2.next = e3
addTwoNumbers()
