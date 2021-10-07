'''You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.'''

'''You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):

        # keep track of final linked list
        # set inital value of what sum of the ones place should be
        # use modulo 10 to grab the leftmost single digit aka strip off ones place
        added = ListNode(val = (l1.val + l2.val) % 10) # NOTE: 6 -> 6 | 10 -> 1 | 12 -> 1
        # keep track of any carry overs
        # use floor division so it only keeps the right most single digit; NOTE: 6 -> 6 | 10 -> 0 | 12 -> 2
        carryover = (l1.val + l2.val) // 10
        # keep track of current node
        current = added

        # while either of these exists...
        while l1.next and l2.next:
            # set as next node
            l1 = l1.next
            l2 = l2.next

            # add the values together to then set the value as the current's next node by creating new node
            current.next = ListNode(val = (carryover + l1.val + l2.val) % 10)
            # update carryover value
            carryover = (carryover + l1.val + l2.val) // 10
            # update current to the new current made above
            current = current.next

        # in case the two lists have diff amounts of nodes
        while l1.next:
            l1 = l1.next
            current.next = ListNode(val = (carryover + l1.val) % 10)
            carryover = (carryover + l1.val) // 10
            current = current.next

        while l2.next:
            l2 = l2.next
            current.next = ListNode(val = (carryover + l2.val) % 10)
            carryover = (carryover + l2.val) // 10
            current = current.next

        # in case there is still a final carryover
        if carryover > 0:
            current.next = ListNode(val = 1)

        # Lastly
        return added
