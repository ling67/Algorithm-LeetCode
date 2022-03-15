/*
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

 

Example 1:


Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
Example 2:


Input: root = [1,null,2,null,0,3]
Output: 3
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max_diff = float("-inf")
        self.helper(root)
        return self.max_diff
        
    #return max, min
    def helper(self, root):
        
        #exit
        if not root.left and not root.right:
            return root.val, root.val
        
        root_min, root_max = root.val, root.val
        
        #divide
        if root.left:
            left_min,left_max = self.helper(root.left)
            root_min = min(root_min, left_min)
            root_max = max(root_max, left_max)
        if root.right:
            right_min,right_max = self.helper(root.right)
            root_min = min(root_min, right_min)
            root_max = max(root_max, right_max)
        #conquer
        
        self.max_diff = max(self.max_diff, abs(root.val - root_max), abs(root.val - root_min))
        
        return root_min, root_max
        
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
    
    class ResultType {
        private int min;
        private int max;
        
        private ResultType() {
        }
        
        private ResultType(int min, int max) {
            this.min = min;
            this.max = max;
        }
    }
    
    public int maxDiff = 0;
    
    public int maxAncestorDiff(TreeNode root) {
        //exit
        if (root == null) {
            return 0;
        }
        getMaxAndMin(root);
        return maxDiff;
    }
    
    private ResultType getMaxAndMin(TreeNode root) {
        ResultType result = new ResultType(Integer.MAX_VALUE, Integer.MIN_VALUE);
        //exit
        if (root.left == null && root.right == null) {
            return new ResultType(root.val, root.val);
        }
        
        //divide & conquer
        if (root.left != null) {
            ResultType left = getMaxAndMin(root.left);
            maxDiff = Math.max(maxDiff, Math.max(Math.abs(left.min - root.val), Math.abs(left.max - root.val)));
            result.min = Math.min(left.min, root.val);
            result.max = Math.max(left.max, root.val);
        }
        
        if (root.right != null) {
            ResultType right = getMaxAndMin(root.right);
            maxDiff = Math.max(maxDiff, Math.max(Math.abs(right.min - root.val), Math.abs(right.max - root.val)));
            result.min = Math.min(result.min, Math.min(right.min, root.val));
            result.max = Math.max(result.max, Math.max(right.max, root.val));
        }
        
        return result;
    }    
}
