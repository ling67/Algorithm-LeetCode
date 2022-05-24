"""
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000
 

Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?
"""

"""
backtrack结束条件：curr_sum == target
constraints on next_candidate: no constraint, any num in nums can be added
arguments to pass in backtrack function: curr_sum
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def backtrack(curr_sum):
            if curr_sum == target:
                self.res += 1
                return
            
            if curr_sum > target:
                return
            
            for next_num in nums:      # (1,3)和(3,1)都可以算到答案里，所以是Permutation problem, next_idx 从0开始
                backtrack(curr_sum + next_num)
                
        self.res = 0
        backtrack(0)
        return self.res
      
 """
1.define state dp[i]=how many ways to combine to number i
2.we want get dp[target]
3.initialize dp[0] = 1
4.dp[i] = dp[i-nums[0]] + dp[i-nums[1]]
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        lens = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for m in range(target + 1):
            for num in nums:
                if m >= num:
                    dp[m] += dp[m - num]
        
        return dp[target]
