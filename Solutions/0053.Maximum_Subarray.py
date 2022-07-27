/*
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
*/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #step1:构造前缀和pre_sum
        pre_sum = [0 for _ in range(len(nums) + 1)]
        for i, num in enumerate(nums):
            pre_sum[i + 1] = pre_sum[i] + num
        
        #step2:the same as 127.best time to buy and sell stock
        min_pre = float("inf")
        max_sum = float("-inf")
        for pre in pre_sum:
            max_sum = max(max_sum, pre - min_pre)     # 注意不能更换maxSubSum和minPrefixSum的更新顺序,why， 比如输入为[-1]
            min_pre = min(min_pre, pre)
        return max_sum

    
    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = cur = nums[0]
        for n in nums[1:]:
            cur = max(cur + n, n)
            res = max(res, cur)
        return res
    
    

/************************************Java Version******************************************/
class Solution {
    public int maxSubArray(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        
        //sum记录前i个数的和，max记录全局最大值，minSum记录前i个数中0-k的最小值
        int max = Integer.MIN_VALUE, sum = 0, minSum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            max = Math.max(max, sum - minSum);
            minSum = Math.min(minSum, sum);
        }
        return max;
    }
}



