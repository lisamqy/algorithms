'''You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.'''

'''You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self,l1, l2):
        # initiate a dummy node if we later need to insert into a linked list
        dummy = ListNode()
        # set that as our current pointer
        current = dummy
        carryover = 0

        # iterate through the given lists if any of the above exists
        while l1 or l2 or carryover:
            # if l1 not None-> store digit else set as 0
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            # summed digit
            val = value1 + value2 + carryover
            # in case of number over 9, we have to store the leftmost digit; ex: 15, store 1
            carryover = val // 10
            # in case of number over 9, we have to store the rightmost digit; ex: 15, store 5
            val = val % 10
            current.next = ListNode(val)

            # update current pointers
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


        
            