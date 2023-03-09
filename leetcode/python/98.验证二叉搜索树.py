# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: 
            return True
        
        left, right = root.left, root.right
        if not left and not right:
            return True
        if right and self.getMin(root.right) <= root.val:
            return False
        if left and self.getMax(root.left) >= root.val:
            return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)
    
    def getMax(self, root: TreeNode) -> int:
        left, right = root.left, root.right
        if not left and not right:
            return root.val
        if not left:
            return max(root.val, self.getMax(right))
        if not right:
            return max(root.val, self.getMax(left))
        return max(root.val, self.getMax(left), self.getMax(right))

    def getMin(self, root: TreeNode) -> int:
        left, right = root.left, root.right
        if not left and not right:
            return root.val
        if not left:
            return min(root.val, self.getMin(right))
        if not right:
            return min(root.val, self.getMin(left))
        return min(root.val, self.getMin(left), self.getMin(right))