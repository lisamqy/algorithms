'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive solution
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # check for input
        if not root:
            return False
        # update the sum to equal the difference of given targetSum - current node's value
        targetSum -= root.val
        # check if current node is a leaf node and 
        if not root.left and not root.right:
            # this would return the bool of whether we've gotten our target sum from the difference
            return targetSum == 0
        # otherwise we're call the function recursively on either the left or right child
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

# Time: O(n)