/*
Given the roots of two binary search trees, root1 and root2, return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.
Example 2:


Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false

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

/*
1.hashset
2.traversal
*/
class Solution {
    public boolean twoSumBSTs(TreeNode root1, TreeNode root2, int target) {
        Set<Integer> s = inHashset(root1, target, new HashSet());
        return inCheck(root2, s);
    }
    
    //store the target minus each node in binary tree r
    public Set<Integer> inHashset(TreeNode r, int target, Set<Integer> s) {
        if (r == null) return s;
        inHashset(r.left, target, s);
        s.add(target - r.val);
        inHashset(r.right, target, s);
        return s;
    }
    
    //check each node in root2, exist in hashset s
    private boolean inCheck(TreeNode r, Set<Integer> s) {
        if (r == null) return false;
        return inCheck(r.left, s) || s.contains(r.val) || inCheck(r.right, s);
    }
}
