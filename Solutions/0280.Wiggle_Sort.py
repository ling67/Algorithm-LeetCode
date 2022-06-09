"""
Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

You may assume the input array always has a valid answer.

 

Example 1:

Input: nums = [3,5,2,1,6,4]
Output: [3,5,1,6,2,4]
Explanation: [1,6,2,5,3,4] is also accepted.
Example 2:

Input: nums = [6,6,5,6,3,8]
Output: [6,6,5,6,3,8]
 

Constraints:

1 <= nums.length <= 5 * 104
0 <= nums[i] <= 104
It is guaranteed that there will be an answer for the given input nums.
 

Follow up: Could you solve the problem in O(n) time complexity?
"""


"""
从左到右扫一遍，不满足条件的交换就好了。
需要证明的是，当我们 交换了 nums[i] 和 nums[i - 1] 以后：
... nums[i - 2], nums[i], nums[i - 1]
nums[i - 2] 不会和 nums[i] 形成逆序（不满足条件的大小关系）
那假如原来是 nums[i - 2] <= nums[i - 1]，那么 nums[i - 1] 和 nums[i] 交换的条件是，nums[i - 1] <= nums[i]。
那我们就推导出此时 nums[i] >= nums[i - 2]，因此交换之后，不会让 nums[i] 和 nums[i - 2] 的大小关系出现变化。
反过来如果 nums[i - 2] >= nums[i - 1] 的情况同理。
"""
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        preShouldBeLessThanCur = True
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i] and preShouldBeLessThanCur or (nums[i - 1] <= nums[i] and not preShouldBeLessThanCur):
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
            preShouldBeLessThanCur = not preShouldBeLessThanCur
