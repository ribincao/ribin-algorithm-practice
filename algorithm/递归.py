# 二叉树翻转
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        if not root.left and not root.right:
            return root
        
        left = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(left)
        
        return root

# 链表反转
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head