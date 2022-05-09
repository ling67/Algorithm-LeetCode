"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""

"""
1.确定状态f[i] 设数字串S前i个数字解密成字母串有f[i]中方式
2.求 f[n]
3.初始化 f[0] = 0 f[1] = 1
4.递推公式：f[i] = f[i-1] + f[i-2]
时间复杂度O(n), 空 O(n)
注意：f[0] = 1, 且要判断i > 1
"""
"""
1.define state:dp[i] represent the number of ways to decode it first i string
2.get dp[n]
3.dp[0] = 1 dp[1] = 1
4.dp[i] = dp[i-1] + dp[i-2](if 10 < s[i-2.i-1] < 26)
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1  #只能初始化dp[0], dp[1]是不确定的
        
        for i in range(1, n+1):
            if s[i-1] >= '1' and s[i-1] <= '9':
                dp[i] += dp[i-1]
            
            if i > 1:
                j = 10 * int(s[i-2]) + int(s[i-1])
                if s[i-2] != '0' and j >= 10 and j <= 26:
                    dp[i] += dp[i-2]
        
        return dp[n]
        
        

