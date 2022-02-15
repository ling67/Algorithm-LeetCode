"""
Description
Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.

Wechat reply 【587】 get the latest requent Interview questions . (wechat id : jiuzhang15)

Example
Example 1:

Input: nums = [1,1,2,45,46,46], target = 47 
Output: 2
Explanation:

1 + 46 = 47
2 + 45 = 47
Example 2:

Input: nums = [1,1], target = 2 
Output: 1
Explanation:
1 + 1 = 2
"""

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        nums.sort()
        lens = len(nums)
        i, j = 0, lens - 1
        count = 0
        last_pair = (None, None)

        while i < j:
            twoSum = nums[i] + nums[j]
            if twoSum == target:
                if (nums[i], nums[j]) != last_pair:
                    count += 1
                last_pair = (nums[i], nums[j])
                i, j =i + 1, j - 1 
            elif twoSum > target:
                j -= 1
            else:
                i += 1
        return count
                
