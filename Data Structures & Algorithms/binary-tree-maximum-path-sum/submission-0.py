# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        def trav(node):
            if not node:
                return 0

            left_sum = max(trav(node.left), 0)
            right_sum = max(trav(node.right), 0)
            total = node.val + left_sum + right_sum

            self.maxSum = max(self.maxSum, total)

            return node.val + max(left_sum, right_sum)
        
        trav(root)
        return self.maxSum