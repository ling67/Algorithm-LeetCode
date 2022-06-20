"""
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

 

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
"""

"""理解题目关键在于理解words are sorted lexicographically的意思。举个例子: ["wrt","wrf"]这个例子中，"wrt"排在"wrf"前面，
这是因为在外星文中"t"排在"f"的前面。想想我们地球文中"abc"排在"abd"前面是因为"c"排在"d"前面，或者说ord("c") < ord("d")。
在外星文中，他们认为ord("t") < ord("f")。
理解了这个，我们进行比较的时候只需要比较word[i]与word[i+1]即可得到inDegree的关系以及neighbors的关系了。
"""

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # 1. construct the adjacency list representation
        # 2. get the in_degrees information
        graph = collections.defaultdict(list)
        in_degrees = collections.defaultdict(int)
        for word in words:
            for ch in word:
                in_degrees[ch] = 0
                
        for i in range(len(words)-1):
            prev, curr = words[i], words[i+1]
            minLen = min(len(prev), len(curr))
            if len(prev) > len(curr) and prev[:minLen] == curr[:minLen]:
                return ""
            for j in range(minLen):
                parent, child = prev[j], curr[j]
                if parent != child:
                    graph[parent].append(child)
                    in_degrees[child] += 1
                    break

        # 3. bfs I. initialize q by putting in_degree = 0 nodes into q
        q = collections.deque()
        for node, in_degree in in_degrees.items():
            if in_degree == 0:
                q.append(node)
                
        # 4. bfs II. keep appending in_degree = 0 nodes and popping while updating res
        res = ""
        while len(q) > 0:
            curr_node = q.popleft()
            res += curr_node
            for next_node in graph[curr_node]:
                in_degrees[next_node] -= 1
                if in_degrees[next_node] == 0:
                    q.append(next_node)
                    
        return res if len(res) == len(graph) else ""

