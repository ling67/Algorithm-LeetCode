"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.
"""

"""
至少多少右括号：
至多多少右括号：如果这个值为负数说明中间有时候可能）数目大于（数目
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        l = r = 0
        for ch in s:
            if ch == '(':
                l += 1
                r += 1
            elif ch == ')':
                if l > 0:
                    l -= 1 
                r -= 1
            else:
                if l > 0:
                    l -= 1
                r += 1
            if r < 0:
                return False
        return l == 0
