"""
Given the root of a binary tree, return the sum of values of its deepest leaves.
 

Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
"""

#DFS 遍历tree：

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.max_layer = 0
        self.helper(root, 0)
        return self.sum
    
    def helper(self, root, last_layer):
        if not root:
            return 
        root_layer = last_layer + 1
        if root_layer == self.max_layer:
            self.sum += root.val
        if root_layer > self.max_layer:
            self.sum = root.val
            self.max_layer = root_layer
            
        if root.left:
            self.helper(root.left, root_layer)
        if root.right:
            self.helper(root.right, root_layer)
            

#BFS 遍历tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        sum_val = 0
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            sum_val = 0
            for _ in range(size):
                curr = q.popleft()
                sum_val += curr.val
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)

        return sum_val
