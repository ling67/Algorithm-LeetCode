"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""

//python version: set
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        res = []
        for num in nums2:
            if num in nums1_set:
                res.append(num)
        return set(res)

//python: space O(1) time nlogn
 class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        lens1, lens2 = len(nums1), len(nums2)
        res = []
        i, j = 0, 0
        while i < lens1 and j < lens2:
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                while i + 1 < lens1 and nums1[i] == nums1[i + 1]:
                    i += 1
                while j + 1 < lens2 and nums2[j] == nums2[j + 1]:
                    j += 1
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
                
        return res
