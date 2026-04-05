# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        can u a level order traversal using bfs and a queue. We keep track of the max
        before each level and count the number of nodes greater while updating the
        max for each node individually
        """

        res = 0
        q = deque([(root, -101)])

        while q:
            node, max_val = q.popleft()
            if node.val >= max_val:
                res += 1
                max_val = node.val
            
            if node.left:
                q.append((node.left, max_val))
            if node.right:
                q.append((node.right, max_val))
        
        return res