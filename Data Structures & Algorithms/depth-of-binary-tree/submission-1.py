# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([])
        height = 0
        queue.append(root)
        while len(queue) != 0:
            level_size = len(queue)
            height += 1
            for i in range(level_size):
                e = queue.popleft()
                if e.left is not None:
                    queue.append(e.left)
                if e.right is not None:
                    queue.append(e.right)
        return height
