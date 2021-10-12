'''Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode):
        # initiate fast and slow pointer both starting at head
        fast, slow = head, head
        # while there is a fast and a fast's next...
        while fast and fast.next:
            # check if a cycle exists
            fast = fast.next.next
            slow = slow.next
            # if cycle, store the value they met up at
            if slow == fast:
                break
        # no cycle so return None
        else:
            return None
        
        # now we check for the node where cycle starts
        # set another pointer to start again at the head
        pointer = head
        # move both pointer and fast one node at a time til they match
        while pointer != fast:
            pointer = pointer.next 
            fast = fast.next
        # once out of that while loop, we should have the cycle starter node
        return pointer

    
# Space = O(1)