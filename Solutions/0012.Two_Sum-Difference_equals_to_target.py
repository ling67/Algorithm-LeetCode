"""
Description
Given an sorted array of integers, find two numbers that their difference equals to a target value.
Return a list with two number like [num1, num2] that the difference of num1 and num2 equals to target value, and num1 is less than num2.

Wechat reply the 【610】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

It's guaranteed there is only one available solution.
Note: Requires O(1) space complexity to comple

Example
Example 1:

Input: nums = [2, 7, 15, 24], target = 5 
Output: [2, 7] 
Explanation:
(7 - 2 = 5)
Example 2:

Input: nums = [1, 1], target = 0
Output: [1, 1] 
Explanation:
(1 - 1 = 0)
"""

class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        if not nums:
            return [-1, -1]

        n = len(nums)    

        target = abs(target)

        j = 0
        for i in range(n):
            if i == j:
                j += 1
            while j < n and nums[j] - nums[i] < target:
                j += 1
            if j < n and nums[j] - nums[i] == target:
                return [nums[i], nums[j]]
        
