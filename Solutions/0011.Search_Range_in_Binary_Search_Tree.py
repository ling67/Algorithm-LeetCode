"""
Description
Given a binary search tree and a range [k1, k2], return node values within a given range in ascending order.

Wechat reply the【Video】get the free video lessons , the latest frequent Interview questions , etc. (wechat id :jiuzhang15)


Example
Example 1:

Input:

tree = {5}
k1 = 6
k2 = 10
Output:

[]
Explanation:

No number between 6 and 10

Example 2:

Input:

tree = {20,8,22,4,12}
k1 = 10
k2 = 22
Output:

[12,20,22]
Explanation:

[12,20,22] between 10 and 22

"""

from typing import (
    List,
)
from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def search_range(self, root: TreeNode, k1: int, k2: int) -> List[int]:
        # write your code here
        
        #exit
        if not root:
            return []

        res = []

        #divide
        if root.val > k2:
            res.extend(self.search_range(root.left, k1, k2))
        elif root.val < k1:
            res.extend(self.search_range(root.right, k1, k2))
        else:
            res.extend(self.search_range(root.left, k1, k2))
            res.append(root.val)
            res.extend(self.search_range(root.right, k1, k2))
        
        #conquer
        return res

