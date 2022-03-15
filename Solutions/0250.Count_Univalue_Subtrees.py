/*
Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

 

Example 1:


Input: root = [5,1,5,5,5,null,5]
Output: 4
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [5,5,5,5,5,null,5]
Output: 6
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        self.helper(root)
        return self.cnt
        
    #check is root is a uni-value subtrees
    def helper(self, root):
        if not root:
            return True
        
        #divide
        left_is = self.helper(root.left)
        right_is = self.helper(root.right)
        
        #conquer
        if (not left_is) or (not right_is) or (root.left and root.left.val != root.val) or (root.right and root.right.val != root.val):
            return False
        
        self.cnt += 1
        return True
        
        

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
    
    private int count = 0;   //记录uni-value subtree个数
    
    public int countUnivalSubtrees(TreeNode root) {
        if (root == null) return 0;
        isUniValueSubtree(root);
        return count;
    }
    
    //判断这个树是不是uni-value subtree
    private boolean isUniValueSubtree(TreeNode root) {
        //exit
        if (root == null) {
            return true;
        }
        if (root.left == null && root.right == null) {
            count++;
            return true;
        } 
        
        //divide        
        boolean leftIs = isUniValueSubtree(root.left);
        boolean rightIs = isUniValueSubtree(root.right);
        boolean rootIs = false;
        
        //如果左边为空，就判断root和右边的值是否相等
        if (root.left == null) {
            if (root.right.val == root.val) {
                rootIs = true;
            }
        //如果右边为空，就判断root和左边的值是否相等 
        } else if (root.right == null) {
            if (root.left.val == root.val) {
                rootIs = true;
            }
        } else {
            if (root.left.val == root.val && root.right.val == root.val) {
                rootIs = true;
            }
        }
        
        boolean result = leftIs && rightIs && rootIs;
        if (result) {
            count++;
        }
        return result;
    }
}
