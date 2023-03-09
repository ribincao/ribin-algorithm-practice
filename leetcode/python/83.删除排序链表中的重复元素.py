# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        start = head
        while start.next:
            if start.val == start.next.val:
                start.next = start.next.next
            else:
                start = start.next
        
        return head