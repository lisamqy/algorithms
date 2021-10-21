'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive solution
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # take care of base case
        if not root:
            return 0
        # recursively call maxDepth function on the current node's left and right children
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Time and space = O(n) with n being the number of levels that exist under the root


# not using recursion but using iterative bfs
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        # track the current level of the tree that we're at
        level = 0
        # and initialize a q starting at the root
        q = deque([root])
        # while traversing through our q, remove every node under
        while q:
            # take snapshot of current q
            for i in range(len(q)):
                # remove all and add their children
                node = q.popleft()
                # (if it has a right or left...add/append their children to our q)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # after doing all the above, we increment the level
            level += 1
        return level

# ...or iterative dfs
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # initialize a stack with a pair of values -> root with a depth of 1
        stack = [[root, 1]]
        # NOTE: if we do have null root node, the while loop with pop it but the if statement wont execute
        # so the result returned at the bottom will remain 0
        result = 0

        # while stack is not empty
        while stack:
            # pop the two values from our stack
            node, depth = stack.pop()
            # if node is non-null
            if node:
                # update our result
                result = max(result, depth)
                # add to our stack the left and right children and increase our current depth; null nodes will be ignored
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return result

