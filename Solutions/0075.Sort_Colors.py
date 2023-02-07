/*
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.


Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

*/

"""
version 1 : 3 pointer
O(n)
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p1, p2 = 0, 0, len(nums) - 1
        while p1 <= p2:
            if nums[p1] == 0:
                nums[p0], nums[p1] = nums[p1], nums[p0]
                p0 += 1
                p1 += 1
            elif nums[p1] == 2:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1
            else:
                p1 += 1
            


//version 2：2 times partition
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)
        i, j = 0, lens - 1
        while i <= j:
            while i <= j and nums[i] == 0:
                i += 1
            while i <= j and nums[j] > 0:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
        
        i, j = i, lens - 1
        while i <= j:
            while i <= j and nums[i] == 1:
                i += 1
            while i <= j and nums[j] == 2:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
        
            

