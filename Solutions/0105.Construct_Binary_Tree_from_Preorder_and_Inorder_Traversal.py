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
        def build(in_start, in_end):
            if in_start >= in_end:
                return None
            
            root = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1
            in_idx = num_idx[root.val]
            
            root.left = build(in_start, in_idx)
            root.right = build(in_idx + 1, in_end)
            
            return root
        
        
        num_idx = defaultdict(int)
        for idx, num in enumerate(inorder):
            num_idx[num] = idx
        
        self.pre_idx = 0
        return build(0, len(inorder))
