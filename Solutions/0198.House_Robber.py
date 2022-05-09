"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

"""
1.define state: dp_steal[i] represent the max profit if steal i
dp_not_steal[i] represent the max profit if not steal i
2.get max{dp_steal[n-1], dp_not_steal[n-1]}
3.dp_steal[0] = nums[0] dp_not_steal[0] = 0
4.dp_steal[i] = max{dp_steal[i-2], dp_not_steal[i-2], dp_not_steal[i-1]} + nums[i]
dp_not_steal[i] = max{dp_steal[i-1], dp_not_steal[i-1]}
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp_steal = [0] * n
        dp_not_steal = [0] * n
        
        dp_steal[0] = nums[0]
        dp_not_steal[0] = 0
        dp_steal[1] = nums[1]
        dp_not_steal[1] = nums[0]
        
        for i in range(2, n):
            dp_steal[i] = max(dp_steal[i-2], dp_not_steal[i-2], dp_not_steal[i-1]) + nums[i]    
            dp_not_steal[i] = max(dp_steal[i-1], dp_not_steal[i-1])
            
        return max(dp_steal[n-1], dp_not_steal[n-1])

       
"""
1.状态定义 dp[i][0] 不偷第i+1栋房子的最大金币 dp[i][1] 偷第i+1栋房子的最大金币
2.求 min(dp[n-1][0], dp[n-1][1])
3.初始化 dp[0][0] = 0, dp[0][1] = 1
4.递推公式 dp[i][0] = min(dp[i-1][0] dp[i-1][1])
dp[i][1] = dp[i-1][0]
0代表不偷， 1代表偷
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0], dp[0][1] = 0, nums[0]
        
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]) 
            dp[i][1] = dp[i-1][0] + nums[i]
            
        return max(dp[n-1])
      
#version2:
"""
1.状态定义 f[i]=the max profit when reaching ith house
2.求 f[n-1]
3.初始化 f[0] = nums[0]
4.递推公式 f[i] = max(f[i-1], f[i-2]+nums[i])
0代表不偷， 1代表偷
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        for i in range(1, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]) 
            
        return dp[-1]
        
#version3：改成滚动数组
"""空间优化：dp[i] 之和 dp[i-2]与dp[i-1]有关，所以可以用prevMax和currMax来代表dp[i-2]与dp[i-1]"""
"""
1.状态定义 f[i]=the max profit when reaching ith house
2.求 f[n-1]
3.初始化 f[0] = nums[0]
4.递推公式 f[i] = max(f[i-1], f[i-2]+nums[i])
0代表不偷， 1代表偷
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMax, currMax = 0, 0   #prevMax is dp[i-2], currMax is dp[i-1]
        for i in range(len(nums)):
            temp = currMax
            currMax = max(prevMax + nums[i], currMax)
            prevMax = temp
            
        return currMax
        
