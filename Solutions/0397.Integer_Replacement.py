"""
Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.

 

Example 1:

Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1
Example 2:

Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1
Example 3:

Input: n = 4
Output: 2
 

Constraints:

1 <= n <= 231 - 1
"""


class Solution:
    def integerReplacement(self, n: int) -> int:
        q = collections.deque()
        q.append(n)
        visited = set()
        visited.add(n)
        
        layer = -1
        while q:
            size = len(q)
            layer += 1
            for _ in range(size):
                curr = q.popleft()
                if curr == 1:
                    return layer
                if curr % 2 == 0:
                    next_num = curr / 2
                    if next_num not in visited:
                        q.append(next_num)
                        visited.add(next_num)
                else:
                    for next_num in [curr - 1, curr + 1]:
                        if next_num not in visited:
                            q.append(next_num)
                            visited.add(next_num)
                
