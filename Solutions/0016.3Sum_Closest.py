/*
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0

*/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        lens = len(nums)
        closet_sum = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(lens - 2):
            l, r = i + 1, lens - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                #check if we need update closet_sum
                if abs(three_sum - target) < abs(closet_sum - target):
                    closet_sum = three_sum
                
                #check how to move point
                if three_sum > target:
                    r -= 1
                else: 
                    l += 1
                
        return closet_sum
            
                

class Solution {
    public int threeSumClosest(int[] nums, int target) { 
        if (nums == null || nums.length < 3) {
            return -1;
        }
        //首先对数组进行排序
        Arrays.sort(nums);
        int bestSum = nums[0] + nums[1] + nums[2];
        //遍历，固定一端端点
        for (int i = 0; i < nums.length - 2; i++) {
            //定义双指针，双指针相向而行
            int left = i + 1, right = nums.length - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                // 更新bestSum
                if (Math.abs(target - sum) < Math.abs(target - bestSum)){
                    bestSum = sum;
                }                
                if (sum > target) {
                    right--;
                } else {
                    left++;
                } 
            }
        }
        return bestSum;  
    }
}
