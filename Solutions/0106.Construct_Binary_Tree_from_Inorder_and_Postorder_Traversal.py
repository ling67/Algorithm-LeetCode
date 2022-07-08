"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""
"""
solution 1: O(N^2)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())  #delete the last element in array, use pop()
        idx = inorder.index(root.val)
        
        root.right = self.buildTree(inorder[idx+1:], postorder) # 注意要先更新right, 这是因为我们需要对postorder做pop
        root.left = self.buildTree(inorder[:idx], postorder)    # 只有先把后面的pop出来才能去pop前面的，而postorder后面的对应的是right部分
        
        return root       
    
            # idx = 0
        # for i, num in enumerate(inorder):
        #     if num == root.val:
        #         idx = i
        #         break
      
"""
solution 1 takes O(N^2) because each time we find idx in inorder, it takes O(N).
We can use a hash table to store the num-to-idx pair in advance.
This leads to solution 2, which is O(N) instead of O(N^2).
"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(start, end):
            if start >= end:
                return None
            root = TreeNode(postorder.pop())
            idx = num_idx[root.val]
            
            root.right = build(idx + 1, end)        # 注意right要放到left前面更新
            root.left = build(start, idx)        
        
            return root  
        
        num_idx = defaultdict(int)
        for idx, num in enumerate(inorder):
            num_idx[num] = idx
        return build(0, len(inorder))
        
