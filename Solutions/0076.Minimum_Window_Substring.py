Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
 
官方答案：https://leetcode.com/problems/minimum-window-substring/solutions/164122/minimum-window-substring/
 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = s + s
        t_cnt = collections.Counter(t)
        window_cnt = defaultdict(int)

        l = 0
        for r, ch in enumerate(s):
            window_cnt[ch] += 1

            # satisfy condition l need to move
            while l <= r and self.satisfy_condition(window_cnt, t_cnt):
                if r - l + 1 < len(res):
                    res = s[l:r+1] 
                
                window_cnt[s[l]] -= 1
                if window_cnt[s[l]] == 0:
                    del window_cnt[s[l]]
                l += 1

        return "" if res == s + s else res

    def satisfy_condition(self, cnter_s, cnter_t):
        for ch, cnt in cnter_t.items():
            if cnt > cnter_s[ch]:
                return False
        return True
 
 
"""
time complexity, O(mn) m is the time to check is_valid()
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_ch_cnt = Counter(t)  # record the character:freq of t
        window_ch_cnt = defaultdict(int) # record the character:freq of t
        min_len = sys.maxsize

        i, j = 0, 0
        start, end = 0, 0

        for i, ch in enumerate(s):
            while j < len(s) and not self.is_valid(window_ch_cnt, t_ch_cnt):
                window_ch_cnt[s[j]] += 1
                j += 1

            if self.is_valid(window_ch_cnt, t_ch_cnt):
                if j - i < min_len:
                    min_len = j - i
                    start, end = i, j

            window_ch_cnt[ch] -= 1
            if window_ch_cnt[ch] == 0:
                del window_ch_cnt[ch]

        return s[start:end]

    #check if all character cnter_t has already in cnter_s
    def is_valid(self, window_ch_cnt, t_ch_cnt):
        for ch, cnt in t_ch_cnt.items():
            if cnt > window_ch_cnt[ch]:
                return False
        return True
