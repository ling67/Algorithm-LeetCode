"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
"""
#方法一：heapQ

#方法二：binary search

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        hq = []
        res = []
        for num in arr:
            hq.append((abs(num - x), num))
        heapify(hq)
        for _ in range(k):
            res.append(heappop(hq)[1])
        res.sort()
        return res
