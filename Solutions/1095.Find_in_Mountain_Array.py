"""
(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.
 

Constraints:

3 <= mountain_arr.length() <= 104
0 <= target <= 109
0 <= mountain_arr.get(index) <= 109
"""

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        #先找到mountain
        l, r = 0, n - 1
        while l + 1 < r:
            m = l + (r - l) // 2
            if mountain_arr.get(m) > mountain_arr.get(m - 1):
                l = m
            else:
                r = m
        idx = l if mountain_arr.get(l) > mountain_arr.get(r) else r
        
        #左右边分别二分查找
        l = self.inc_binary_search(mountain_arr, target, 0, idx)
        r = self.dec_binary_search(mountain_arr, target, idx, n - 1)
        if l != -1:
            return l
        if r != -1:
            return r
        return -1
              
    def inc_binary_search(self, mountain_arr, target, l, r):
        while l + 1 < r:
            m = l + (r - l) // 2
            if mountain_arr.get(m) == target:
                return m
            elif mountain_arr.get(m) > target:
                r = m
            else:
                l = m
        if mountain_arr.get(l) == target:
            return l
        if mountain_arr.get(r) == target:
            return r
        return -1
            
    def dec_binary_search(self, mountain_arr, target, l, r):
        while l + 1 < r:
            m = l + (r - l) // 2
            if mountain_arr.get(m) == target:
                return m
            elif mountain_arr.get(m) > target:
                l = m
            else:
                r = m
        if mountain_arr.get(l) == target:
            return l
        if mountain_arr.get(r) == target:
            return r
        return -1


