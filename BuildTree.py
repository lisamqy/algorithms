'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree 
and inorder is the inorder traversal of the same tree, construct and return the binary tree.
'''

# Definition for a binary tree node

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive solution
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case; check for input
        if not preorder or not inorder:
            return None
        
        # otherwise we have to create a treenode that is the root
        # NOTE: preorder list always start with the root node; by locating that number, 
        # ...we can determine the left subtree and right subtree from the inorder list
        root = TreeNode(preorder[0])
        # now we have to find the position of root value in our inorder list
        # by getting the index of that value
        mid = inorder.index(preorder[0])
        # now we build the left and right subtree recursively...
        # use list slicing to only get the left subtree values; 
        # we know it'll be the values following the root up until mid from the perorder list
        # and every value up until the mid from the inorder list(aka everything up until but not including the root value)
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # the right subtree will take the values following mid + 1's index from both the preorder and inorder list
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root

# Time: O(n^2) since recursion and use of .index()