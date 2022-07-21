"""
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
Example 2:

Input: nums = [1,10,2,9]
Output: 16
 

Constraints:

n == nums.length
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
"""
先看只有两个点A和B的情况,
______A_____P_______B_______
可以发现，只要选择位置P在 [A, B] 区间内，不管在哪，距离之和都是A和B之间的距离，如果P不在 [A, B] 之间，那么距离之和就会大于A和B之间的距离，
现在再加两个点C和D：
______C_____A_____P_______B______D______
通过分析可以得出，P点的最佳位置就是在 [A, B] 区间内.
如果加入很多点，我们选择最佳的点是最小区间[A, B]之间的点，也就是[median - 1, median + 1]之间选一个点，
这就是为什么我们需要选择median了
"""

"""
solution 1: find median by sorting
"""
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = self._find_median(nums)
        return sum(abs(num - median) for num in nums)
    
    def _find_median(self, nums):
        nums.sort()
        return nums[len(nums)//2]
        
        
"""
solution 2: find meddian by quick select(kth largest element) - O(N)
模板一个星期不看就不记得了
"""
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = self._find_median(nums)
        return sum(abs(num - median) for num in nums)
    
    def _find_median(self, nums):
        return self._quick_select(nums, 0, len(nums) - 1, len(nums) // 2)
        
    def _quick_select(self, nums, start, end, k):
        if start >= end:
            return nums[k]
        
        pivot = nums[(start + end) // 2]
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        if k <= right:
            return self._quick_select(nums, start, right, k)
        elif k >= left:
            return self._quick_select(nums, left, end, k)
        
        return nums[k]
