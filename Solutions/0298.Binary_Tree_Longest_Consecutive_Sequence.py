/*
Given the root of a binary tree, return the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path needs to be from parent to child (cannot be the reverse).

 

Example 1:


Input: root = [1,null,3,2,4,null,null,null,5]
Output: 3
Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:


Input: root = [2,null,3,2,null,1]
Output: 2
Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-3 * 104 <= Node.val <= 3 * 104
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        return max(self._helper(root))
    
    def _helper(self, root):
        """
        returns (the LCS ended with root, without root)
        """
        if not root:
            return 0, 0
        if not root.left and not root.right:
            return 1, 0
        
        # divide
        left_w, left_wo = self._helper(root.left)  #w 以root结尾  wo不以root结尾
        right_w, right_wo = self._helper(root.right)
        
        # conquer
        root_wo = max(left_w, left_wo, right_w, right_wo)
        root_w = 1
        if root.left and root.left.val == root.val + 1:
            root_w = max(root_w, 1 + left_w)
        if root.right and root.right.val == root.val + 1:
            root_w = max(root_w, 1 + right_w)
            
        return root_w, root_wo


//version divide
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
//verision 3:divide conquer
class Solution {
    
    private class ResultType {
        int maxInSubtree;    //包括和不包括root的最大值
        int maxFromRoot;    //包括root的最大值
        public ResultType(int maxInSubtree, int maxFromRoot) {
            this.maxInSubtree = maxInSubtree;
            this.maxFromRoot = maxFromRoot;
        } 
    }
            
    //1.return the longest consecutive sequence path of binary tree root
    public int longestConsecutive(TreeNode root) {
        return help(root).maxInSubtree;        
    }
    
    //1.return the longest consecutive sequence path of binary tree root
    private ResultType help(TreeNode root){
        
        //3.exit
        if (root == null) {
            return new ResultType(0, 0);
        }
        
        ResultType result = new ResultType(0, 1);
        
        //2.divide
        ResultType left = help(root.left);
        ResultType right = help(root.right);
        
        //3.conquer
        if(root.left != null && root.val + 1 == root.left.val) {
            result.maxFromRoot = Math.max(
                result.maxFromRoot,
                left.maxFromRoot + 1
            );
        }
        
        if(root.right != null && root.val + 1 == root.right.val) {
            result.maxFromRoot = Math.max(
                result.maxFromRoot,
                right.maxFromRoot + 1
            );
        }
        
        result.maxInSubtree = Math.max(
            result.maxFromRoot,
            Math.max(left.maxInSubtree, right.maxInSubtree)
        );
        
        return result;
    }
}



