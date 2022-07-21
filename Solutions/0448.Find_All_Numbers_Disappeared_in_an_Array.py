"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""

# hashset   O(n) O(n)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        nums_set = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                res.append(i)
        return res
    
    # if num not in nums  o(n)

    
"""
We use the sign of the index as the indicator. If one number never occur, 
we know the number corresponding to the idx will never be negative.
[4,3,1,3] -- > [-4,3,-1,-3], 2 is missing, so num[2-1] will never be changed to be negative 
"""
 class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])
        
        res =[]
        for idx, num in enumerate(nums):
            if num > 0:
                res.append(idx + 1)
        return res
