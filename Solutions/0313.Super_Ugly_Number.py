

"""
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        added = set()
        added.add(1)
        hq = [1]
        for _ in range(n):
            curr_min = heappop(hq)
            for prime in primes:
                if prime * curr_min not in added:
                    heappush(hq, prime * curr_min)
                    added.add(prime * curr_min)
                    
        return curr_min
"""  

A super ugly number is a positive integer whose prime factors are in the array primes.

Given an integer n and an array of integers primes, return the nth super ugly number.

The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

 

Example 1:

Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 super ugly numbers given primes = [2,7,13,19].
Example 2:

Input: n = 1, primes = [2,3,5]
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are in the array primes = [2,3,5].
 

Constraints:

1 <= n <= 106
1 <= primes.length <= 100
2 <= primes[i] <= 1000
primes[i] is guaranteed to be a prime number.
All the values of primes are unique and sorted in ascending order.


# Solution1:heap solution: O(nlog(kn)) where k is the lens of primes list

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        added = set()
        added.add(1)
        hq = [1]
        for _ in range(n):
            curr_min = heappop(hq)
            for prime in primes:
                if prime * curr_min not in added:
                    heappush(hq, prime * curr_min)
                    added.add(prime * curr_min)
                    
        return curr_min

      
# Solution2:DP 

# https://leetcode-cn.com/problems/super-ugly-number/solution/chao-ji-chou-shu-by-leetcode-solution-uzff/
    
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * (n + 1)
        m = len(primes)
        pointers = [0] * m
        nums = [1] * m
        
        for i in range(1, n + 1):
            min_num = min(nums)
            dp[i] = min_num
            for j in range(m):
                if nums[j] == min_num:
                    pointers[j] += 1
                    nums[j] = dp[pointers[j]] * primes[j]
        return dp[n]
    
    
    
