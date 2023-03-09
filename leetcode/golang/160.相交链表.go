/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func getIntersectionNode(headA, headB *ListNode) *ListNode {
    A, B := headA, headB;
    for A != B {
        if A == nil {
            A = headB;
        } else {
            A = A.Next;
        }

        if B == nil {
            B = headA;
        } else {
            B = B.Next;
        }
    }
    return A;
}