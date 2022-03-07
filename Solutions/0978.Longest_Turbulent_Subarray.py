"""
Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.
 

Example 1:

Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
Example 2:

Input: arr = [4,8,12,16]
Output: 2
Example 3:

Input: arr = [100]
Output: 1
 

Constraints:

1 <= arr.length <= 4 * 104
0 <= arr[i] <= 109
"""


"""
1.状态定义 
dph[i] 从A[i]结尾的动荡子列的最大长度， A[i]是high
dp[i] 从A[i]结尾的动荡子列的最大长度， A[i]是low
2.求 return max{i=0,....,n-1}max(dph[i], dpl[i])
3.初始化 dph[0] = dpl[0] = 1
4.递推公式
if A[i] > A[i-1], dph[i] = dpl[i-1] + 1, dpl[i] = 1
if A[i] < A[i-1], dpl[i] = dph[i-1] + 1, dph[i] = 1
if A[i] = A[i-1], dph[i] = dpl[i] = 1
"""
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_lens = 1
        inc, dec = 1, 1  #inc 第0个元素结尾的上一个是递增的值  
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                inc = dec + 1
                dec = 1
            elif arr[i] < arr[i-1]:
                dec = inc + 1
                inc = 1
            else:
                inc = 1
                dec = 1
                
            max_lens = max(max_lens, inc, dec)
        
        return max_lens
