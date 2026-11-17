# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if root is None:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            nodes_list = []
            for i in range(level_size):
                e = queue.popleft()
                nodes_list.append(e.val)
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)

            result.append(nodes_list)
        
        return result

        