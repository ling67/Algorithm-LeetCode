"""
Given a string s, return all the palindromic permutations (without duplicates) of it.

You may return the answer in any order. If s has no palindromic permutation, return an empty list.

 

Example 1:

Input: s = "aabb"
Output: ["abba","baab"]
Example 2:

Input: s = "abc"
Output: []
 

Constraints:

1 <= s.length <= 16
s consists of only lowercase English letters.
"""

"""
After examing 266, we can get the following solution:
say if we have a string "aabbcc", we only need to find all the permutations for "abc", then return all the permutations + permutation[::-1]
in this way the time complexity is O((N/2)!)
"""    


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:       
        def backtrack(curr_idx, curr_comb):
            if len(curr_comb) == len(even_chars):
                res.append("".join(curr_comb.copy()))
                return
            for next_idx in range(len(even_chars)):
                if next_idx in visited:
                    continue
                if next_idx > 0 and even_chars[next_idx] == even_chars[next_idx-1] and next_idx - 1 not in visited:
                    continue            # 去重
                visited.add(next_idx)
                curr_comb.append(even_chars[next_idx])
                backtrack(next_idx, curr_comb)
                visited.remove(next_idx)
                curr_comb.pop()
        
        # step 1: pre-cessing: "aaabbbbcc" --> "abbc"
        res = []
        counter = collections.Counter(s)
        cnt = 0             # cnt of ch that appear only once
        even_chars = ""     # stores the chars that appear even times 
        only_once = ""      # store the char that appear only once
        for ch, freq in counter.items():
            if freq % 2 == 1:
                even_chars += ch * (freq // 2)      # "aaabb" --> "ab"
                only_once = ch
                cnt += 1
            else:
                even_chars += ch * (freq // 2)       # "aaaabb" --> "aab"
        if cnt > 1:
            return res
        
        # step 2: bachtrack for "abbc" and find all it's permutations
        even_chars = sorted(even_chars)     # 去重第一步 - sort
        visited = set()
        backtrack(0, [])
        
        # step 3: re-construct the pandlindrome using the generated permutations
        ans = []
        for comb in res:
            ans.append(comb + only_once + comb[::-1])
        return ans      


