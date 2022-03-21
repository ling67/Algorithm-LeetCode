"""
Description
Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 \leq n \leq 10^41≤n≤10 
4
 . Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Wechat reply the【Video】get the free video lessons , the latest frequent Interview questions , etc. (wechat id :jiuzhang15)


Example
Example 1:

Input:org = [1,2,3], seqs = [[1,2],[1,3]]
Output: false
Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
Example 2:

Input: org = [1,2,3], seqs = [[1,2]]
Output: false
Explanation:
The reconstructed sequence can only be [1,2].
Example 3:

Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
Output: true
Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
Example 4:

Input:org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
Output:true
"""

from typing import (
    List,
)

class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequence_reconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # write your code here
        if not org:
            return True
        if not seqs:
            return False

        #1.construct graph
        graph = collections.defaultdict(list)
        for u, v in seqs:
            graph[u].append(v)

        #2.construct in_degrees
        in_degrees = collections.defaultdict(int)
        for i in range(len(org)):
            in_degrees[i] = 0
        for u, v in seqs:
            in_degrees[v] += 1
            
        #3.    
        q = collections.deque()
        for u, v in in_degrees.items():
            if v == 0:
                q.append(v)

        while q:
            size = len(q)
            if size > 1:
                return False
            for _ in range(size):
                curr = q.popleft()
                for next_node in graph[curr]:
                    in_degrees -= 1
                    if in_degrees[next_node] == 0:
                        q.append(next_node)
        return True
