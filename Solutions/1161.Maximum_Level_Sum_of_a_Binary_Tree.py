/*
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val
        q = collections.deque()
        q.append(root)
        level = 0
        res = 1
        while q:
            level += 1
            size = len(q)
            row_sum = 0
            for _ in range(size):
                cur = q.popleft()
                row_sum += cur.val
                if cur.left:     #这里总是写成root.left
                    q.append(cur.left)    
                if cur.right:
                    q.append(cur.right)
            
            if row_sum > max_sum:
                max_sum = row_sum
                res = level
                
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
    public int maxLevelSum(TreeNode root) {
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        int maxSum = Integer.MIN_VALUE;
        int maxLayer = 1;
        int layer = 1;
        
        while (!queue.isEmpty()) {
            int sum = 0;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode head = queue.poll();
                if (head.left != null) {
                    queue.offer(head.left);
                }
                if (head.right != null) {
                    queue.offer(head.right);
                }
                sum += head.val;
            }
            if (sum > maxSum) {
                maxSum = sum;
                maxLayer = layer;
            }
            maxSum = Math.max(maxSum, sum);
            layer++;
        }    
        return maxLayer;
    }
}
