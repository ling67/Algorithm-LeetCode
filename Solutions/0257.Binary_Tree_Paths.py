/*
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 

Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
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

// version backtrack
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    
        def backtrack(curr_node, curr_comb):
            if not curr_node.left and not curr_node.right:
                res.append("".join(curr_comb))   

            for next_node in [curr_node.left, curr_node.right]:
                if next_node:
                    curr_comb.append("->" + str(next_node.val))    #讲路径上的所有节点保存在comb中
                    backtrack(next_node, curr_comb)
                    curr_comb.pop()
        
        if not root:
            return []
        res = []
        backtrack(root, [str(root.val)])
        return res
                
        

//version 2:divide

//return all root-to-leaf paths
class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        
        List<String> paths = new ArrayList<>();
        
        //3.exit
        if (root == null) {
            return paths;
        }
        
        //leaf
        if (root.left == null && root.right == null) {
            paths.add(root.val + "");
            return paths;
        }
        
        //2.slipt
        List<String> left = binaryTreePaths(root.left);
        List<String> right = binaryTreePaths(root.right);
        
        for(String path : left) {
            paths.add(root.val + "->" + path);
        }
        
        for(String path : right) {
            paths.add(root.val + "->" + path);
        }
        
        return paths;
    }
}
