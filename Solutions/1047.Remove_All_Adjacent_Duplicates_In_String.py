"""
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.

str = "-";
seq = ("a", "b", "c"); # 字符串序列
print str.join( seq );
"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        
        for ch in s:
            if len(st) != 0 and ch == st[-1]:
                st.pop()
            else:
                st.append(ch)
        return "".join(st)   
    
