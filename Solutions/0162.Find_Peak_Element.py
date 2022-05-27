/*
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
*/

/**
we should consider 4 diff situation 
nums[0] > nums[1] nums[n] > nums[n-1]// nums[n] < nums[n-1] we consider 0 is the peak index
nums[0] < nums[1] nums[n] > nums[n-1] n is the peak index
nums[0] < nums[1] nums[n] < nums[n-1] keep consider 3 situation
**/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] < nums[mid] < nums[mid+1]:
                start = mid
            else:
                end = mid
        return start if nums[start] > nums[end] else end
            

class Solution {
    public int findPeakElement(int[] nums) {
        if (nums == null || nums.length == 0 || nums.length == 1){
            return 0;
        }
        
        int n = nums.length;
        
        if (nums[0] > nums[1]) return 0;
        if (nums[n-1] > nums[n-2]) return n-1;
        
        int start = 0, end = n-1;
        while (start + 1 < end){
            
            if (nums[start] > nums[start+1]) {
                return start;
            }
            if (nums[end] >  nums[end-1]) {
                return end;
            }
            
            int mid = start + (end - start) / 2;
            
            if((nums[mid-1] < nums[mid]) && nums[mid] > nums[mid+1]) {
                return mid;
            } else if ((nums[mid-1] < nums[mid]) && (nums[mid] < nums[mid+1])) {
                start = mid;
            } else {
                end = mid;
            }
        }
        
        if (nums[start] > nums[end]) {
            return start;
        } else{
            return end;
        }
        
    }
}
