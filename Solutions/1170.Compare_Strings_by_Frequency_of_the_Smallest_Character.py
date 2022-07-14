"""
Let the function f(s) be the frequency of the lexicographically smallest character in a non-empty string s. For example, if s = "dcce" then f(s) = 2 because the lexicographically smallest character is 'c', which has a frequency of 2.

You are given an array of strings words and another array of query strings queries. For each query queries[i], count the number of words in words such that f(queries[i]) < f(W) for each W in words.

Return an integer array answer, where each answer[i] is the answer to the ith query.

Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
Example 2:

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").
 

Constraints:

1 <= queries.length <= 2000
1 <= words.length <= 2000
1 <= queries[i].length, words[i].length <= 10
queries[i][j], words[i][j] consist of lowercase English letters.

"""

"""
step 1: calculate the f(q) for each q in queries f_q, and f(w) for each w in words f_w.
step 2: sort the f_w.
step 3: ieterate queries and do binary search in f_w to update res.
"""

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f_q = self.fre_smallest_ch(queries)
        w_q = self.fre_smallest_ch(words)
        w_q.sort()
        
        res = []
        for freq in f_q:
            idx = bisect.bisect_right(w_q, freq)
            res.append(len(w_q) - idx)
        return res
    
    def fre_smallest_ch(self, words):
        res = []
        for word in words:
            cnter = collections.Counter(word)
            smallest_ch = min(word)
            smallest_cnt = cnter[smallest_ch]
            res.append(smallest_cnt)
        return res


