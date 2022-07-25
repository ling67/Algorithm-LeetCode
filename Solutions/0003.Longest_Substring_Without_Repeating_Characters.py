"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch_to_cnt = defaultdict(int)
        max_len = 0
        i = 0
        for j, ch in enumerate(s):
            ch_to_cnt[ch] += 1
            
            while i <= j and j - i + 1 > len(ch_to_cnt):    #判断每个字符只出现了一次
                ch_to_cnt[s[i]] -= 1
                if ch_to_cnt[s[i]] == 0:
                    del ch_to_cnt[s[i]]
                i += 1
            
            if j - i + 1 == len(ch_to_cnt):
                max_len = max(max_len, j - i + 1)
        
        return max_len
       
       

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        j = 0
        max_len = 0
        
        for i in range(len(s)):
            while j < len(s) and s[j] not in visited:
                visited.add(s[j])
                j += 1
            max_len = max(max_len, j - i)
            visited.remove(s[i])
        return max_len
