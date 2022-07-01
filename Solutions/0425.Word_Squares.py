"""
Given an array of unique strings words, return all the word squares you can build from words. The same word from words can be used multiple times. You can return the answer in any order.

A sequence of strings forms a valid word square if the kth row and column read the same string, where 0 <= k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.
 

Example 1:

Input: words = ["area","lead","wall","lady","ball"]
Output: [["ball","area","lead","lady"],["wall","area","lead","lady"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input: words = ["abat","baba","atan","atal"]
Output: [["baba","abat","baba","atal"],["baba","abat","baba","atan"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
"""

"""
这题的核心方法是backtrack: 一个单词一个单词往上加，每次加一个单词都必须保证其prefix是之前所加单词的对应列组成的，
比如我们想加在第五行加单词，那这个单词必须满足prefix是前4行的第四列组成的。
知道了这个我们可以尝试套着模板来backtrack了.
Time complexity: It is tricky to calculate the exact number of operations in the backtracking algorithm. 
We know that the trace of the backtrack would form a n-ary tree. 
Therefore, the upper bound of the operations would be the total number of nodes in a full-blossom n-ary tree.
In our case, at any node of the trace, at maximum it could have 26 branches (i.e. 26 alphabet letters). 
Therefore, the maximum number of nodes in a 26-ary tree would be approximately 26^L.
O(K26^L*L), where K is the len(words), L is len(words[0]).
TODO:超时
"""

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def backtrack(curr_row, curr_square, res):
            if curr_row == N:
                res.append(curr_square.copy())
                return
            for next_row in valid_candidates(curr_row, curr_square):
                curr_square.append(next_row)
                backtrack(curr_row + 1, curr_square, res)
                curr_square.pop()
        
        def valid_candidates(curr_row, curr_square):
            res = []
            prefix = "".join(word[curr_row] for word in curr_square)
            for word in words:
                if word.startswith(prefix):     # this takes O(L) where L is the lens of the word, we can use a hash map to store the (prefix, word) pairs in advance. 
                    res.append(word)
            return res
            
        res = []
        N = len(words[0])
        for word in words:
            backtrack(1, [word], res)
        return res

       
"""
Brutal force takes O(K) time to query the word with a certain prefix, and it takes O(1) space.
Hashmap realized O(1) time to query the word with a certain prefix, but it takes way more space: O(KL).
Trie data structure provides a compact and yet still fast way to retrieve words with a given prefix.
It takes O(L) time to query the word, where L is the lens of the word, which is much faster than the Brutal force,
especially in real world, there could be millions of words in a book, but the lens of each words are within 20.
It takes O(KL) space in worst case, but in real world, it is much less than that, cuz lots of words share the same prefix.
"""
class TrieNode:
    
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.words = []
        

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curr_node = self.root
        for ch in word:
            curr_node = curr_node.child[ch]
            curr_node.words.append(word)

    def start_with(self, prefix):
        """
        return a list of words that starts with prefix
        """
        curr_node = self.root
        for ch in prefix:
            curr_node = curr_node.child[ch]
            
        return curr_node.words
    

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def backtrack(row, curr_comb):
            if row == n - 1:
                res.append(curr_comb.copy())
                return
            
            # find next_possible_words
            prefix = ""
            for i in range(row + 1):    # 我们想加在第五行加单词，那这个单词必须满足prefix是前4行的第四列组成的
                prefix += curr_comb[i][row + 1]
            for next_word in trie.start_with(prefix):
                curr_comb.append(next_word)
                backtrack(row + 1, curr_comb)
                curr_comb.pop()            
        
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        m, n = len(words), len(words[0])
        res = []
        for word in words:
            backtrack(0, [word])
        return res 
