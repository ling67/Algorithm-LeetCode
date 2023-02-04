/*
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []

*/


//Solution 1: two pointer
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        
        nums.sort()   #step 1:sort the arr
        
        res = []
        lens = len(nums)
        
        #setp 2: for 虚幻nums[i],然后双指针解决twosum问题
        for i in range(lens - 2):
            if nums[i] > 0:    #优化点
                break
            if i > 0 and nums[i] == nums[i -1]:   # 注意点一：对i去重
                continue
                
            left, right = i + 1, lens - 1    # 注意点二：left 和 right 的初始值
            while left < right:
                threeSum = nums[left] + nums[right] + nums[i]
                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]: # 注意点三：对 left 和 right 去重!!!!!!!
                        left += 1
                    while left < right and nums[right] == nums[right+1]: # 注意点三：对 left 和 right 去重!!!!!!!
                        right -= 1
        return res
 
 //Solution 2: hashset
 
 class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:    #i 去重
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:   #j 去重
                    j += 1
            seen.add(nums[j])
            j += 1
                        

