# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, node):
        if node is None:
            return 0
        left_sum = self.solve(node.left)
        if left_sum < 0:
            left_sum = 0
        right_sum = self.solve(node.right)
        if right_sum < 0:
            right_sum = 0
        self.maxi = max(self.maxi, left_sum + node.val + right_sum)
        return node.val + max(left_sum, right_sum)
    
  

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float("-inf")
        self.solve(root)
        return self.maxi
