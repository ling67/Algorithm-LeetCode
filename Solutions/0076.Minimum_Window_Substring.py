Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
  
"""
time complexity, O(mn) m is the time to check is_valid()
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnter_t = Counter(t)    #store string t ch_num
        cnter = defaultdict(int)    #store string 
        min_len = float("inf")
        start, end = 0, 0  #record the index of min_len subarray.
        j = 0
        
        #套用九章的模板 for at least problems
        for i, ch in enumerate(s):
            while j < len(s) and not self.is_valid(cnter, cnter_t):
                cnter[s[j]] += 1
                j += 1
            
            if self.is_valid(cnter, cnter_t):
                if j - i < min_len:
                    min_len = j - i
                    start, end = i, j
            cnter[s[i]] -= 1
            
        return s[start:end]
    
    #check if all character cnter_t has already in cnter_s
    def is_valid(self, cnter_s, cnter_t):
        for ch, cnt in cnter_t.items():
            if cnt > cnter_s[ch]:
                return False
        return True
     
    
"""
this solution is O(N), instead of using self.allIncluded(sourceDict, targetDict) to check matched or not, 
we use a int missing to keep track of how many chars are still needed in order to match
also, in stead of using s[i:j] everytime we renew res, we use start, end to renew the idx, which reduce time from O(N) to O(1)
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnter_t = Counter(t)
        cnter = defaultdict(int)
        missing = len(cnter_t)    # how many ch are still missing in order to match t
        min_len = sys.maxsize
        start, end = 0, 0
        j = 0
        for i, ch in enumerate(s):
            while j < len(s) and missing > 0:
                cnter[s[j]] += 1
                if cnter[s[j]] == cnter_t[s[j]]:    # 正好加到满足条件了，就需要missing -= 1
                    missing -= 1
                j += 1
            
            if missing == 0:            # missing == 0 means matched
                if j - i < min_len:
                    min_len = j - i
                    start, end = i, j   # 也可以定义一个res, 用res = s[i:j]来更新结果，但是takes O(N)时间，所以用start, end来记录就可以了
            
            cnter[s[i]] -= 1
            if cnter[s[i]] == cnter_t[s[i]] - 1:    # 正好减到不满足条件了，就需要missing += 1
                missing += 1
                
        return s[start:end]    
