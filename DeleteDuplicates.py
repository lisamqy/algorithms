'''Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.'''


# Definition for singly-llinked list.
class ListNode:
    def __inite__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        # if head exists, we return head(or if no head we return none by default)
        if head:
            current = head
        # while current has a next...
        while current.next:
            # if current's val is same as the next's val
            if current.val == current.next.val:
                # reassign the next's val to the next next
                current.next = current.next.next
            # if not the same...
            else:
                # reassign current to the next to keep checking the rest of the list
                current = current.next
        return head


# Time = O(n) / Space = O(1)