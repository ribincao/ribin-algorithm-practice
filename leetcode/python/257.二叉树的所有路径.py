# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ret = []
        def dfs(root, tmp):
            if not root.left and not root.right:
                tmp.append(str(root.val))
                ret.append(list(tmp))
                return
            tmp.append(str(root.val))
            if root.left:
                dfs(root.left, list(tmp))
            if root.right:
                dfs(root.right, list(tmp))
        
        dfs(root, [])
        res = []
        for tmp in ret:
            res.append('->'.join(tmp))
        return res
