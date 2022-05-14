"""
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1
 

Constraints:

1 <= n <= 231 - 1
"""

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        BOUND =  2147483647
        arr = []
        while n // 10 != 0:
            arr.append(n % 10)
            n //= 10
        arr.append(n % 10)
        
        i, j = 0, len(arr)-1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        
        for i in range(len(arr) - 1, 0, -1):
            if arr[i-1] < arr[i]:
                break

        left_pos = i-1
        dis = float('inf')
        right_pos = left_pos
        for j in range(i, len(arr)):
            if arr[j] > arr[left_pos] and arr[j] - arr[left_pos] <= dis:
                right_pos = j
                dis = arr[j] - arr[left_pos]
        
        if right_pos != left_pos:
            arr[left_pos], arr[right_pos] = arr[right_pos], arr[left_pos]
            i, j = left_pos + 1, len(arr) - 1
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
                
            res = 0
            for num in arr:
                if 10*res + num <= BOUND:
                    res = 10 * res + num
                else:
                    return -1
            return res
        
        else:
            return -1
