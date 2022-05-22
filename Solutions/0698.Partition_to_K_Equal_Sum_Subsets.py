"""
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false
 

Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].
"""

"""
套backtrack模板即可，backtrack里面需要传入(curr_sum, curr_idx, curr_cnt).
结束条件是已有curr_cnt=k段满足条件了. 
Time complexity: we basically iterate over nums and for each element either use it or drop it, 
which is O(2^n). We are doing the same for each subset. Total subsets are k. 
So Time Complexity becomes O(k*(2^n))
"""
"""
这题要求把一个arr分成k个subsets, 每个subsets的sum都是target. 这是一个NP-complete problem, 只能backtrack - O(k*2^n).
与之类似的，要求把一个arr分成k个subarray, 每个subarray的sum都是target. 这是一个dp问题 - O(k*n*target)
超时了
"""

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:       
        def backtrack(curr_idx, curr_sum, curr_cnt):
            if curr_cnt == k:    # 为什么只需要curr_cnt=k就return True了？ 
                return True      # 这是因为target = sum(nums) // k, 所以如果k个subsets满足加起来等于target，
                                 # 那说明nums里面的所有num都已经用上了
            if curr_sum > target:
                return False
            elif curr_sum == target:                # 拼出一段之后，从头开始去拼下一段
                if backtrack(-1, 0, curr_cnt + 1):  # 注意这里要从 -1 开始搜索
                    return True
            elif curr_sum < target:
                for next_idx in range(curr_idx + 1, len(nums)):     # 去后面找数来拼凑 - O(2^N)
                    if next_idx not in visited:
                        visited.add(next_idx)
                        if backtrack(next_idx, curr_sum + nums[next_idx], curr_cnt):
                            return True
                        visited.remove(next_idx)
            
            return False
        
        
        if sum(nums) % k != 0:
            return False
        target = sum(nums) // k
        
        visited = set()     # 因为拼出一段之后，需要从"头!!!!"开始去拼下一段，所以需要visited标记
        return backtrack(-1, 0, 0)
