"""
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

 

Constraints:

1 <= nums.length <= 2000
-106 <= nums[i] <= 106
"""

"""
1.状态定义：
dp[i] 以i结尾的最大的长度 
cnt[i] 以i结尾的最大长度的个数 
2.求max{cnt}
3.初始化：dp[0] = 1 cnt[0] = 1
4.递推公式：
dp[i] = max{dp[j] + 1} if nums[i] > nums[j] and j < i
cnt[i] = 
"""
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n  #以i结尾的最大的长度
        cnt = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] = cnt[i] + cnt[j]
                        
        maxValue = max(dp)
        num = 0
        for i in range(n):
            if dp[i] == maxValue:
                num += cnt[i]
                
        return num
            
                    
