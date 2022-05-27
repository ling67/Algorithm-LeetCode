/*
Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

 

Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1

*/
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arr[mid-1] < arr[mid] and arr[mid+1] < arr[mid]:
                return mid
            elif arr[mid-1] < arr[mid] < arr[mid+1]:
                start = mid
            else:
                end = mid
        return start if arr[start] > arr[end] else end
        
        
class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int start = 0, end = arr.length - 1;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (arr[mid - 1] < arr[mid] && arr[mid] > arr[mid + 1]) {
                return mid;
            } else if (arr[mid - 1] < arr[mid] && arr[mid] < arr[mid + 1]) {
                start = mid;
            } else {
                end = mid;
            }
        }
        return arr[start] > arr[end] ? start : end;
    }
}
