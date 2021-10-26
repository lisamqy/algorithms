'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).'''

'''
A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution using recursive dfs
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # use a helper function
        def valid(node, left, right):
            # since an empty BST can still be considered a BST
            if not node:
                return True
            # check if current node's val is greater than the left boundary but less than the right
            if not(node.val > left and node.val < right):
                return False
            
            # now onto our recursive call...
            # make sure left subtree of node(s) is valid by passing node.left and 
            # use left as our lower boundary and update our upper boundary to be the parent's val
            # also make sure right subtree is valid by passing node.right and
            # update the parent's val as the left boundary and use right as our upper boundary
            # NOTE: if both these evaluate to True, we know it's been a correct BST so far so we can simply return the result(bool)
            return (valid(node.left, left, node.val) and 
                    valid(node.right, node.val, right))


        # use negative infinity and infinity aka float("-inf")/float("inf") as our initial lower and upper boundaries since the root can be anything
        return valid(root, float("-inf"), float("inf"))


# Time and space: O(n) since worst case we're checking every node once if it is a valid BST