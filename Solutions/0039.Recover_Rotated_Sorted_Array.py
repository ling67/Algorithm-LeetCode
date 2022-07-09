/*
Description
Given a rotated sorted array, return it to sorted array in-place.（Ascending）

Wechat reply the 【39】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

What is rotated array?

For example, the orginal array is [1,2,3,4], The rotated array of it can be [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]
Example
Example 1:

Input:

array = [4,5,1,2,3]
Output:

[1,2,3,4,5]
Explanation:

Restore the rotated sorted array.

Example 2:

Input:

array = [6,8,9,1,2]
Output:

[1,2,6,8,9]
Explanation:

Restore the rotated sorted array.
*/

from typing import (
    List,
)

class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        if len(nums) == 1: return nums
        if nums[0] < nums[-1]: return nums
        
        min_idx = self._find_min_idx(nums)
        self._swap(nums, 0, min_idx - 1)    # 三步反转法: reverse the left part
        self._swap(nums, min_idx, len(nums) - 1)    # reverse the right part
        self._swap(nums, 0, len(nums) - 1)  # reverse for the 3rd time
        
    def _find_min_idx(self, nums):  # 注意如果有重复的元素就要跟nums[end]比较
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < nums[end]:   # 跟nums[end]比较
                end = mid
            elif nums[mid] > nums[end]:
                start = mid
            else:       # in case there is duplicates, we decreament end by 1
                end -= 1
        return start if nums[start] <= nums[end] else end
    
    def _swap(self, nums, start, end):
        i, j = start, end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


/******************************************java version********************************************/           

public class Solution {
    /**
     * @param nums: An integer array
     * @return: nothing
     */
    public void recoverRotatedSortedArray(List<Integer> nums) {
        // write your code here
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums.get(i) > nums.get(i + 1)) {
                reverse(nums, 0, i);
                reverse(nums, i + 1, nums.size() - 1);
                reverse(nums, 0, nums.size() - 1);
            }
        }
    }

    private void reverse(List<Integer> nums, int start, int end) {
        for (int i = start, j = end; i < j; i++, j--) {
            int temp = nums.get(i);
            nums.set(i, nums.get(j));
            nums.set(j, temp);
        }
    }
}



