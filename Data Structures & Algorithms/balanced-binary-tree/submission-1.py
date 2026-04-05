# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            if not root:
                return 0, True
            
            check_left = check(root.left)
            check_right = check(root.right)

            balanced = (check_left[1] and check_right[1]) and abs(check_left[0] - check_right[0]) <= 1
            height = max(check_left[0], check_right[0]) + 1

            return height, balanced
        
        return check(root)[1]