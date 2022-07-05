"""
Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

 

Example 1:

Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:

Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 30
words[i] consists of lowercase English letters.
"""
"""
首先insert所有的word进Trie, 然后再将words list按照长度反向sort, 
最后遍历words, 如果发现有一个word can_be_built, then return the word.
需要在Trie class里面写一个can_be_built(word)函数
"""

class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.isEnd = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.add(word)
        
    def add(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = TrieNode()
            curr = curr.child[ch]
        curr.isEnd = True
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie(words)
        words.sort(key = lambda x:(-len(x), x))
        for word in words:
            curr = trie.root
            for ch in word:
                curr = curr.child[ch]
                if not curr.isEnd:
                    break
            if curr.isEnd:
                return word
        return ""

