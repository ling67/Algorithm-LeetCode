"""
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

 

Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

Constraints:

The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1
 

Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?
"""

"""
solution 1: do an in order traversal turn it into a list, and then find the swapped elements.
It's not modify in place, we need to modify in-place. 
Think about how do we modify an sorted arr problem in place. 
Similar with the previous mode problem, we need to use a global prev_node, so that we can compare the adjacent nodes in the sorted arr.
"""
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.wrong_node_1 = None
        self.wrong_node_2 = None
        self.prev_node = None
        self.in_order(root)
        self.wrong_node_1.val, self.wrong_node_2.val = self.wrong_node_2.val, self.wrong_node_1.val

    def in_order(self, root):
        if root.left:
            self.in_order(root.left)
        
        if self.prev_node and root.val < self.prev_node.val:
            if not self.wrong_node_1:
                self.wrong_node_1 = self.prev_node
                self.wrong_node_2 = root    # 这里要赋值second_swapped是因为可能就是相邻的两个nodes交换了
            else:
                self.wrong_node_2 = root
                
        self.prev_node = root               # 注意要改变prev_node
            
        if root.right:
            self.in_order(root.right)
