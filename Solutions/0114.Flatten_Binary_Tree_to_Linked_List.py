/*
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
 

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        if not root.left and not root.right:
            return 
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        if not root.left:
            return root
        
        left_head = root.left
        curr = root.left
        while curr.right:
            curr = curr.right
        curr.right = root.right
        root.left = None
        root.right = left_head

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.helper(root)
        
    def helper(self, root):
        #exit
        if not root:
            return None
        if not root.left:
            root.right = self.helper(root.right)
            return root
        
        #divide
        left_tree = self.helper(root.left)
        right_tree = self.helper(root.right)
        
        left_tail = left_tree
        while left_tail and left_tail.right:
            left_tail = left_tail.right
            
        root.left = None
        root.right = left_tree
        left_tail.right = right_tree
        
        return root
        

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

//1.definition:
class Solution {
    
    public void flatten(TreeNode root) {
        
        help(root);        
    }
    
    //return last root  
    private TreeNode help(TreeNode root){
        
        //3.exit
        if (root == null) {
            return null;
        }
        
        if (root.left == null && root.right == null) {
            return root;
        }
        
        //2.split
        TreeNode leftLastNode = help(root.left);
        TreeNode rightLastNode = help(root.right);
        
        if (leftLastNode == null) {
            return rightLastNode;
        }
        
        if (rightLastNode == null) {
            root.right = root.left;
            root.left = null;
            return leftLastNode;
        }
        
        //conquer
        leftLastNode.right = root.right;
        root.right = root.left;
        root.left = null;
        
        return rightLastNode;
        
    }
}
