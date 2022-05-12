"""
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

 

Example 1:


Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
Example 2:


Input: root = [2,1,1]
Output: [[1]]
Example 3:


Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
 

Constraints:

The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200
"""

"""
将树的字串都序列化之后，存入dict，若value>1说明有same structure
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        def serialize(root):
            if not root:
                return "#"
            
            left_ser = serialize(root.left)
            right_ser = serialize(root.right)
            #root_ser = left_ser + ',' + str(root.val) + ',' + right_ser  #这个顺序一定是root，left，right
            root_ser = str(root.val) + ',' + left_ser + ',' + right_ser  #这个顺序一定是root，left，right
            ser_node[root_ser].append(root)
            return root_ser

        ser_node = collections.defaultdict(list)  #subnode, node
        serialize(root)
        
        return [lst[0] for lst in ser_node.values() if len(lst) > 1]  #value中每个节点的字串一样，所以取一个结点就可以

