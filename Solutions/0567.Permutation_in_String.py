"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

"""
permutation:排列，顺序不一样
solution 1: 由于我们要求的substring时固定长度的，所以最好maintina a fixed size window - 套用fix window模板
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)   #store s1的长度
        cnter_2 = Counter(s1)   #store s1的字符和频次
        ch_to_cnt = defaultdict(int)   #记录窗口内的字母和频次的对应关系
        
        for i in range(len(s2)):
            ch_to_cnt[s2[i]] += 1
            
            if i >= k:
                ch_to_cnt[s2[i - k]] -= 1
                if ch_to_cnt[s2[i - k]] == 0:
                    del ch_to_cnt[s2[i - k]]
            
            if ch_to_cnt == cnter_2:
                return True
            
        return False
