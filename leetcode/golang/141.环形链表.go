/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func hasCycle(head *ListNode) bool {
    if head == nil {
        return false;
    }
    slow := head;
    fast := head;

    for fast.Next != nil {
        slow = slow.Next;
        fast = fast.Next.Next;
        if fast == nil {
            return false;
        }
        if fast == slow {
            return true;
        }
    }
    return false
}