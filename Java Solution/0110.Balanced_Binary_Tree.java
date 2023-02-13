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
    public boolean isBalanced(TreeNode root) {
        if (root == null) return true;
        boolean l = isBalanced(root.left);
        boolean r = isBalanced(root.right);
        int lLen = height(root.left);
        int rLen = height(root.right); 
        if (l && r && Math.abs(lLen - rLen) <= 1) {
            return true;
        } else {
            return false;
        }
    }

    private int height(TreeNode root) {
        if (root == null) return 0;
        return Math.max(height(root.left), height(root.right)) + 1;
    } 
}
