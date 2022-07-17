"""
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
nums[i] - nums[j] == k
Notice that |val| denotes the absolute value of val.

 

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:

Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
 

Constraints:

1 <= nums.length <= 104
-107 <= nums[i] <= 107
0 <= k <= 107
"""

#Solution 1: 双指针，注意去重
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        i, j = 0, 1
        cnt = 0
        
        while i < n and j < n:
            if nums[j] - nums[i] > k:
                i += 1
            elif nums[j] - nums[i] < k or i == j:    #易错点 i == j时没考虑
                j += 1
            else:
                cnt += 1
                i += 1
                j += 1
                #注意去重：
                while i < len(nums) and nums[i] == nums[i-1]:   #易错点 去重
                    i += 1
                while j < len(nums) and nums[j] == nums[j-1]:   #易错点 去重
                    j += 1
        return cnt

      
#solution 2: hash map
# https://www.bilibili.com/video/BV1MV41127o1?spm_id_from=333.999.0.0

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ct = Counter(nums)
        res = 0
        if k == 0:
            for v in ct.values():
                res += v > 1
        else:
            for n in ct:
                res += n + k in ct
        return res
    
