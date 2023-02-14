/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    private int diameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        if (root == null) return 0;
        getDepth(root);
        return diameter - 1;
    }

    private int getDepth(TreeNode root) {
        if (root == null) return 0;
        int l = getDepth(root.left);
        int r = getDepth(root.right);
        diameter = Math.max(diameter, l + r + 1);
        return Math.max(l, r) + 1;
    }
}
