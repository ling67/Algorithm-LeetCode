"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.
"""

#Solution 1: counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        ch_freq = Counter(nums)
        for ch, freq in ch_freq.items():
            if freq == 2:
                res.append(ch)
        return res
      
#Solution 2: set memery O(n)

      
#Solution 3: 因为每个数的大小小于等于数组长度，可以用数对应下标的数的正负号进行标记，把遇到的数对应的数变成负，如果已经是负数了，则证明已经出现过  (推荐)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                res.append(idx + 1)
            else:
                nums[idx] *= -1
        return res
      
