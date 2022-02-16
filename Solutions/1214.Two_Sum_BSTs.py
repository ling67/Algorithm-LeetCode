"""
Given the roots of two binary search trees, root1 and root2, return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.
Example 2:


Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false
 

Constraints:

The number of nodes in each tree is in the range [1, 5000].
-109 <= Node.val, target <= 109
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. hashset
# 2. in-order-traversal + 反向双指针
# 3. brutal force

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        # step 1:put the node of 1st tree into a hash set
        hashset = set()
        curr = root1
        st = []
        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left
            curr = st.pop()
            hashset.add(curr.val)
            curr = curr.right
            
        #step 2: loop over the 2nd tree and see if there is a node add up to target
        curr = root2
        st = []
        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left
            curr = st.pop()
            if target - curr.val in hashset:
                return True
            curr = curr.right
        return False
