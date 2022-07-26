"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_cnt = 0
        vowel_cnt = 0
        for i, ch in enumerate(s):
            vowel_cnt += 1 if ch in "aeiou" else 0    # step 1: 把ith item加进去
            
            if i >= k:  
                vowel_cnt -= 1 if s[i - k] in "aeiou" else 0    # step 2: 把(i-k)th item 吐出来
            
            max_cnt = max(max_cnt, vowel_cnt)     # step 3: 更新res
        
        return max_cnt

