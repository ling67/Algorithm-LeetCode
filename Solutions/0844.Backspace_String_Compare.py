"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.construct(s) == self.construct(t)
    
    def construct(self, s):
        st1 = []
        for ch in s:
            if st1:
                if ch == '#':
                    st1.pop()
                else:
                    st1.append(ch)
            else:
                if ch != '#':
                    st1.append(ch)
        return st1

# Solution 2: O(1) memery space     
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.construct(s) == self.construct(t)
    
    def construct(self, s):
        backspace_cnt = 0
        res = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "#":
                backspace_cnt += 1
            else:
                if backspace_cnt > 0:
                    backspace_cnt -= 1
                else:
                    res += s[i]
        return res[::-1]
