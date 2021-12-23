/*
描述
给一棵二叉树, 找到和为最小的子树, 返回其根节点。
输入输出数据范围都在int内。

LintCode会打印根节点为你返回节点的子树。保证只有一棵和最小的子树并且给出的二叉树不是一棵空树。

样例
样例 1:

输入:
{1,-5,2,1,2,-4,-5}
输出:1
说明
这棵树如下所示：
     1
   /   \
 -5     2
 / \   /  \
1   2 -4  -5 
整颗树的和是最小的，所以返回根节点1.
样例 2:

输入:
{1}
输出:1
说明:
这棵树如下所示：
   1
这棵树只有整体这一个子树，所以返回1.
*/


/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */

public class Solution {
    /**
     * @param root: the root of binary tree
     * @return: the root of the minimum subtree
     */

    private int minSum;
    private TreeNode minRoot;

    public TreeNode findSubtree(TreeNode root) {
        // write your code here
        minSum = Integer.MAX_VALUE;
        minRoot = null;
        getSum(root);
        return minRoot;        
    }

    //返回子数的和
    private int getSum(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int sum = getSum(root.left) + getSum(root.right) + root.val;
        if (sum < minSum) {
            minSum = sum;
            minRoot = root;
        }
        return sum;
    }

}
