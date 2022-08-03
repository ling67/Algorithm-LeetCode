"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

"""
将0都变成-1，题目就变成了max subarray size with sum == 0.
由于arr中有正数有负数，所以不能用sliding window, 只能用prefix sum + hashmap
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums = [-1 if nums[i] == 0 else 1 for i in range(len(nums))]
        
        max_lens = 0
        pre_sum = 0
        pre_sum_dict = collections.defaultdict(int)
        pre_sum_dict[0] = -1
        
        for i, num in enumerate(nums):
            pre_sum += num
            if pre_sum in pre_sum_dict:
                max_lens = max(max_lens, i - pre_sum_dict[pre_sum])
            else:
                pre_sum_dict[pre_sum] = i
                
        return max_lens
            
            
