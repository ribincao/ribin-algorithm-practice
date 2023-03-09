/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func deleteDuplicates(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head;
    }

    start := head;
    for start.Next != nil {
        if start.Val == start.Next.Val {
            start.Next = start.Next.Next;
        } else {
            start = start.Next;
        }
    }
    return head;
}