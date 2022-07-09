"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
"""

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        inc_cnt = 0
        dec_cnt = 0
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return False
            elif arr[i] > arr[i-1]:
                if dec_cnt > 0:
                    return False
                inc_cnt += 1
            elif arr[i] < arr[i-1]:
                if inc_cnt == 0:
                    return False
                dec_cnt += 1
                
        return inc_cnt > 0 and dec_cnt > 0
        
