"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst = s.split(" ")
        if len(pattern) != len(lst):
            return False
        
        ch_to_str = collections.defaultdict(str)
        str_to_ch = collections.defaultdict(str)  #since we can not different ch map same string
        
        for i in range(len(lst)):
            ch = pattern[i]
            word = lst[i]
            if ch in ch_to_str:
                if ch_to_str[ch] != word or str_to_ch[word] != ch:
                    return False
            else:
                if word in str_to_ch:
                    return False
                ch_to_str[ch] = word
                str_to_ch[word] = ch
        return True
