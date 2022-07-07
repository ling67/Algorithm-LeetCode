/*
Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

*/

**
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
 
 
// version 1：用递归实现 time complexity is O(N)
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归的出口（结束条件）
        if not root:
            return []
        
        res = []
        res.append(root.val)
        
        # divide
        leftRes = self.preorderTraversal(root.left)     # # 注意不要用append. [1,2]+[3,4]=[1,2,3,4], [1,2].append([3,4])=[[1,2], [3,4]]
        rightRes = self.preorderTraversal(root.right)
        
        # conquer
        res += leftRes
        res += rightRes
        
        return res
       
//version 2:Non-Recursion  用栈

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack = [root]
        res = []
        while stack:
            currNode = stack.pop()
            res.append(currNode.val)
            if currNode.right:
                stack.append(currNode.right)
            if currNode.left:
                stack.append(currNode.left)
        return res
 
 
/**********************************java version**************************************/ 
  
//version 1:Divide & Conquer 
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> result = new LinkedList<>();
        //exit
        if (root == null) {
            return result;
        }
        
        //divide + conquer
        result.add(root.val);
        result.addAll(preorderTraversal(root.left));   //加入链表时用addAll()
        result.addAll(preorderTraversal(root.right));
        return result;
    }
}

//version 2:Travers 
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
    public List<Integer> preorderTraversal(TreeNode root) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        traverse(root, result);
        return result;
    }
    
    //把root为跟的preorder加入result里面
    private void traverse(TreeNode root, ArrayList<Integer> result) {
        if (root == null) {
            return;
        }
        
        result.add(root.val);
        traverse(root.left, result);
        traverse(root.right, result);
    }
}


//version: java stack

class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        List<Integer> preorder = new ArrayList<>();
        
        if (root == null) {
            return preorder;
        }
        stack.push(root);
        while (!stack.empty()) {
            TreeNode node = stack.pop();
            preorder.add(node.val);
            if (node.right != null) {
                stack.push(node.right);
            }
            if (node.left != null) {
                stack.push(node.left);
            }
        }
        return preorder;
    }
}



