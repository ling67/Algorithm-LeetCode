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
        maxSubSum = nums[0]
        prefixSum = 0       # 一般都是初始化为0
        minPrefixSum = 0    #只能定义为0，因为初始的prefixSum是0
        
        for num in nums:
            prefixSum += num
            maxSubSum = max(maxSubSum, prefixSum - minPrefixSum)  # 注意不能更换maxSubSum和minPrefixSum的更新顺序， 比如输入为[-1]
            minPrefixSum = min(minPrefixSum, prefixSum)  
            
        return maxSubSum
        

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



