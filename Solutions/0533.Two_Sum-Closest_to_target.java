/*
Description
Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.

Return the absolute value of difference between the sum of the two numbers and the target.

Example
Example1

Input:  nums = [-1, 2, 1, -4] and target = 4
Output: 1
Explanation:
The minimum difference is 1. (4 - (2 + 1) = 1).
*/

public class Solution {
    /**
     * @param nums: an integer array
     * @param target: An integer
     * @return: the difference between the sum and the target
     */
    public int twoSumClosest(int[] nums, int target) {
        // write your code here
        if (nums == null || nums.length < 2) {
            return -1;
        }

        Arrays.sort(nums);
        
        int left = 0, right = nums.length - 1;
        int diff = Integer.MAX_VALUE;
        
        while (left < right) {
            int sum = nums[left] + nums[right];
            diff = (diff > Math.abs(target - sum)) ? Math.abs(target - sum) : diff;
            if (sum > target) {
                right--;
            } else {
                left++;
            }
        }
        return diff;
    }
}
