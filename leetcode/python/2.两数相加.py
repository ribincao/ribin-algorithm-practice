# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        start = head
        c = 0
        while c or l1 or l2:
            if l1:
                c += l1.val
                l1 = l1.next
            if l2:
                c += l2.val
                l2 = l2.next
            
            val, c = c % 10, c // 10
            start.next = ListNode(val)
            
            start = start.next
        
        return head.next