"""
You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.

A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make s balanced. If s is already balanced, return 0.

 

Example 1:

Input: s = "QWER"
Output: 0
Explanation: s is already balanced.
Example 2:

Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
Example 3:

Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER". 
 

Constraints:

n == s.length
4 <= n <= 105
n is a multiple of 4.
s contains only 'Q', 'W', 'E', and 'R'.
"""

"""
We want a minimum length of substring, which leads us to the solution of sliding window.
Specially this time we don't care the count of elements inside the window, we want to know the count outside the window.
This is because we can change the char inside the window whatever we want, so as long as outside the window,
all(count[Q],count[W],count[E],count[R]) <= n / 4 is satisfied, then we can make it balanced.
find the minimum substring so that outside the substring, condition all(four chars has frequency less than n//4) is satisfied.
第一种模板：find min subarray size for at least problem, 后面的指针去远离前面的指针
"""
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        counter = collections.Counter(s)    # keep track of the cnt outside the window
        min_size = n
        j = 0
        for i in range(len(s)):
            while j < n and not all(cnt <= n//4 for cnt in counter.values()):
                counter[s[j]] -= 1
                j += 1
            
            if all(cnt <= n//4 for cnt in counter.values()):
                min_size = min(min_size, j - i)
                
            counter[s[i]] += 1
            
        return min_size



