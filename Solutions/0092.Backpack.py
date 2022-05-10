"""
Description
Given n items with size A_{i}A 
i
​
  an integer m denotes the size of a backpack. How full you can fill this backpack?
(Each item can only be selected once and the size of the item is a positive integer)

Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang15)


You can not divide any item into small pieces.
n \lt 1000n<1000
m \lt 1e9m<1e9
Example
Example 1:

Input:

array = [3,4,8,5]
backpack size = 10
Output:

9
Explanation:

Load 4 and 5.

Example 2:

Input:

array = [2,3,5,7]
backpack size = 12
Output:

12
Explanation:

Load 5 and 7.
"""

from typing import (
    List,
)

"""
dp[i][j] represent first i array number can compose j backpack
dp[n][m]
dp[i][0] = true
dp[0][j] = False
dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
"""
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack(self, size: int, nums: List[int]) -> int:
        # write your code here
        lens = len(nums)

        dp = [[False] * (size+1) for _ in range(lens+1)]
        for i in range(lens+1):
            dp[i][0] = True

        for i in range(1, lens+1):
            for j in range(1, size+1):
                dp[i][j] = dp[i-1][j]

                if j >= nums[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]
        
        for i in range(size, -1, -1):
            if dp[lens][i]:
                return i
        
