"""
Given a string s, return true if a permutation of the string could form a palindrome.

 

Example 1:

Input: s = "code"
Output: false
Example 2:

Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true
 

Constraints:

1 <= s.length <= 5000
s consists of only lowercase English letters.
"""

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        ch_cnt = collections.defaultdict(int)
        for ch in s:
            if ch in ch_cnt:
                ch_cnt[ch] += 1
            else:
                ch_cnt[ch] = 1
        cnt = 0
        for k, v in ch_cnt.items():
            cnt += v % 2
        return cnt <= 1
                
            
