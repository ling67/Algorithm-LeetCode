"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 500
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""

"""
本题要求最短路径，所以一定要用到BFS
又要求输出满足最短这个条件的所有路径，所以一定要用到DFS
本题是带层序遍历的BFS + 带backtracking的DFS
算法：如果需要从start位置出发做DFS，想要走最短路径去end位置，我们每一步都不能往远离end位置的节点走，因为如果往远离end位置的节点走的话就不会是最短路径了，
所以每一步都要往离end更近的节点走，那么问题来了，start位置开始有好几个节点可以走，怎样判断选哪一个节点走会往end更进一步呢？那就需要直到这些节点离end的距离，
求每个节点离某个end位置的距离问题，就需要用到带层序遍历的BFS，用一个hashmap记录每一个节点离end的距离
所以总结起来程序的顺序是：
1. 从end到start做BFS，记录每一个节点到end节点的距离，存入hashmap中 eg: distance["dog"] = 2
2. 从start到end做DFS，每走一步都必须确保end的distance越来越近。最后将路径都存入到res里
"""

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def backtrack(curr_node, curr_comb):
            if curr_node == endWord:
                res.append(curr_comb.copy())
                return
            for next_node in get_nextwords(curr_node):
                if next_node not in distance or distance[next_node] >= distance[curr_node]:
                    continue
                curr_comb.append(next_node)
                backtrack(next_node, curr_comb)
                curr_comb.pop()
            
        def get_nextwords(word):
            res = []
            for i, ch in enumerate(word):
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    if letter != ch:
                        candidate = word[:i] + letter + word[i+1:]
                        if candidate in wordset:
                            res.append(candidate)
            return res
        
        def bfs():     #from end to start update distance  # O(N), where N is number of words in word_set
            q = deque()
            visited = set()
            q.append(endWord)
            visited.add(endWord)
            dist = -1
            while len(q) > 0:
                dist += 1
                lens = len(q)
                for _ in range(lens):
                    curr_node = q.popleft()
                    distance[curr_node] = dist
                    if curr_node == beginWord:
                        return
                    for next_node in get_nextwords(curr_node):
                        if next_node not in visited:
                            q.append(next_node)
                            visited.add(next_node)
            
        
        wordset = set(wordList)
        wordset.add(beginWord)
        if endWord not in wordset:
            return []
        
        distance = defaultdict(int)    # node --> distance of this node to end node
        bfs()
        
        res = []
        backtrack(beginWord, [beginWord])
        return res
        
        
