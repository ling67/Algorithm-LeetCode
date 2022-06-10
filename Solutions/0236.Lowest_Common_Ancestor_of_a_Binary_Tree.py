/*
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
*/  

 """
 python version: divide & conquer
 Time Complexity: O(N), where N is the number of nodes in the binary tree. 
 In the worst case we might be visiting all the nodes of the binary tree.
 Space Complexity: O(1)
 """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #exit
        if not root:
            return None
        if root == p:
            return p
        if root == q:
            return q
        
        #divide
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        #conquer
        if l and r:
            return root
        if l:
            return l
        if r:
            return r

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    
    //1.return the lowest common ancestor of p and q 
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    
        if (root == null || root == p || root == q) {
            return root;
        }
        
        //2.divide
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        
        //3.conquer
        if (left != null && right != null) {
            return root;
        } 
        if (left != null) {
            return left;
        }
        if (right != null) {
            return right;
        }
        
        return null;
        
    }
}






