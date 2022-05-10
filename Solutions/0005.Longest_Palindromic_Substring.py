"""
 Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""
  
"""
dp[i][j] 代表s[i...j]是不是一个回文串
dp[i][j] = True if dp[i+1][j-1] is true and s[i] = s[j] or j-i == 1
return the longest substring for all dp[i][j] = True
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
            
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j] and (j-i == 1 or dp[i+1][j-1]):
                    dp[i][j] = True
        
        maxLen = 1
        string = s[0]
        for i in range(n):
            for j in range(i+1, n):
                if dp[i][j] and maxLen < j-i+1:
                    maxLen = j-i+1
                    string = s[i:j+1]   #注意这里是不包括就j+1的
        return string
                        
