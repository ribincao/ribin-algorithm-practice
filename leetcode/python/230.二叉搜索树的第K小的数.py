# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ret = []
        def middle(node):
            if not node:
                return
            middle(node.left)
            ret.append(node.val)
            middle(node.right)
        middle(root)
        return ret[k - 1]