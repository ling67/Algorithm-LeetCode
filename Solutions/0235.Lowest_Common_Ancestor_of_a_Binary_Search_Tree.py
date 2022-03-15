/*
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
*/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 
#version1: same with 236
#Time complexity O(N) 
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #exit
        if not root or root == p or root == q:
            return root
        
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
        
#version2: use BFS fature 
#Time complexity O(N) 
 
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #exit
        if not root or root == p or root == q:
            return root
        
        #divide & conquer
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q) 
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q) 
        else:
            return root
               
//version: divide & conquer
class Solution {
    
    //1.definition return LCA
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
        //3.exit
        if (root == null || root == p || root == q) {
            return root;
        }
        
        //2.conquer
        if ((p.val >= root.val) && (q.val >= root.val)) {
            return lowestCommonAncestor(root.right, p, q);
        } else if((p.val < root.val) && (q.val < root.val)) {
            return lowestCommonAncestor(root.left, p, q);
        } else {
            return root;
        }
    }
}




