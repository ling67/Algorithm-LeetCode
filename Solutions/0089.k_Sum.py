"""
Description
Given n distinct positive integers, integer k (k \leq n)(k≤n) and a number target.

Find k numbers where sum is target. Calculate how many solutions there are?

Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang15)


Example
Example 1:

Input:

A = [1,2,3,4]
k = 2
target = 5
Output:

2
Explanation:

1 + 4 = 2 + 3 = 5
Example 2:

Input:

A = [1,2,3,4,5]
k = 3
target = 6
Output:

1
Explanation:

There is only one method. 1 + 2 + 3 = 6
"""

from typing import (
    List,
)

"""
•要求从一些正整数中选出一些，使得和是Target
• 背包问题
• 数组A：各个物品的重量
• Target：背包最大称重
• 使得和是Target：背包正好装满
• 最后一步：最后一个数An-1是否选入这K个数
• 情况一（An-1不选入）：需要在前n-1个数中选K个数，使得它们的和
是Target
• 情况二（An-1选入）：需要在前n-1个数中选K-1个数，使得它们的和是
Target - An-1
• 要知道还有几个数可选，以及它们的和需要是多少：序列加状态
• 状态：f[i][j][s]表示有多少种方法可以在前i个数中选出j个，使得它们的和是s
f[i][j][s] = f[i-1][j][s]; if s>=A[i-1]: f[i][j][s] += f[i-1][k-1][s-A[i-1]]
"""

"""
采用动态规划（dp）的思想，进行状态转移，记录数字和和出现次数之间的关系。
用dp[i][j][t]表示前i个数里选j个和为t的方案数。
dp[i][j][t] = 选A[i-1]: dp[i-1][j-1][t-A[i-1]] + 不选 A[i-1]: dp[i-1][j][t]
initialize: dp[i][0][0] = 1
return dp[lens][k][target]
"""

class Solution:
    """
    @param a: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def k_sum(self, a: List[int], k: int, target: int) -> int:
        # write your code here
        dp = [[[0 for _ in range(target + 1)] for _ in range(k + 1)] for _ in range(len(a) + 1)]
        for i in range(len(a) + 1):
            dp[i][0][0] = 1

        for i in range(1, len(a) + 1):
            for j in range(1, min(k + 1, i + 1)):
                for m in range(1, target + 1):
                    dp[i][j][m] = dp[i-1][j][m]
                    if m >= a[i-1]:
                        dp[i][j][m] += dp[i-1][j-1][m-a[i-1]]
        return dp[-1][-1][-1]


