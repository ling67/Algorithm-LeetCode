"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        hq = []
        backadd = deque()
        freqs = Counter(list(s))
        for val, freq in freqs.items():
            heappush(hq, (-freq, val))
        
        res = ""
        while len(hq) > 0:
            for _ in range(2):
                if len(hq) == 0 and len(backadd) > 0:   #要注意这里的判断，容易忘记
                    return ""
                
                if len(hq) > 0:
                    freq, val = heappop(hq)
                    freq = -freq
                    freq -= 1
                    if freq > 0:
                        backadd.append((-freq, val))
                    res += val
                    
                if len(hq) == 0 and len(backadd) == 0:
                    return res
        
            while len(backadd) > 0:
                heappush(hq, backadd.pop())
