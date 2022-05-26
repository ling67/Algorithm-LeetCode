"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
"""

# this is definetely a hard problem
# https://leetcode.com/problems/delete-node-in-a-bst/solution/
"""
O(height), O(height)
"""
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # case 1: if root is leaf node - just delete it
            if not root.left and not root.right:
                root = None
            
            # case 2: if root has right node - replace the root by the successor,
            # and then delete the successor in the right subtree root.right = deleteNode(root.right, root.val)
            elif root.right:
                root.val = self._successor(root)
                root.right = self.deleteNode(root.right, root.val)
            
            # case 3: if root has no right node - replace the root by the predessor
            # and then delete the predecessor in the left subtree root.left = deleteNode(root.left, root.val)
            else:
                root.val = self._predessor(root)
                root.left = self.deleteNode(root.left, root.val)
        
        return root
        
    def _successor(self, root):     # O(height), 因为一直都在往下走
        """
        Return the successor of the root by taking one step right and always left, cuz the successor is the node just larger than the root
        """
        curr = root.right
        while curr.left:
            curr = curr.left
        return curr.val
    
    def _predessor(self, root):
        """
        Return the predecessor of the root by taking one step left and then always right
        """
        curr = root.left
        while curr.right:
            curr = curr.right
        return curr.val

