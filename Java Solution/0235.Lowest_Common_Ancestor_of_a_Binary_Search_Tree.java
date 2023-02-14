/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) return null;
        if (p == root || q == root) return root;

        if (p.val < root.val && q.val > root.val) return root;
        if (p.val > root.val && q.val < root.val) return root;

        if(root.val<q.val && root.val<p.val) return lowestCommonAncestor(root.right, p, q);
        if(root.val>q.val && root.val>p.val) return lowestCommonAncestor(root.left, p, q);

        return null;
    }
}
