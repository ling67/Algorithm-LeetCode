/*
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[2]
        
    def helper(self, root):
        #exit
        if not root:
            return (-float("inf"), float("inf"), True)
        
        #divide
        leftMax, leftMin, leftValid = self.helper(root.left)
        rightMax, rightMin, rightValid = self.helper(root.right)
        
        #conquer
        rootMax = max(leftMax, rightMax, root.val)
        rootMin = min(leftMin, rightMin, root.val)
        rootIsValid = leftValid and rightValid and (leftMax < root.val < rightMin)

        return (rootMax, rootMin, rootIsValid)
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[2]
        
    def helper(self, root):
        if not root.left and not root.right:
            return root.val, root.val, True
        
        root_min, root_max, root_valid = root.val, root.val, True
        
        if root.left:
            l_min, l_max, l_valid = self.helper(root.left)
            root_min = min(root_min, l_min)
            root_max = max(root_max, l_max)
            if not l_valid or l_max >= root.val:
                root_valid = False
            
        if root.right:
            r_min, r_max, r_valid = self.helper(root.right)
            root_min = min(root_min, r_min)
            root_max = max(root_max, r_max)
            if not r_valid or r_min <= root.val:
                root_valid = False
                
        return root_min, root_max, root_valid
        
        
/**********************************************Java version******************************************/

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
    
    private class ResultType {
        boolean isBST;
        TreeNode minNode;   //注意记录的是最小值好最大值的节点
        TreeNode maxNode;
        
        public ResultType(boolean isBST) {
            this.isBST = isBST;
            this.maxNode = maxNode;
            this.minNode = minNode;
        }
    }
    
    public boolean isValidBST(TreeNode root) {
        ResultType result = help(root);
        return result.isBST;
    }
    
    //return root minValue and maxValue and isSearchTree
    private ResultType help(TreeNode root) {
        
        if (root == null) {
            return new ResultType(true);
        }
        
        //divide
        ResultType left = help(root.left);
        ResultType right = help(root.right);
        
        if (!left.isBST || !right.isBST) {
            return new ResultType(false);
        }
        
        if (left.maxNode != null && left.maxNode.val >= root.val) {
            return new ResultType(false);
        }
        
        if (right.maxNode != null && right.minNode.val <= root.val) {
            return new ResultType(false);
        }
        
        ResultType result = new ResultType(true);
        result.minNode = left.minNode != null ? left.minNode : root;  
        result.maxNode = right.maxNode != null ? right.maxNode : root;
        
        return result;
        
    }
    
}

