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

"""
Time complexity : we visit each node exactly once, thus the time complexity is O(N), where N is the number of nodes.
Space complexity : O(1)
"""

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
          
        
// version backtrack 优化
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def backtrack(curr_node, curr_path):
            if not curr_node.left and not curr_node.right:
                res.append(curr_path)
                return
            
            for next_node in [curr_node.left, curr_node.right]:
                if next_node:
                    backtrack(next_node, curr_path + "->" + str(next_node.val))    #这里为什么没有回退是因为str是不可改变了，多以下次循环时，本质上curr_path是没有变的
        
        res = []
        backtrack(root, str(root.val))
        return res
       

//version 2:divide
"""
return all the binary paths for a tree rooted as root
""" 
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # 3. 递归的出口（结束条件）
        if not root:
            return []
        if not root.left and not root.right:   # 注意这里往往需要判断之后根节点没有左右节点的特殊的情况，养成好习惯，尤其是本题，没有这个判断无法输出正确结果
            return [str(root.val)]
        
        # 1. 递归的拆解之divide：无脑divide 成左右两边
        leftPaths = self.binaryTreePaths(root.left)
        rightPaths = self.binaryTreePaths(root.right)
        
        # 2. 递归的拆解之conquer/merge：这时候要想整棵树在该问题上的结果和左右儿子在该问题上的结果之间的联系是什么，是root.val加上左节点的path，然后root.val加上右节点的path
        rootPaths = []
        for leftPath in leftPaths:
            rootPaths.append(str(root.val) + "->" + leftPath)
        for rightPath in rightPaths:
            rootPaths.append(str(root.val) + "->" + rightPath)
        
        return rootPaths

       
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
