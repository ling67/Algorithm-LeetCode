"""
Description
Given an array of integers, find how many pairs in the array such that their sum is less than or equal to a specific target number. Please return the number of pairs.

Wechat reply 【609】 get the latest requent Interview questions . (wechat id : jiuzhang15)

Example
Example 1:

Input: nums = [2, 7, 11, 15], target = 24. 
Output: 5. 
Explanation:
2 + 7 < 24
2 + 11 < 24
2 + 15 < 24
7 + 11 < 24
7 + 15 < 24
Example 2:

Input: nums = [1], target = 1. 
Output: 0. 

"""

class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        nums.sort()
        i, j = 0, len(nums)-1
        count = 0

        while i < j:
            sums = nums[i] + nums[j]
            if sums <= target:
                count += j - i   # 注意这里是 cnt += j - i 表示nums[i] 加上 (i 到 j之间的任何数)，一定也是小于等于target的
                i += 1
            else :
                j -= 1
        return count

