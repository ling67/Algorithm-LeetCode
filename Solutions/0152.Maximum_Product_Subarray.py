"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

"""
分析：
最后一步：对于最优的策略（乘积最大），一定有最后一个元素a[j]
第一种情况：最优策略的序列就是{a[j]}, 答案是a[j]
第二种情况，连续子序列长度大于1，name最优策略中a[j]前1个元素肯定是a[j-1]
但是如果a[j]是正数，我们虚妄以a[j-1]结尾的连续子序列乘积最大
如果a[j]是负数，我们希望以a[j-1]结尾的连续子序列乘积最小

1.状态定义 
f[i] 表示以a[i+1]结尾的连续子序列的最大乘积
g[i]表示以a[j]结尾的连续子序列的最小乘积
2.求什么
f[n-1]
3.初始化

4.递推公式

"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lens = len(nums)
        min_neg = [0 for _ in range(lens)]   #min_neg[i] = 以i结尾的最小负数
        max_pos = [0 for _ in range(lens)]   #max_pos[i] = 以i结尾的最大正数
        min_neg[0], max_pos[0] = nums[0], nums[0]
        for i in range(1, lens):
            if nums[i] >= 0:
                max_pos[i] = max(nums[i], max_pos[i-1] * nums[i])
                min_neg[i] = min(nums[i], min_neg[i-1] * nums[i])
            else:
                max_pos[i] = max(nums[i], min_neg[i-1] * nums[i])
                min_neg[i] = min(nums[i], max_pos[i-1] * nums[i])
                
        return max(max_pos)
