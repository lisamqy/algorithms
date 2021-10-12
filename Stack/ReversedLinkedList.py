'''Given the head of a singly linked list, reverse the list, and return the reversed list.'''

class Solution:
    def reverseLList(self, head):
        # set a prev for reference
        prev = None
        current = head
        # while current exists; not None
        while current:
            next = current.next # store current's next in variable
            current.next = prev # have current's next point at the prev
            prev = current #update the prev
            current = next #update the current

        return prev


# Time = O(n) Space = O(1)