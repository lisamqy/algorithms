'''Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        # initiate a dummy node in case list starts off with dupes
        dummy = ListNode(0, next = head)
        # create a slow pointer so we can keep track of prev node
        # starts off pointing at 0
        slow = dummy
        current = head

        # NOTE: EX: 1>1>1>2>3
        while current:
            # if it has a next and is also a dupe...
            # NOTE: slow=>0>1>1>1>2>3
            if current.next and current.val == current.next.val:
                # ...in the case there are multiple dupes
                while current.next and current.val == current.next.val:
                    # update current to ignore the dupes
                    # NOTE: slow=>0>1>2>3
                    current = current.next
                # update slow's next to skip dupe/current
                # NOTE: slow=>0>2>3 
                slow.next = current.next
            # else if not a dupe, we can just move along our slow
            # NOTE: slow=>2>3
            else:
                slow = slow.next
            # dont forget to update our current--whether or not it was a dupe
            current = current.next

        # return updated list starting after the 0 using .next
        return dummy.next