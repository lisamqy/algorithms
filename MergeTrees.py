'''
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

'''

# Time and Space: O(n+m) because we have to traverse through the entire tree of each given tree; 
# n being number of nodes in a tree 1 and m being number of nodes in tree 2

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Resursive Solution
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if not root1 and not root2:
            return None
        
        # store the value if current tree has values, otherwise set at 0
        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0
        # create a new node thats going to be the merged root node of both trees
        root = TreeNode(v1 + v2)

        # using recursion, merge and left and right subtrees; 
        # but only if they have a child, otherwise set as none so their value will later be turned to 0 (in like 30 or 31) or none if both root.lefts == None
        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        # lastly, return the new merged binary tree
        return root