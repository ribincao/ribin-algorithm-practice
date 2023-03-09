/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func middleNode(head *ListNode) *ListNode {
	n := 0;
	tmp := head;
	for tmp != nil {
		n += 1;
		tmp = tmp.Next;
	}
	k := n / 2;
	ret := head;
	for k > 0 {
		ret = ret.Next;
		k -= 1;
	}
	return ret;
}