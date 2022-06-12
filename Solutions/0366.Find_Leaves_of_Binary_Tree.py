"""
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.
 

Example 1:


Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
Example 2:

Input: root = [1]
Output: [[1]]
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root):
            if not root:
                return -1
            left_level = dfs(root.left)
            right_level = dfs(root.right)
            root_level = max(left_level, right_level) + 1
            res[root_level].append(root.val)
            return root_level
        
        res = collections.defaultdict(list)   #if the helper function is internal function, we can directly use res, otherwise, we need use self.res
        dfs(root)
        return res.values()   #always forget, derectly return array.
