# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        ret = []

        queue = [root]
        while queue:
            update = []
            tmp = []
            for node in queue:
                tmp.append(node.val)
                if node.left:
                    update.append(node.left)
                if node.right:
                    update.append(node.right)
            ret.append(tmp)
            queue = update
        return ret