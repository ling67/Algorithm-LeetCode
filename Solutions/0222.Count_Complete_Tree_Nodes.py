"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
"""

#version1: divide and conquer time complexity O(n) do not satisfy question.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
      
#version use the BST feature, use the property of complete Tree - O(logN*logN)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l_height = self.getHeight(root.left)
        r_height = self.getHeight(root.right)
        
        if l_height == r_height:   # left subtree is a perfect binary tree, but right subtree may or may not
            return 2**l_height + self.countNodes(root.right)
        else:                      # right subtree is a perfect binary tree, but left subTree may or may not
            return 2**(r_height) + self.countNodes(root.left)
    
    def getHeight(self, root):
        if not root:
            return 0
        
        return 1 + self.getHeight(root.left) 
