"""
  Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105
  
"""
  
  
  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Solution 1: First convert the BST into a sortedArr using inorder traversal, then use two pointer method to do the two sum problem
#iterative in-order traversal of a tree要背熟  TODO

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        sortedArr = self.inorder(root)
        i,j = 0, len(sortedArr) - 1
        while i < j:
            if sortedArr[i] + sortedArr[j] > k:
                j -= 1
            elif sortedArr[i] + sortedArr[j] < k:
                i += 1
            else:
                return True
        return False
    
    
    def inorder(self, root):
        res = []
        if not root:
            return res
        
        if root.left:
            res += self.inorder(root.left)
        res.append(root.val)
        if root.right:
            res += self.inorder(root.right)
            
        return res

"""
一边遍历，一边check，遍历：递归，栈
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = set()
        st = [root]    #栈
        while st:
            cur = st.pop()
            if k - cur.val in nums:
                return True
            nums.add(cur.val)
            if cur.left:
                st.append(cur.left)
            if cur.right:
                st.append(cur.right)
        return False
