/*
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1

*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia = 0
        self.helper(root)
        return self.max_dia - 1
    
    #return max length
    def helper(self, root):
        #exit
        if not root:
            return 0
        
        #divide
        l = self.helper(root.left)
        r = self.helper(root.right)

        #conquer
        self.max_dia = max(self.max_dia, l + r + 1)
        
        return max(l, r) + 1
        


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
    
    private int diameter;  //记录diameter最大值，边数

    public int diameterOfBinaryTree(TreeNode root) {
        if(root == null) return 0;
        diameter = 0;
        getDepth(root);
        return diameter;
    }
    
    //获取树的深度:节点数
    private int getDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        if (root.left == null && root.right == null) {
            return 1;
        }
        int leftDepth = getDepth(root.left);
        int rightDepth = getDepth(root.right);
        diameter = Math.max(diameter, leftDepth + rightDepth);  //
        
        return Math.max(leftDepth, rightDepth) + 1;
    }
}
