"""
Description
Given an array of integers, find how many pairs in the array such that their sum is bigger than a specific target number. Please return the number of pairs.

Wechat reply 【443】 get the latest requent Interview questions . (wechat id : jiuzhang15)

Example
Example 1:

Input: [2, 7, 11, 15], target = 24
Output: 1
Explanation: 11 + 15 is the only pair.
Example 2:

Input: [1, 1, 1, 1], target = 1
Output: 6
Challenge
Do it in O(1) extra space and O(nlogn) time.

"""

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        nums.sort()
        l, r = 0, len(nums) - 1
        count = 0

        while l < r:
            if nums[l] + nums[r] <= target:
                l += 1
            else:
                count += r - l   #若 nums[l] + nums[r] > target, 则 nums[l + k] + nums[r] > target (k >= 0)
                r -= 1

        return count
            
