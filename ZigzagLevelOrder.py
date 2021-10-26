'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # check for input
        if not root:
            return []
        # initialize 2 stacks, s1 for the odd levels, s2 for the event levels
        s1 = [root]
        s2 = []
        # initialize empty list for the values
        level = []
        # initalize result as the final output list holding the sublist if any
        result = []

        # run while node exists
        while s1 or s2:
            while s1:
                # remove the current first element from s1 and store it in variable
                root = s1.pop()
                # now we add the second/even level to the second stack after checking for input
                level.append(root.val)
                if root.left:
                    s2.append(root.left)
                if root.right:
                    s2.append(root.right)
            # add onto the result the values we currently have in our level...
            # and then clear it out in prep for the next (odd) level
            result.append(level)
            level = []
            while s2:
                root = s2.pop()
                level.append(root.val)
                # NOTE: make sure we check input/append from right to left now since we did left to right above
                if root.right:
                    s1.append(root.right)
                if root.left:
                    s1.append(root.left)
            # check for input in case we appended empty sublist
            if level != []:
                result.append(level)
            level = []
        
        return result

# Time: O(n) since we're only visiting every single node a single time
# Space: O(n) with n being all the nodes in the tree