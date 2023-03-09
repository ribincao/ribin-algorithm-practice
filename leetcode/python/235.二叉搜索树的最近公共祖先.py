# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a, b, c = root.val, p.val, q.val

        if a > b and a > c:
            return self.lowestCommonAncestor(root.left, p, q)
        if a < b and a < c:
            return self.lowestCommonAncestor(root.right, p, q)
        return root