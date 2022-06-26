"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

 

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
 

Constraints:

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.
"""

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(curr_idx, curr_comb):
            if len(curr_comb) == len(s):
                res.append(curr_comb)
                return res
            
            if s[curr_idx + 1].isdigit():
                backtrack(curr_idx + 1, curr_comb + s[curr_idx + 1])
            else:
                for next_ch in [s[curr_idx + 1].lower(), s[curr_idx + 1].upper()]:
                    backtrack(curr_idx + 1, curr_comb + next_ch)
                    
        res = []
        backtrack(-1, "")
        return res



