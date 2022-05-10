"""
Description
There are n items and a backpack with size m. Given array A representing the size of each item and array V representing the value of each item.

What's the maximum value can you put into the backpack?

Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang15)


A[i], V[i], n, m are all integers.
You can not split an item.
The sum size of the items you want to put into backpack can not exceed m.
Each item can only be picked up once
m <= 1000m<=1000\
len(A),len(V)<=100len(A),len(V)<=100

Example
Example 1:

Input:

m = 10
A = [2, 3, 5, 7]
V = [1, 5, 2, 4]
Output:

9
Explanation:

Put A[1] and A[3] into backpack, getting the maximum value V[1] + V[3] = 9

Example 2:

Input:

m = 10
A = [2, 3, 8]
V = [2, 5, 8]
Output:

10
Explanation:

Put A[0] and A[2] into backpack, getting the maximum value V[0] + V[2] = 10

Challenge
O(nm) memory is acceptable, can you do it in O(m) memory?
"""

from typing import (
    List,
)
"""
dp[i][j] 前i个放入容量j中的最大value
dp[size][m]
dp[i][j] max{dp[i-1][j], dp[i-1][j-nums[i-1]] + v[i-1]}
"""
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @param v: Given n items with value V[i]
    @return: The maximum value
    """
    def back_pack_i_i(self, m: int, a: List[int], v: List[int]) -> int:
        # write your code here
        size = len(a)
        dp = [[0] * (m+1) for _ in range(size+1)]

        for i in range(1, size+1):
            for j in range(1, m+1):
                dp[i][j] = dp[i-1][j]
                if j >= a[i-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-a[i-1]] + v[i-1])
        return dp[size][m]
