/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 var ret []int;
 func kthSmallest(root *TreeNode, k int) int {
	 ret = nil;
	 middle(root);
	 return ret[k - 1];
 }
 
 func middle(root *TreeNode) {
	 if root != nil {
		 middle(root.Left);
		 ret = append(ret, root.Val);
		 middle(root.Right);
	 }
 }