"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        pos_dict = defaultdict(list)
        q = deque()
        q.append((root, 0))
        
        while len(q) > 0:
            curr_node, curr_pos = q.popleft()
            pos_dict[curr_pos].append(curr_node.val)
            if curr_node.left:
                q.append((curr_node.left, curr_pos - 1))
            if curr_node.right:
                q.append((curr_node.right, curr_pos + 1))
                
        min_pos, max_pos = min(pos_dict.keys()), max(pos_dict.keys())
        res = [[] for _ in range(max_pos - min_pos + 1)]
        for pos, lst in pos_dict.items():
            res[pos - min_pos] = lst
        return res

