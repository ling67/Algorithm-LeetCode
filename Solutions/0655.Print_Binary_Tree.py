/*
Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:

The height of the tree is height and the number of rows m should be equal to height + 1.
The number of columns n should be equal to 2height+1 - 1.
Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
Continue this process until all the nodes in the tree have been placed.
Any empty cells should contain the empty string "".
Return the constructed matrix res.

 

Example 1:


Input: root = [1,2]
Output: 
[["","1",""],
 ["2","",""]]
Example 2:


Input: root = [1,2,3,null,4]
Output: 
[["","","","1","","",""],
 ["","2","","","","3",""],
 ["","","4","","","",""]]
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def helper(root, depth, pos):
            res[-(depth + 1)][pos] = str(root.val)
            if root.left:
                helper(root.left, depth - 1, pos - 2**(depth - 1))
            if root.right:
                helper(root.right, depth - 1, pos + 2**(depth - 1))
        
        depth = self._find_depth(root)
        m, n = depth, 2 ** depth - 1
        res = [["" for _ in range(n)] for _ in range(m)]
        
        helper(root, depth - 1, 2 ** (depth - 1) - 1)
        return res
    
    def _find_depth(self, root):
        if not root:
            return 0
        return 1 + max(self._find_depth(root.left), self._find_depth(root.right))



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
    public List<List<String>> printTree(TreeNode root) {
        int height = getHeight(root);
        int wide = getWide(height);  // 2的h次方减去1
        List<List<String>> result = new ArrayList<>();
        for (int i = 0; i < height; i++) {
            List<String> list = new ArrayList<>();
            for (int j = 0; j < wide; j++) {
                list.add("");
            }
            result.add(list);
        }
        print(result, root, 0, 0, wide - 1);
        return result;
    }
    
    private void print(List<List<String>> result, TreeNode root, int row, int left, int right) {
        if (root == null) return;
        int center = (left + right) / 2;
        result.get(row).set(center, String.valueOf(root.val));
        print(result, root.left, row + 1, left, center - 1);
        print(result, root.right, row + 1, center + 1, right);
    }
    
    private int getHeight(TreeNode root) {
        if (root == null) return 0;
        return Math.max(getHeight(root.left), getHeight(root.right)) + 1;
    }
    
    private int getWide(int height) {
        int wide = 1;
        while (height > 0) {
            wide = wide * 2;
            height--;
        }
        return wide - 1;
    }
    
}
