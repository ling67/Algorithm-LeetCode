"""
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 8
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(start, end):
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]
            
            res = []
            for mid in range(start, end + 1):
                left_tree = helper(start, mid - 1)
                right_tree = helper(mid + 1, end)
                for left in left_tree:
                    for right in right_tree:
                        root = TreeNode(mid)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res
        
        if n == 0:
            return []
        return helper(1, n)

