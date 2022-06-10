"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

 

Example 1:


Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:


Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.
"""

"""
backtrack 1 更简便
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def backtrack(curr_node, curr_sum):
            if not curr_node.left and not curr_node.right:
                return curr_sum
            
            res = 0
            for next_node in [curr_node.left, curr_node.right]:
                if next_node:
                    res += backtrack(next_node, curr_sum * 10 + next_node.val)   #this point donot need backtrack，int is immutable
            return res
    
        res = backtrack(root, root.val)
        return res

"""
backtrack 2 套模板
"""
      
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def backtrack(curr_node, curr_sum):
            if not curr_node.left and not curr_node.right:
                res.append(curr_sum)
                return
            
            for next_node in [curr_node.left, curr_node.right]:
                if next_node:
                    temp = curr_sum
                    next_sum = curr_sum * 10 + next_node.val
                    backtrack(next_node, next_sum)
                    curr_sum = temp
    
        if not root.left and not root.right:
            return root.val
        res = []
        backtrack(root, root.val)
        return sum(res)
