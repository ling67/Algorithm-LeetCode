"""
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

 

Example 1:


Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]
"""


"""
solution 1: time complexity O(N^2). space complexity O(1)
把这棵树画出来pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1] 自然就明白了代码怎么写了！
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        root = TreeNode(preorder.pop(0))   #the first element in preprder is the root
        postorder.pop()   #the last element in postorder is the root
        idx = 0 
        for i, val in enumerate(postorder):  
            if postorder[i] == preorder[0]:   #the element follow the root is the subtree root
                idx = i
                break
        root.left = self.constructFromPrePost(preorder, postorder[:idx + 1])
        root.right = self.constructFromPrePost(preorder, postorder[idx + 1:])
        return root
      
"""
solution 2: O(N)
1. find the idx for root: pre[start]
2. find the idx for left tree: pre_root_idx + 1
3. find the idx for right tree: post_root_idx - 1
4. recurssive call
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def helper(preorder, postorder):
            if not preorder or not postorder:
                return None
            root = TreeNode(preorder.pop(0))   #the first element in preprder is the root
            postorder.pop()   #the last element in postorder is the root
            if len(preorder) > 0:    #do not forget check the length
                idx = self.num_idx[preorder[0]]
                root.left = self.constructFromPrePost(preorder, postorder[:idx + 1])
                root.right = self.constructFromPrePost(preorder, postorder[idx + 1:])
            return root
        
        self.num_idx = collections.defaultdict(int)   #this is class variable
        for idx, val in enumerate(postorder):
            self.num_idx[val] = idx
            
        return helper(preorder, postorder)
        
