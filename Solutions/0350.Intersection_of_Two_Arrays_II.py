"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""

"""
Approach 1: hashmap to store the frequency of each num.
O(min(m, n))
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_cnt = Counter(nums1)
        res = []
        for num in nums2:
            if num in num_to_cnt:
                res.append(num)
                num_to_cnt[num] -= 1
                if num_to_cnt[num] == 0:
                    del num_to_cnt[num]
        return res

"""
Facebook follow ups:
follow up 1: What if the given array is already sorted? How would you optimize your algorithm?
"""
"""
Approach 2 - O(m+n), O(1)
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        i, j = 0, 0
        len1, len2 = len(nums1), len(nums2)
        res = []
        while i < len1 and j < len2:
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return res
        

