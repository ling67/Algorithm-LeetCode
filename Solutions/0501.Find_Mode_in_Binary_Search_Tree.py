"""
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [1,null,2,2]
Output: [2]
Example 2:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
 

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if not root:
                return
            freq[root.val] += 1
            dfs(root.left)
            dfs(root.right)
        
        if not root:
            return []
        
        freq = collections.defaultdict(int)
        dfs(root)
        max_freq = max(f for f in freq.values())
        return [key for key, f in freq.items() if f == max_freq]

      
 """
Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""
"""
Before we do the follow up question for BST. Let's think how to do it in a sorted arr with O(1) space.
We dynamically update the curr_cnt and max_cnt and res, by comparing prev with curr.
"""
def find_mode(arr):
    curr_cnt = 1
    max_cnt = 1
    res = []
    prev = arr[0]
    for num in arr[1:]:
        curr_cnt = curr_cnt + 1 if num == prev else 1  # 如果不相等就reset curr_cnt=1
        if curr_cnt == max_cnt:
            res.append(num)
        elif curr_cnt > max_cnt:
            res = [num]
            max_cnt = curr_cnt
        prev = num
    return res

if __name__ == "__main__":
    arr = [1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6]
    print(find_mode(arr))
    
    
    
    
"""
solving BST problems is very similar with solving sorted arr problems.
we just need to do in order traversal of the tree.
O(N), O(1)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        self.prev = None
        self.max_cnt = 1
        self.curr_cnt = 1
        self.res = []
        
        self.inorder(root)
        return self.res
        
    def inorder(self, root):    
        if not root:
            return 
        
        self.inorder(root.left)
        
        if self.prev:
            self.curr_cnt = self.curr_cnt + 1 if root.val == self.prev.val else 1   # 如果不相等就reset curr_cnt=1
        if self.curr_cnt == self.max_cnt:
            self.res.append(root.val)
        elif self.curr_cnt > self.max_cnt:
            self.res = [root.val]               # 这里更新res的时候要清除之前的items
            self.max_cnt = self.curr_cnt
            
        self.prev = root      # 注意in-order traversal prev change to curr
        
        self.inorder(root.right)
