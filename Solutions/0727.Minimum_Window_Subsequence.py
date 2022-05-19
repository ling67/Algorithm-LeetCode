"""
Given strings s1 and s2, return the minimum contiguous substring part of s1, so that s2 is a subsequence of the part.

If there is no such window in s1 that covers all characters in s2, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

 

Example 1:

Input: s1 = "abcdebdde", s2 = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of s2 in the window must occur in order.
Example 2:

Input: s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"
Output: ""
 

Constraints:

1 <= s1.length <= 2 * 104
1 <= s2.length <= 100
s1 and s2 consist of lowercase English letters.

"""

// 方法1：超时
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_lens = len(s)
        res = ""
        j = 0
        for i in range(len(s)):     # O(N)
            while j < len(s) and not self._is_subseq(s[i:j], t):
                j += 1
            
            if j - i < min_lens and self._is_subseq(s[i:j], t):
                min_lens = j - i
                res = s[i:j]        # O(N) here could be optimized to O(1), see below solution
        
        return res
    
    def _is_subseq(self, s, t):       # taks O(M)
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == len(t)
 

 """
solution 3: dp
dp[i][j] = the minimum window subsequence that ends with ith in s, and jth in t
if s[i-1] == t[j-1]: dp[i][j] = 1 + dp[i-1][j-1]
else: dp[i][j] = 1 + dp[i-1][j]
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        dp = [[20000] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + dp[i-1][j]
        
        min_len = min(dp[i][n] for i in range(m + 1))
        if min_len == 20000:
            return ""
        for i in range(m + 1):
            if dp[i][n] == min_len:
                return s[i-min_len:i]      
 
