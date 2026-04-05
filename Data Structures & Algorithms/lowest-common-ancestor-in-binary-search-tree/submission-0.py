# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        This is a binary search tree so all the values are arranged in an order:
        left < root < right

        So all we need to do is check whether both p and q are less than root, if yes
        means they are in the left sub tree and if both are greater then p and q are in 
        the right sub tree. if both p and q are not greater or lesser than root, means
        we are at the LCA as they must be in different subtrees or we have hit either
        p or q first meaning the other comes lower down
        """

        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root