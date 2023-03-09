/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func removeNthFromEnd(head *ListNode, n int) *ListNode {
    var start *ListNode = &ListNode{
        Val: 0,
        Next: head,
    };

    first := start;
    second := start;

    for n > 0 {
        second = second.Next;
        n -= 1;
    }

    for second.Next != nil {
        first = first.Next;
        second = second.Next;
    }
    first.Next = first.Next.Next;

    return start.Next;
}