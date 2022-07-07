/*
Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [5,4,5,1,1,5]
Output: 2
Example 2:


Input: root = [1,4,5,4,4,5]
Output: 2
*/

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.helper(root)) - 1
        
    # r_end, r_pass, r_not 
    def helper(self, root):
        if not root:
            return 0, 0, 0
        
        l_end, l_pass, l_not = self.helper(root.left)
        r_end, r_pass, r_not = self.helper(root.right)
        
        root_end, root_pass, root_not = 1, 0, 0
        
        if root.left:
            if root.left.val == root.val:
                root_end = max(root_end, l_end + 1)
                
        if root.right:        
            if root.right.val == root.val:
                root_end = max(root_end, r_end + 1)
        
        if root.left and root.right:
            if root.left.val == root.right.val == root.val:
                root_pass = l_end + 1 + r_end
        
        root_not = max(l_end, l_pass, l_not, r_end, r_pass, r_not)
        
        return root_end, root_pass, root_not

//python version
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.helper(root)) - 1
    
    """
    return 
    w  end with
    wo without
    p  pass  严格穿过，不能是1，至少是3
    """
    def helper(self, root):
        #exit
        if not root:
            return 0,0,0
        if not root.left and not root.right:
            return 1, 0, 0
        
        #divide 
        l_w, l_wo, l_p = self.helper(root.left)
        r_w, r_wo, r_p = self.helper(root.right)
        
        #conquer
        root_wo = max(l_w, l_wo, l_p, r_w, r_wo, r_p)
        root_w, root_p = 1, 0
        
        if root.left and root.left.val == root.val:   #这里容易忘记做判断
            root_w = max(root_w, l_w + 1)
        if root.right and root.right.val == root.val:  #这里容易忘记做判断
            root_w = max(root_w, r_w + 1)   
            
        if root.left and root.right and (root.left.val == root.right.val == root.val):   #这里容易忘记做判断
            root_p = l_w + r_w + 1
        
        return root_w, root_wo, root_p

/***********************************java version*****************************/
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
        int excludeRootMax;     //不包括root的路径的最大值
        int endRootMax;         //严格以root为终节点的路径最大值
        int passRootMax;        //严格通过root的最大路径值，注意不能root为终节点
        private ResultType(int excludeRootMax, int endRootMax, int passRootMax) {
            this.excludeRootMax = excludeRootMax;
            this.endRootMax = endRootMax;
            this.passRootMax = passRootMax;
        }
    }
    
    public int longestUnivaluePath(TreeNode root) {
        if (root == null) {
            return 0;
        }
        ResultType result = help(root);
        return Math.max(Math.max(result.excludeRootMax, result.endRootMax), result.passRootMax) - 1;
    }
    
    ResultType help(TreeNode root) {
        //exit
        if (root == null) {
            return new ResultType(0, 0, 0);
        }
        
        if (root.left == null && root.right == null) {
            return new ResultType(0, 1, 0);   //注意初始化
        }
        
        ResultType result = new ResultType(0, 1, 0);   //注意初始化
        
        //divide
        ResultType left = help(root.left);
        ResultType right = help(root.right);
        
        //conquer
        if (root.left != null) {
            if (root.left.val == root.val) {
                result.endRootMax = left.endRootMax + 1;
                
            }
            result.excludeRootMax = Math.max(Math.max(left.excludeRootMax, left.endRootMax), left.passRootMax);
        }
        
        if (root.right != null) {
            if (root.right.val == root.val) {
                result.endRootMax = Math.max(result.endRootMax, right.endRootMax + 1);
            }
            result.excludeRootMax = Math.max(result.excludeRootMax, Math.max(Math.max(right.excludeRootMax, right.endRootMax), right.passRootMax));
        }
        
        if (root.left != null && root.right != null) {
            if (root.left.val == root.val && root.val == root.right.val) {
                result.passRootMax = left.endRootMax + right.endRootMax + 1;
            }
        }
        return result;
    }
    
}
