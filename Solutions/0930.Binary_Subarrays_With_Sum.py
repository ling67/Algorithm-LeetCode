"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
 

Constraints:

1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length
"""

"""
求和为goal的连续字串个数 = 和小于等于goal的连续字串个数 - 和小于等于goal-1的连续字串个数. 
注意nums[i] is either 0 or 1.所以当 nums[i] + ... nums[j] <= target时，cnt = j - i + 1
"""
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self._at_most(nums, goal) - self._at_most(nums, goal - 1)
    
    def _at_most(self, nums, target):
        cnt = 0
        sums = 0
        i = 0
        for j in range(len(nums)):
            sums = sums + nums[j]
            
            while i < j and sums > target:
                sums = sums - nums[i]
                i += 1
                
            if sums <= target:
                cnt += j - i + 1  #以j结尾连续字串的个数
                
        return cnt
                