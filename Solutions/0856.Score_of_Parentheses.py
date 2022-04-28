"""
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: s = "()"
Output: 1
Example 2:

Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2
 

Constraints:

2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.
"""

#stack
//https://leetcode-cn.com/problems/score-of-parentheses/solution/gua-hao-de-fen-shu-by-leetcode/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for x in s:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2*v, 1)
        
        return stack.pop()

    
"""
        ((()()))  
        basicly we just use a stack         
        we are just gonna have a thing called score this is what we are gonna to return
        we are just gonna loop through wach character of the string 
        there are two diff char we could potentially see 
        so a equal to open parenthesis, then we will do something
        otherwise we will also do somthing
        so what we do here, we just push the score on 
"""
