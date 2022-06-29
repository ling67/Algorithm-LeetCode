"""
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.

 

Example 1:

Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 15
"""

"""
For permutation problem, the 1st idx has N choices of number, 2nd has n-1 choices.
so time complexity id O(solutions = N!). 
For constrained permutation problem, the time complexity is O(valid solutions)
"""

class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(curr_comb):
            if len(curr_comb) == n:
                self.res += 1
                return
            
            for num in range(1, n + 1):
                if num in visited:
                    continue
                if (num % (len(curr_comb) + 1)) == 0 or ((len(curr_comb) + 1) % num) == 0:
                    curr_comb.append(num)
                    visited.add(num)
                    backtrack(curr_comb)
                    visited.remove(num)
                    curr_comb.pop()
                    
        self.res = 0
        visited = set()
        backtrack([])
        return self.res
