"""
Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there is not one, return 0 instead.

 

Example 1:

Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
 

Constraints:

1 <= nums.length <= 2 * 105
-104 <= nums[i] <= 104
-109 <= k <= 109
"""

#由于arr中有正数有负数，所以不能用sliding window, 只能用prefix sum + hashmap

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        max_lens = 0
        pre_sum = 0
        pre_sum_dict = collections.defaultdict(int)  #存储pre_sum, index
        pre_sum_dict[0] = -1
        for i, num in enumerate(nums):
            pre_sum += num
            
            if pre_sum - k in pre_sum_dict:
                max_lens = max(max_lens, i - pre_sum_dict[pre_sum - k])
            
            if pre_sum not in pre_sum_dict:   # 只有当pre_sum not in pre_sum_dict我们才更新pre_sum_dict[pre_sum]，
                pre_sum_dict[pre_sum] = i       # 这是为了保证idx尽可能小，这样max_lens才能尽可能大
        
        return max_lens
