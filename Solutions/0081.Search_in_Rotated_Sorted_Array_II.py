/*
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
*/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end = 0, len(nums) - 1
            
        while end > 0 and nums[end] == nums[0]:
            end -= 1
            
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target or nums[start] == target or nums[end] == target:
                return True
            if nums[start] <= nums[mid]:
                if nums[start] < target < nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] < target < nums[end]:
                    start = mid
                else:
                    end = mid
        return True if (nums[start] == target or nums[end] == target) else False
       

class Solution {
    public boolean search(int[] nums, int target) {
        
        int n = nums.length;
        int start = 0, end = n - 1;
        //把相同的元素删除
        while ((end > 0) && nums[end] == nums[0]) {
            end--;
        }
        
        while (start + 1 < end) {
            
            int mid = start + (end - start) / 2;
            if (nums[mid] == target || nums[start] == target || nums[end] == target) {
                return true;
            } 
            
            if (nums[start] <= nums[mid]) {
                if (nums[start] < target && target < nums[mid]) {
                    end = mid;
                } else {
                    start = mid;
                }
            } else {
                if (nums[mid] < target && target < nums[end]) {
                    start = mid;
                } else {
                    end = mid;
                }
            }
        }
        return (nums[start] == target || nums[end] == target);
    }
}
