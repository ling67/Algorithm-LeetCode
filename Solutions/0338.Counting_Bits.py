"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""

"""
状态f[i]=i的二进制中有多少个1
和位操作相关的动态规划一般用值作为状态
转移方程f[i] = f[i>>1] + i%2
i>>1表示i往右移动一位，最后一位就撞到墙了就撞没了。
初始条件为f[0]=0
O(N)， O（N）
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        dp = [0 for _ in range(n+1)]
        dp[0] = 0
        for i in range(1, n + 1):
            dp[i] = dp[i//2] + i % 2
        return dp
        
