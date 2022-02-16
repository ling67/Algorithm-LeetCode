"""
Description
Partition an integers array into odd number first and even number second.

Wechat reply 【373】 get the latest requent Interview questions . (wechat id : jiuzhang15)

The answer is not unique. All you have to do is give a vaild answer.

Example
Example 1:

Input: [1,2,3,4]
Output: [1,3,2,4]
Example 2:

Input: [1,4,2,3,5,6]
Output: [1,3,5,4,2,6]
Challenge
Do it in-place.

"""


class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        lens = len(nums)
        i, j = 0, lens - 1

        while i < j:
            while nums[i] % 2 != 0:
                i += 1
            while nums[j] % 2 == 0:
                j -= 1
            if i < j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j -= 1
        return nums
