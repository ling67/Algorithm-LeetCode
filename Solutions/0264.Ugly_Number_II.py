"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 

Constraints:

1 <= n <= 1690
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        added = set()    #容易忘记
        added.add(1)
        hq = [1]
        for _ in range(n):
            min_num = heappop(hq)
            for k in [2,3,5]:
                if min_num * k not in added:
                    heappush(hq, min_num * k)
                    added.add(min_num * k)
                    
        return min_num
