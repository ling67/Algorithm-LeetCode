"""
A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (variables), and internal nodes (nodes with two children) correspond to the operators. In this problem, we only consider the '+' operator (i.e. addition).

You are given the roots of two binary expression trees, root1 and root2. Return true if the two binary expression trees are equivalent. Otherwise, return false.

Two binary expression trees are equivalent if they evaluate to the same value regardless of what the variables are set to.

 

Example 1:

Input: root1 = [x], root2 = [x]
Output: true
Example 2:



Input: root1 = [+,a,+,null,null,b,c], root2 = [+,+,a,b,c]
Output: true
Explaination: a + (b + c) == (b + c) + a
Example 3:



Input: root1 = [+,a,+,null,null,b,c], root2 = [+,+,a,b,d]
Output: false
Explaination: a + (b + c) != (b + d) + a
 

Constraints:

The number of nodes in both trees are equal, odd and, in the range [1, 4999].
Node.val is '+' or a lower-case English letter.
It's guaranteed that the tree given is a valid binary expression tree.
 

Follow up: What will you change in your solution if the tree also supports the '-' operator (i.e. subtraction)?

"""

# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
遍历二叉树并且记录每个字母出现的频率，最后判断是否相等
只能解决只有+的问题
"""
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        def dfs(root, cnter):
            if not root:
                return
            if root.val.isalpha():
                cnter[root.val] += 1
            dfs(root.left, cnter)
            dfs(root.right, cnter)
        
        cnter1 = defaultdict(int)
        cnter2 = defaultdict(int)
        dfs(root1, cnter1)
        dfs(root2, cnter2)
        return cnter1 == cnter2
