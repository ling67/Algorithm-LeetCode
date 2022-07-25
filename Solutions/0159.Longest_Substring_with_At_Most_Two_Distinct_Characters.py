"""
Given a string s, return the length of the longest substring that contains at most two distinct characters.

 

Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
 

Constraints:

1 <= s.length <= 105
s consists of English letters.
"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ch_to_freq = collections.defaultdict(int)
        max_lens = 0
        i = 0
        for j in range(len(s)):
            ch_to_freq[s[j]] += 1
            
            while i <= j and len(ch_to_freq) > 2:
                ch_to_freq[s[i]] -= 1
                if ch_to_freq[s[i]] == 0:
                    del ch_to_freq[s[i]]
                i += 1
            
            if len(ch_to_freq) <= 2:
                max_lens = max(max_lens, j - i + 1)
        return max_lens
                
