/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    c := 0;
    var head ListNode;
    start := &head;

    for {
        if c == 0 && l1 == nil && l2 == nil {
            break;
        }

        if l1 != nil {
            c += l1.Val;
            l1 = l1.Next;
        }
        if l2 != nil {
            c += l2.Val;
            l2 = l2.Next;
        }

        val := c % 10;
        c = c / 10;

        var tmp ListNode;
        tmp.Val = val;

        start.Next = &tmp;
        start = &tmp;
    }
    return head.Next;
}