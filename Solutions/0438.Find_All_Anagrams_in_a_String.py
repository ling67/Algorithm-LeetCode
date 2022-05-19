"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res =[]
        ch_cnt = Counter(p) #store p 的字母和频次对应关系
        k = len(p)   #记录p的长度
        ch_cnt_window = defaultdict(int)  #store 滑动窗口内字母和频次的对应关系
        
        for i in range(len(s)):
            ch_cnt_window[s[i]] += 1
            
            if i >= k:
                ch_cnt_window[s[i - k]] -= 1
                if ch_cnt_window[s[i - k]] == 0:
                    del ch_cnt_window[s[i - k]]
            
            if ch_cnt_window == ch_cnt:
                res.append(i - k + 1)
                
        return res
