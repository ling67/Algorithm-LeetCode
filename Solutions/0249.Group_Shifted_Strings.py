"""
We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

 

Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
Example 2:

Input: strings = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.
"""

#the key of the hashmap is a tuple of the list [ord(ch)-ord(first_ch) for ch in each string]
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        str_dict = collections.defaultdict(list)
        for s in strings:
            ch_lst = []
            for ch in s:
                ch_lst.append((ord(ch) - ord(s[0])) % 26)    #注意容易忘记：ZA会形成环，所以take mod of 26
            str_dict[tuple(ch_lst)].append(s)
            
        return str_dict.values()
