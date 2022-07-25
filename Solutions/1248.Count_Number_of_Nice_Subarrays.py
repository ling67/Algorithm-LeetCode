"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMostK(k):
            res = i = 0
            for j in range(len(nums)):
                k -= nums[j] % 2
                while k < 0:
                    k += nums[i] % 2
                    i += 1
                res += j - i + 1        #以j结尾的,小于等于k的个数
            return res
        return atMostK(k) - atMostK(k - 1)
        
    

"""
exactly(K) = atMost(K) - atMost(K-1); 第二种模板：find max subarray size for at most problem. 写法是while loop里让前面的指针去追后面的指针
"""
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self._at_most(nums, k) - self._at_most(nums, k - 1)
        
    def _at_most(self, nums, k):
        odd_cnt = 0
        i = 0
        res = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 1:
                odd_cnt += 1
                
            while i <= j and odd_cnt > k:
                if nums[i] % 2 != 0:
                    odd_cnt -= 1
                i += 1
            
            if odd_cnt <= k:
                res += j - i + 1 
                j += 1
                
        return res
            
