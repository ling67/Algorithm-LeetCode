"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = collections.defaultdict(list)
        for word in strs:
            char_word = list(word)   #变成char[]
            char_word.sort()    #容易忘记排序
            word_dict[tuple(char_word)].append(word)    #hashmap存进去
            
        return word_dict.values()   #返回hashmap的值   [v for k, v in mapping.items()] 
