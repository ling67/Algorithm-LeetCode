"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

"""for循环nums[i]，然后for循环nums[j]，在用双指针解决twoSum问题 O(N^3), O(1)"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        
        nums.sort()
        
        res = []
        lens = len(nums)
        
        for i in range(lens-3):
            if i > 0 and nums[i] == nums[i-1]:  #去重
                continue
            
            if nums[i] * 4 > target:  #优化
                break
                
            for j in range(i+1, lens-2):
                # 注意这里给j去重不能从j>=1开始，因为要至少让j先取上第一个值i+1之后才能与前一个数比较！不然[0,0,0,], 0就通不过了。
                
                if j > i + 1 and nums[j] == nums[j-1]:  
                    continue
                    
                if nums[i] + nums[j] * 3 > target: #优化
                    break
                
                left, right = j + 1, lens - 1
                while left < right:
                    fourSum = nums[i] + nums[j] + nums[left] + nums[right]
                    if fourSum > target:
                        right -= 1
                    elif fourSum < target:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:  #去重
                            left += 1 
                        while left < right and nums[right] == nums[right + 1]:  #去重
                            right -= 1
        return res
