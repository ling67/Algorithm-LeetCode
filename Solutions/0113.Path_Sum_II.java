/*
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
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

//back-dfs

class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        List<Integer> combination = new ArrayList<Integer>();
        combination.add(root.val);
        help(root, targetSum - root.val, combination, result);
        return result;
    }
    
    private void help(TreeNode root,
                     int target,
                     List<Integer> combination,
                     List<List<Integer>> result) {
        
        if ((root.left == null) && (root.right == null) && (target == 0)) {
            result.add(new ArrayList<Integer>(combination));
            return;
        } 
        
        if (root.left != null) {
            combination.add(root.left.val);
            help(root.left, target - root.left.val, combination, result);
            combination.remove(combination.size() - 1);
        }
        
        if (root.right != null) {
            combination.add(root.right.val);
            help(root.right, target - root.right.val, combination, result); 
            combination.remove(combination.size() - 1);  #注意这个要后退，因为combination的值会改变
        }
    }
}
