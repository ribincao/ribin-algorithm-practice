# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ret = []
        while head:
            ret.append(head.val)
            head = head.next
        i, j = 0, len(ret) - 1
        while i < j:
            if ret[i] == ret[j]:
                i += 1
                j -= 1
            else:
                return False
        return True