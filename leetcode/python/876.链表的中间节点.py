# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        tmp = head
        n = 0
        while tmp :
            n += 1
            tmp = tmp.next
        k = n // 2

        ret = head
        while k != 0:
            ret = ret.next
            k -= 1
        return ret