# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        tmp = ListNode()
        tmp.next = head
        ret = tmp

        while tmp.next :
            if tmp.next.val == val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return ret.next