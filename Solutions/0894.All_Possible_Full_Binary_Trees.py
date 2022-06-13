"""
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

 

Example 1:


Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Example 2:

Input: n = 3
Output: [[0,0,0]]
 

Constraints:

1 <= n <= 20
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 != 1:    # only odd number of nodes can form a full binary tree
            return []
        if N == 1:
            return [TreeNode(0)]
        
        res = []
        for i in range(1, N, 2):
            left_roots = self.allPossibleFBT(i)
            right_roots = self.allPossibleFBT(N-i-1)
            for left_node in left_roots:
                for right_node in right_roots:
                    root = TreeNode(0)
                    root.left = left_node
                    root.right = right_node
                    res.append(root)
            
        return res

       
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        def dfs(n):
            if n % 2 != 1:
                return []
            if n in self.memo:
                return self.memo[n]
            
            res = []
            for i in range(1, n, 2):
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(n-1-i):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        res.append(root)
            self.memo[n] = res
            return self.memo[n]
            
        self.memo = collections.defaultdict(list)
        self.memo[1] = [TreeNode(0)]
        return dfs(N)
