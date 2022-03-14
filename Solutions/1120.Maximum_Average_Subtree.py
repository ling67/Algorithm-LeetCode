/*
Given the root of a binary tree, return the maximum average value of a subtree of that tree. Answers within 10-5 of the actual answer will be accepted.
A subtree of a tree is any node of that tree plus all its descendants.
The average value of a tree is the sum of its values, divided by the number of nodes.

Example 1:
Input: root = [5,6,1]
Output: 6.00000
Explanation: 
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
So the answer is 6 which is the maximum.
Example 2:

Input: root = [0,null,1]
Output: 1.00000
 

Constraints:
The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 105
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.maxAvg = float("-inf")
        self.helper(root)
        return self.maxAvg
    
    def helper(self, root):
        #exit
        if not root:
            return 0, 0
        
        #divide
        lsum, lnum = self.helper(root.left)
        rsum, rnum = self.helper(root.right)

        #conquer
        rootsum = lsum + rsum + root.val
        rootnum = lnum + rnum + 1
        avg = rootsum / rootnum
        
        if avg > self.maxAvg:
            self.maxAvg = avg
        
        return rootsum, rootnum
        
        

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
class state {
    
    
}

class Solution {
    
    private class ResultType {
        public double sum;
        public int size;
        
        public ResultType (double sum, int size) {
            this.sum = sum;
            this.size = size;
        }
    }
    
    private double maxAverage = Double.MIN_VALUE;
    
    public double maximumAverageSubtree(TreeNode root) {
        
        if (root == null) {
            return 0.00000;
        }
        
        help(root);
        
        return maxAverage;
        
    }
    
    //return Average value
    private ResultType help(TreeNode root) {
        
        if (root == null) {
            return new ResultType(0, 0);
        }
        
        ResultType left = help(root.left);
        ResultType right = help(root.right);
        
        ResultType result = new ResultType(
            left.sum + right.sum + root.val,
            left.size + right.size + 1
        );
        
        if (maxAverage < result.sum / result.size) {
            maxAverage = result.sum / result.size;            
        }
        
        return result;
    }
    
}
