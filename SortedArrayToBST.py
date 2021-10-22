'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive solution
# Time: O(n)
# Space: O(log n) with log n being the height of our tree because we know it's going ot be balanced
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        # create a helper function that takes in 2 parameters(left and right)...
        # so it'll tell us what portion of the input nums we're trying to convert into a treenode
        def helper(left, right):
            # set base case; if left ever happens to be greater than right...
            if left > right:
                return None

            # otherwise handle the recursive call
            # use floor/integer division to get the index of the middle number in our list
            mid = (left + right) // 2
            # now store the created treenode of nums at index mid
            root = TreeNode(nums[mid])
            # next we compute the left subtree of root by calling recursively on the left and anything left of mid ->(mid - 1) as our right
            root.left = helper(left, mid - 1)
            # ...right subtree of root by calling recursively on the anything right of mid ->(mid + 1) and right
            root.right = helper(mid + 1, right)

            # return the balanced treenode
            return root

        # now to use on the given list, we just have to set left as the 0th index and right as the last index
        return helper(0, len(nums)-1)