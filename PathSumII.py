'''
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive solution
class Solution:
    # helper function will take in such parameters: root node, the sum total value that we're trying to equal from a given root, 
    # the list/path that we're currently traversing , a result list that stores all the paths that match targetSum
    def helper(self, root, sum_total, lst, result):
        # base case -> if current node is leaf node
        if not root.left and not root.right:
            # if the current node's value equal to the sum total, 
            # add to the result list a sublist that is the current lst and the current node's value
            if root.val == sum_total:
                result += [lst + [root.val]]
        # if not leaf node, continue recursing
        if root.left:
            # call the function on the child, the updated sum total, update lst, and current result
            self.helper(root.left, sum_total - root.val, lst + [root.val], result)
        if root.right:
            self.helper(root.right, sum_total - root.val, lst + [root.val], result)

        return result

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # check for input
        if not root:
            return []
        # use a helper function will take in such parameters: root, total sum that we want at each level, 
        # a list that'll store all the paths we see, a result list that contains the paths that equal to our targetSum
        return self.helper(root, targetSum, [], [])

    
# Time and Space: O(n)