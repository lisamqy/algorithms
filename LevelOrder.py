'''Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).'''

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution using bfs
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # initialize an array/list for the results
        result = []

        q = collections.deque()
        # initialize the queue with our root node
        q.append(root)

        # run BFS while our queue is not empty
        while q:
            # get length of the q/aka number of values within the queue currently
            q_len = len(q)
            # initialize the sublist for each potential level of nodes
            level = []
            # iterate through the queue one level at a time
            for i in range(q_len):
                # pop nodes from the left since bfs/fifo
                node = q.popleft()
                # double check it's not empty
                if node:
                    level.append(node.val)
                    q.append(node.left) #NOTE: the if statement above will take care of any cases where we might've added a None value
                    q.append(node.right)
            # after we finish that level, add our current level as a sublist into the final result list
            # also double check for input
            if level:
                result.append(level)

        return result


# Time: O(n) since we're only visiting every single node a single time
# Space: O(n) since our queue could have up to n/2 elements since its a binary tree; n/2 becomes just n