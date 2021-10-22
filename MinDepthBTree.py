'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections

# using BFS
class Solution:
    def minDepth(self, root: TreeNode) -> int:

        # check for input
        if not root:
            return 0
        
        # intialize a queue (since it has a faster lookup time compared to a list)
        q = collections.deque()
        # add root node(and it's depth) to q
        q.append((root, 1))

        # while q exists...
        while q:
            # pop out whatever is at the 0th index and store it into node and depth
            node, depth = q.popleft()
            # check whether current node has a left or right child; if not, that should be the min depth
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))


# using DFS and recursion
class Solution:
    def minDepth(self, root: TreeNode) -> int:

        # set base case/check for input
        if not root:
            return 0
        
        # if no child(ren)... NOTE: these 2 lines can be skipped since the last return statement can do the same
        if not root.left and not root.right:
            return 1

        # if either left or right child, call the function recursively on that child and it's child and so forth
        if not root.right and root.left:
            return 1 + self.minDepth(root.left)
        if not root.left and root.right:
            return 1 + self.minDepth(root.right)  

        # if both side has a child, get the minimum of both left and right side depth
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right)) 


        