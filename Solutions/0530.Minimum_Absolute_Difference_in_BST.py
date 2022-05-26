"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        in_order = self.in_order(root)
        min_diff = float("inf")
        for i in range(1, len(in_order)):
            min_diff = min(min_diff, abs(in_order[i] - in_order[i-1]))
        return min_diff
        
    def in_order(self, root):
        if not root:
            return[]
        
        res = []
        res += self.in_order(root.left)
        res.append(root.val)
        res += self.in_order(root.right)
        
        return res
        
