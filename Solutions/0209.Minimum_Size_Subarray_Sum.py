"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105
"""

"""
method 1.i从[0, n] j[i,n] k连续K个sum so, the O(T) n^3
method 2.use sum to record the k arr[] sum   O(T) n^2
method 3.use prefix, also n^2
method 4.when arr[i] + .. arr[] > k, j stop forward, directly stop it.  O(T) n^2
method 5. ~~~当前方法 O(T) = n i and j will not back.
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lens = len(nums)
        minSize = float("inf")
        sums = 0
        j = 0
        for i in range(lens):
            while j < lens and sums < target:    # 满足条件 sums < s
                sums += nums[j]                  # 更新 j
                j += 1
            if sums >= target:                  # 更新 res if 满足条件
                minSize = min(minSize, j - i)  
                
            sums -= nums[i]                     # 更新 i
            
        return minSize if minSize != float("inf") else 0
      
      
"""
Follow up: 如果有负数怎么办？
那就不能用sliding window了，只能sliding window + mono deque. 详见862. Shortest Subarray with Sum at Least K 
"""  
    
"""
Follow up: can we solve in O(NlogN)?
Binary search O(nlogn).  二分答案: Each time, we use window size = mid to test if we have a subarray sum >= s. 
"""
      
