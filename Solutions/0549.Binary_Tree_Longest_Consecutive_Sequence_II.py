"""
Given the root of a binary tree, return the length of the longest consecutive path in the tree.

A consecutive path is a path where the values of the consecutive nodes in the path differ by one. This path can be either increasing or decreasing.

For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid.
On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

 

Example 1:


Input: root = [1,2,3]
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
Example 2:


Input: root = [2,1,3]
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-3 * 104 <= Node.val <= 3 * 104
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        return max(self.helper(root))
        
    """
    Return the LCS ended with root decreasing/increasing, without root, pass root
    pass root include end up with root and pass root
    left_w represent pass root 
    left_wo represent without root
    return root_w_inc  root_wo_inc root_w_dec root_wo_dec
    w: with
    wo: without
    p: pass
    """
    def helper(self, root):
        if not root:
            return 0,0,0,0
        if not root.left and not root.right:
            return 1,1,0,1
        
        left_w_dec, left_w_inc, left_wo, left_p = self.helper(root.left)
        right_w_dec, right_w_inc, right_wo, right_p = self.helper(root.right)
        
        root_wo = max(left_w_dec, left_w_inc, left_wo, left_p, right_w_dec, right_w_inc, right_wo, right_p)
        
        root_w_inc, root_w_dec = 1, 1
        if root.left and root.left.val == root.val + 1:
            root_w_inc = max(root_w_inc, left_w_inc + 1)
        if root.right and root.right.val == root.val + 1:
            root_w_inc = max(root_w_inc, right_w_inc + 1)
        if root.left and root.left.val == root.val - 1:
            root_w_dec = max(root_w_dec, left_w_dec + 1)
        if root.right and root.right.val == root.val - 1:
            root_w_dec = max(root_w_dec, right_w_dec + 1)
            
        root_p = 1
        if root.left and root.right and root.val == root.left.val - 1 == root.right.val + 1:
            root_p = max(root_p, 1 + left_w_inc + right_w_dec)
        if root.left and root.right and root.val == root.left.val + 1 == root.right.val - 1:
            root_p = max(root_p, 1 + left_w_dec + right_w_inc)
            
        return root_w_dec, root_w_inc, root_wo, root_p
        
    
