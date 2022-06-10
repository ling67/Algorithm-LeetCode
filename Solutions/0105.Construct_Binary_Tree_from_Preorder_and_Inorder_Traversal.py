"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder.pop(0))
        idx = inorder.index(root.val)
        
        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])
        
        return root

"""
solution 1中需要O(N^2)的原因是1. preorder.pop(0) takes O(N). We can convert preorder into a q and popleft.
2. finding the idx in inorder list takes O(N). We can use a hash table to store num-to-idx pair in advance.
This leads to solution 2, which takes O(N) instead of O(N^2).
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(preorder_q, start, end):
            if start >= end:
                return None
            
            root = TreeNode(preorder_q.popleft())   # now this takes O(1)
            idx = inorder_idx[root.val]             # now this takes O(1)
            
            # 注意此时必须把start和idx都传进helper function, 因为如果传inorder[:idx]的话，
            # 会导致后面找inorder[:idx]这个subarray中的idx的时候和hash table中的不一样
            root.left = helper(preorder_q, start, idx)  
            root.right = helper(preorder_q, idx + 1, end)
            
            return root
        
        
        preorder_q = collections.deque(preorder)    # use a queue to store preorder list
        inorder_idx = collections.defaultdict(int)  # use a hash table to store num-to-idx pair
        for i, num in enumerate(inorder):
            inorder_idx[num] = i
            
        return helper(preorder_q, 0, len(inorder))
