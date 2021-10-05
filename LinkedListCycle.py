'''Linked List Cycle'''

'''Given head, the head of a linked list, determine if the linked list has a cycle in it.'''
'''Return true if there is a cycle in the linked list. Otherwise, return false.'''

# Definition for singly-linked list.
class ListNode:
        def __init__(self,x):
            self.val = x
            self.next = None

class Solution:
    def hasCycle(self, head: ListNode): #-> bool
        
        # initialize a fast and slow pointer that both start at the head node
        # fast will most twice the pace as the slow pointer 
        # when they meet again, that means there is a cycle
        fast = head
        slow = head

        # while the head is not empty, reassign fast and slow as they traverse through the list
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            # if they meet, its a cycle so return true
            if fast == slow:
                return True
        # else not a cycle so return false
        return False



# Time = O(n) / Space = O(1)
# because we traversed through the linked list using two pointer technique
# even though the fast pointer might traverse through the cycle part of the llist multiple times,
# its still within the magnitude of O(n) time