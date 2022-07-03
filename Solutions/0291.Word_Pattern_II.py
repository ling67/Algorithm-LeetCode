"""
Given a pattern and a string s, return true if s matches the pattern.

A string s matches a pattern if there is some bijective mapping of single characters to strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.

 

Example 1:

Input: pattern = "abab", s = "redblueredblue"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "red"
'b' -> "blue"
Example 2:

Input: pattern = "aaaa", s = "asdasdasdasd"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "asd"
Example 3:

Input: pattern = "aabb", s = "xyzabcxzyabc"
Output: false
 

Constraints:

1 <= pattern.length, s.length <= 20
pattern and s consist of only lowercase English letters.
"""

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def backtrack(curr_s_idx, curr_p_idx):
            if curr_s_idx == len(s) - 1 and curr_p_idx == len(pattern) - 1:
                return True
            if curr_s_idx == len(s) - 1:
                return False
            if curr_p_idx == len(pattern) - 1:
                return False
            for next_s_idx in range(curr_s_idx + 1, len(s)):
                next_ch = pattern[curr_p_idx + 1]
                next_word = s[curr_s_idx + 1: next_s_idx + 1]
                if next_ch in ch_to_str:
                    if ch_to_str[next_ch] != next_word or str_to_ch[next_word] != next_ch:
                        continue
                    if backtrack(next_s_idx, curr_p_idx + 1):
                        return True
                else:
                    if next_word in str_to_ch:
                        continue
                    ch_to_str[next_ch] = next_word
                    str_to_ch[next_word] = next_ch
                    if backtrack(next_s_idx, curr_p_idx + 1):
                        return True
                    del ch_to_str[next_ch]
                    del str_to_ch[next_word]
            return False
        
        ch_to_str = collections.defaultdict(str)
        str_to_ch = collections.defaultdict(str)
        return backtrack(-1, -1)

