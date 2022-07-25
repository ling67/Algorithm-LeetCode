"""
Given a string s and an integer k, return the number of substrings in s of length k with no repeated characters.

 

Example 1:

Input: s = "havefunonleetcode", k = 5
Output: 6
Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: s = "home", k = 5
Output: 0
Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
1 <= k <= 104
"""

"""
Brutal force / sliding window with fixed length: O(26N)
"""
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        freq = collections.defaultdict(int)
        for ch in S[:K]:
            freq[ch] += 1
            
        res = 0
        if len(freq) == K and max(val for val in freq.values()) == 1:
            res += 1 
        
        for i in range(K, len(S)):
            freq[S[i]] += 1
                
            freq[S[i-K]] -= 1
            if freq[S[i-K]] == 0:
                del freq[S[i-K]]
                
            if len(freq) == K and max(val for val in freq.values()) == 1:
                res += 1
                
        return res

# Solution 2: sliding window, get max 
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        cnt = 0
        ch_to_freq = collections.defaultdict(int)
        i = 0
        for j, ch in enumerate(s):
            ch_to_freq[ch] += 1
            while i <= j and (j - i + 1 > len(ch_to_freq) or len(ch_to_freq) > k):
                ch_to_freq[s[i]] -= 1
                if ch_to_freq[s[i]] == 0:
                    del ch_to_freq[s[i]]
                i += 1
            
            if len(ch_to_freq) == j - i + 1 == k:
                cnt += 1
        return cnt
