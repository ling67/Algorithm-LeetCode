"""
Description
Given n items with size nums[i] which an integer array and all positive numbers. An integer target denotes the size of a backpack. Find the number of possible ways to fill the backpack.
Each item may only be used once

Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang15)


Example
Given candidate items [1,2,3,3,7] and target 7,

A solution set is: 
[7]
[1, 3, 3]
return 2
"""

from typing import (
    List,
)
"""
dp[i][j] 前i个数fill重量为J的可能的方式
dp[0][0] = 0
dp[size][target]
dp[i][j] = dp[i-1][j] + dp[i-1][j-num[i-1]]
"""
class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def back_pack_v(self, nums: List[int], target: int) -> int:
        # write your code here
        size = len(nums)
        dp = [[0] * (target+1) for _ in range(size+1)]
        for i in range(size+1):
            dp[i][0] = 1

        for i in range(1, size+1):
            for j in range(1, target+1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1]:
                    dp[i][j] += dp[i-1][j-nums[i-1]]

        return dp[size][target]
