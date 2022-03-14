/*
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        height, isBalance = self.helper(root)
        return isBalance
        
    def helper(self, root):
        isbalance = False
        #exit
        if not root:
            return 0, True
        
        #divide
        lheight, lBalance = self.helper(root.left)
        rheight, rBalance = self.helper(root.right)
        
        #conquer
        if lBalance and rBalance and abs(lheight - rheight) <= 1:
            return max(lheight, rheight) + 1, True
        else:
            return max(lheight, rheight) + 1, False
        


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

//version 1:divide
class Solution {
    public boolean isBalanced(TreeNode root) {
        
        if (root == null) {
            return true;
        }
        
        return Math.abs(height(root.left) - height(root.right)) < 2 
            && isBalanced(root.left) 
            && isBalanced(root.right);
    }
    
    private int height(TreeNode root){
        if (root == null) {
            return 0;
        }
        
        return Math.max(height(root.left), height(root.right)) + 1;
    }
}
