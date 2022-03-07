"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

Constraints:

1 <= n <= 104
"""

"""
时间复杂度n根号n->讲的没懂
1.确定状态 dp[i] 表示最少的数的平方之和为i
2.求  dp[n]
3.初始值 dp[0] 0 dp[1] = 1
4.递推公式 dp[i] = min(dp[j] + 1)
f[i]=the least number of perfect square numbers which sum to i
f[j] = min(f[j-i^2]+1) for i^2<=j
Time complexity: j is from 0 to n, i is from 0 to j^0.5, so O(N^1.5)
超时啦
"""
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(1, n+1):
            j = 1
            while j**2 <= i:
                dp[i] = min(dp[i],  dp[i - j**2] + 1)
                j += 1
                
        return dp[-1]
