"""
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
 

Constraints:

1 <= s.length <= 5 * 104
0 <= k <= 50
"""

"""
最多k个，第二种问题，最长字串用max_cnt标记，还需要ch_to_cnt记录已经加入的ch个数
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ch_to_cnt = defaultdict(int)
        max_cnt = 0
        i = 0
        for j in range(len(s)):
            ch_to_cnt[s[j]] += 1       # 不管是哪种模板，都是先更新后面的指针
            
            while i <= j and len(ch_to_cnt) > k:    #不满足条件怎么更新
                ch_to_cnt[s[i]] -= 1
                if ch_to_cnt[s[i]] == 0:
                    del ch_to_cnt[s[i]]
                i += 1
            
            if len(ch_to_cnt) <= k:      #满足条件，更新res
                max_cnt = max(max_cnt, j - i + 1)
            
        return max_cnt
            
        
