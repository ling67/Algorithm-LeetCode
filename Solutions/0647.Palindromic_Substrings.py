"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""

"""
dp[i][j] represent s[i:j] is palindromic substring?
dp[i][j] if s[i] == s[j] and i + 1 = j True if i+1 != j dp[i][j] = dp[i+1][j-1]
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if i+1 == j:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
        
        cnt = 0
        for i in range(n):
            for j in range(n):
                if dp[i][j]:
                    cnt += 1
        
        return cnt
        
