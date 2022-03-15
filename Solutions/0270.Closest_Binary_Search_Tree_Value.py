/*
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

 

Example 1:


Input: root = [4,2,5,1,3], target = 3.714286
Output: 4
Example 2:

Input: root = [1], target = 4.428571
Output: 1
*/

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
 
"""
recursion版本
"""
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.closest = root.val
        self.helper(root, target)
        return self.closest
    
    def helper(self, root, target):
        if not root:
            return
        
        if abs(root.val - target) < abs(self.closest - target): #打擂台
            self.closest = root.val
        if target < root.val:
            self.helper(root.left, target)
        else:
            self.helper(root.right, target)
        

//non-recurtion
class Solution {
    public int closestValue(TreeNode root, double target) {
        int closest = root.val;
        
        while (root != null) {
            if (Math.abs(closest - target) > Math.abs(root.val - target)) {
                closest = root.val;
            }
            
            if (root.val == target) {
                return root.val;
            } else if (root.val > target) {
                root = root.left;
            } else {
                root = root.right;
            }
        }
        return closest;
    }
}

//recurtion
class Solution {
    
    private int closest;
    
    public int closestValue(TreeNode root, double target) {
        closest = root.val;
        help(root, target);        
        return closest;
    }
    
    private void help(TreeNode root, double target) {
        
        if (root == null) {
            return;
        }
        
        if (Math.abs(root.val - target) < Math.abs(closest - target)) {
            closest = root.val;
        }
        if (target < root.val) {
            help(root.left, target);
        }
        if (target > root.val) {
            help(root.right, target);
        }
    }
}
