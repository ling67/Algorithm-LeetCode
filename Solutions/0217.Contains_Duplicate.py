"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

# Solution 1: use counter solve it
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ch_to_freq = Counter(nums)
        for ch, freq in ch_to_freq.items():
            if freq  > 1:
                return True
        return False
      
# Solution 2: use set solve it
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            
            numSet.add(num)
            
        return False
      
# Solution 3: use bucket sort: list index out of range      
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums or len(nums) <= 1:
            return False
        
        idx = [False for _ in range(max(nums) + 1)]
        for num in nums:
            if idx[num]:
                return True
            else:
                idx[num] = True
        return False      
      
