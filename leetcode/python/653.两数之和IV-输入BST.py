# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    flag = False
    def findTarget(self, root: TreeNode, k: int) -> bool:
        ret = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if k - node.val in ret:
                self.flag = True
                return
            ret.append(node.val)
            dfs(node.right)
        dfs(root)
        return self.flag