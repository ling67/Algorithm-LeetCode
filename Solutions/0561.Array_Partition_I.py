"""
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

 

Example 1:

Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
Example 2:

Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
 

Constraints:

1 <= n <= 104
nums.length == 2 * n
-104 <= nums[i] <= 104
"""

#内置sort
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[i] for i in range(0, len(nums), 2))

#counting sort
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        K = 10000
        element_to_count = [0] * (2 * K + 1)
        for element in nums:
            element_to_count[element + K] += 1
            
        max_sum = 0
        is_even_index = True
        for element in range(2 * K + 1):
            while element_to_count[element] > 0:
                if is_even_index:
                    max_sum += element - K
                is_even_index = not is_even_index
                element_to_count[element] -= 1
        return max_sum
