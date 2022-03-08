/*
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # 下面是非常typical的BFS解binary tree的模板
        res = []
        q = collections.deque()
        q.append(root)   # 注意进q的永远是node, 而不是node.val，永远永远！
        
        while len(q) > 0:
            size = len(q)   # important, 注意这里定义一个lens而不是在59行里直接用len(q)是因为每次q.popleft()之后q的长度会变!
            level = []   # level 记录每一层的信息
            for _ in range(size):
                # 在这一层要做两件事情：
                # 1. 处理这一层：将该层的所有的node.val依次放入level中
                cur = q.popleft()
                level.append(cur.val)
                # 2. 处理下一层：将该层所有的node的左右子节点依次入队列
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)   
            res.append(level)
        return res


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
    
    public List<List<Integer>> levelOrder(TreeNode root) {
        List result = new ArrayList();
        
        if (root == null) {
            return result;
        }
        
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(root);
        
        while (!queue.isEmpty()) {
            ArrayList<Integer> level = new ArrayList<Integer>();
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode head = queue.poll();
                level.add(head.val);
                if (head.left != null) {
                    queue.offer(head.left);
                }
                if (head.right != null) {
                    queue.offer(head.right);
                }
            }
            result.add(level);
        }
        return result;
    }
}
