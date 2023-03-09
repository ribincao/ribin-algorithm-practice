/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */


 func postorderTraversal(root *TreeNode) []int {
    var ret []int;
    dfs(root, &ret);
    return ret;
}

func dfs(root *TreeNode, ret *[]int) []int {
    if root != nil {
        dfs(root.Left, ret);
        dfs(root.Right, ret);
        *ret = append(*ret, root.Val);
    }
    return *ret;
}
