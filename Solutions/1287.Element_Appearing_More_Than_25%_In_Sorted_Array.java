/*
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 105

*/


class Solution {
    public int findSpecialInteger(int[] arr) {
        int n = arr.length;
        int nums1 = arr[n / 4];
        int nums2 = arr[n / 2];
        int nums3 = arr[3 * n / 4];
        
        int len1 = endIndex(arr, nums1) - firstIndex(arr, nums1); 
        if (len1 >= n/4) {
            return nums1;
        }
        
        int len2 = endIndex(arr, nums2) - firstIndex(arr, nums2); 
        if (len2 > n/4) {
            return nums2;
        }
        
        return nums3;
    }
    
    private int firstIndex(int[] arr, int target) {
        int start = 0, end = arr.length - 1;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (arr[mid] >= target) {
                end = mid;
            } else {
                start = mid;
            }
        }
        return arr[start] == target ? start : end;
    }
    
    private int endIndex(int[] arr, int target) {
        int start = 0, end = arr.length - 1;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (arr[mid] <= target) {
                start = mid;
            } else {
                end = mid;
            }
        }
        return arr[end] == target ? end : start;
    }
}
