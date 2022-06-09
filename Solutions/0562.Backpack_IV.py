"""
Description
Give n items and an array, num[i] indicate the size of ith item. An integer target denotes the size of backpack. Find the number of ways to fill the backpack.

Each item may be chosen unlimited number of times

Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang15)


Example
Example1

Input: nums = [2,3,6,7] and target = 7
Output: 2
Explanation:
Solution sets are: 
[7]
[2, 2, 3]
Example2

Input: nums = [2,3,4,5] and target = 7
Output: 3
Explanation:
Solution sets are: 
[2, 5]
[3, 4]
[2, 2, 3]
"""

from typing import (
    List,
)

class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    每个物品只能取一个递推公式：
    dp[i][j] 个数 = dp[i - 1][j - A[i - 1]] + dp[i - 1][j]
    """
    def back_pack_i_v(self, nums: List[int], target: int) -> int:
        # write your code here
        m = len(nums)
        dp = [[0] * (target + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        for i in range(1, m + 1):
            for j in range(0, target + 1):
                k = 0
                while k * nums[i - 1] <= j:
                    dp[i][j] += dp[i - 1][j - nums[i - 1] * k]
                    k += 1
        return dp[m][target] 

