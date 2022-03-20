/*
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        #exit
        if not root:
            return None
        
        #divide
        left_tree = self.increasingBST(root.left)
        right_tree = self.increasingBST(root.right)
        
        #conquer
        if not left_tree:
            root.left = None
            root.right = right_tree
            return root
        
        else:
            curr = left_tree
            while curr.right:
                curr = curr.right
            
            curr.right = root
            root.left = None
            root.right = right_tree
            return left_tree
            

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
    public TreeNode increasingBST(TreeNode root) {
        if (root == null) return null; 
        
        //divide
        TreeNode left = increasingBST(root.left);
        TreeNode right = increasingBST(root.right);
        
        //conquer
        root.right = right;
        
        TreeNode tail = left;
        while (tail != null && tail.right != null) {
            tail = tail.right;
        }
        
        if (left == null) {
            return root;
        } else {
            tail.right = root;
            root.left = null;    //注意这里要断开
            return left;
        }
    }   
}
