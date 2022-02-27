"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
 

Constraints:

1 <= words.length <= 500
1 <= words[i] <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]
 

Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
"""

"""
Heapify will work with lists of tuples such that the first element of each tuple is the value, For example truple is (distance, node), range it by distance

O（N + klogN）
"""
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqDict = collections.Counter(words)
        hq = []
        for word, freq in freqDict.items():
            hq.append((-freq, word))
        heapify(hq)    #按照-freq排序，若相同再按照word排序，时间复杂度O(n)
        
        res = []
        for _ in range(k):    #O(klogN)
            res.append(heappop(hq)[1]) 

        return res;
