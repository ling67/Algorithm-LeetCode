"""
A valid encoding of an array of words is any reference string s and array of indices indices such that:

words.length == indices.length
The reference string s ends with the '#' character.
For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.

 

Example 1:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"
Example 2:

Input: words = ["t"]
Output: 2
Explanation: A valid encoding would be s = "t#" and indices = [0].
 

Constraints:

1 <= words.length <= 2000
1 <= words[i].length <= 7
words[i] consists of only lowercase letters.
"""

#method 1: string  Time O(NlogN)  space: O(Length of All words)
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key = lambda x: -len(x))  
        res = ""
        for s in words:
            if (s + "#") not in res:
                res += (s + "#")
        return len(res)
        
#method 2: trie

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def is_suffix(self, word):  # return True if word is a suffix of the Trie
        curr = self.root
        for ch in word[::-1]:   # 注意要search in the reverse order
            if ch not in curr.child:
                return False
            curr = curr.child[ch]
        return True
    
    def insert(self, word):
        curr = self.root
        for ch in word[::-1]:    # 注意要insert in the reverse order才能与上面的is_suffix对应
            curr = curr.child[ch]
            

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key = lambda x: -len(x))     # 注意要sort in the reversed order
                                                #这样才能search for suffix
        trie = Trie()
        
        res = []
        for word in words:
            if not trie.is_suffix(word):
                trie.insert(word)
                res.append(word + "#")
                
        return sum(len(word) for word in res)
    
