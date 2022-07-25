"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""


"""
Given a string convert it to a string with all same characters with minimal changes. 
The answer is (length of the entire substring) - (number of times of the maximum occurring character in the string).
Given this, this problem is to find the max_lens of substring so that 
(length of substring - number of times of the maximum occurring character in the substring) is at most K.
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ch_to_cnt = collections.defaultdict(int)
        max_lens = 0
        max_occur = 0       # number of times of the maximum occurring character in the string
        i = 0
        for j in range(len(s)):
            ch_to_cnt[s[j]] += 1
            max_occur = max(max_occur, ch_to_cnt[s[j]])
            
            while i <= j and j - i + 1 - max_occur > k:   # window的长度是j - i + 1, window长度减去max_occur就是需要replace的次数
                ch_to_cnt[s[i]] -= 1
                i += 1
                
            if j - i + 1 - max_occur <= k:
                max_lens = max(max_lens, j - i + 1)
                
        return max_lens

