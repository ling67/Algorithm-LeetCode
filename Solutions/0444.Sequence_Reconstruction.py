"""
You are given an integer array nums of length n where nums is a permutation of the integers in the range [1, n]. You are also given a 2D integer array sequences where sequences[i] is a subsequence of nums.

Check if nums is the shortest possible and the only supersequence. The shortest supersequence is a sequence with the shortest length and has all sequences[i] as subsequences. There could be multiple valid supersequences for the given array sequences.

For example, for sequences = [[1,2],[1,3]], there are two shortest supersequences, [1,2,3] and [1,3,2].
While for sequences = [[1,2],[1,3],[1,2,3]], the only shortest supersequence possible is [1,2,3]. [1,2,3,4] is a possible supersequence but not the shortest.
Return true if nums is the only shortest supersequence for sequences, or false otherwise.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [1,2,3], sequences = [[1,2],[1,3]]
Output: false
Explanation: There are two possible supersequences: [1,2,3] and [1,3,2].
The sequence [1,2] is a subsequence of both: [1,2,3] and [1,3,2].
The sequence [1,3] is a subsequence of both: [1,2,3] and [1,3,2].
Since nums is not the only shortest supersequence, we return false.
Example 2:

Input: nums = [1,2,3], sequences = [[1,2]]
Output: false
Explanation: The shortest possible supersequence is [1,2].
The sequence [1,2] is a subsequence of it: [1,2].
Since nums is not the shortest supersequence, we return false.
Example 3:

Input: nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]]
Output: true
Explanation: The shortest possible supersequence is [1,2,3].
The sequence [1,2] is a subsequence of it: [1,2,3].
The sequence [1,3] is a subsequence of it: [1,2,3].
The sequence [2,3] is a subsequence of it: [1,2,3].
Since nums is the only shortest supersequence, we return true.
 

Constraints:

n == nums.length
1 <= n <= 104
nums is a permutation of all the integers in the range [1, n].
1 <= sequences.length <= 104
1 <= sequences[i].length <= 104
1 <= sum(sequences[i].length) <= 105
1 <= sequences[i][j] <= n
All the arrays of sequences are unique.
sequences[i] is a subsequence of nums.
"""

"""举个例子理解题意：
org: [1,2,3], seqs: [[1,2],[1,3]]
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it).
所以存在后面的元素对前面的元素有依赖关系。可以用topological sort
所有的topological sort 都是两步：
1. 从数字关系求出 indegrees 和 neighbors
2. 然后 BFS"""


"""
这个题目要做三个判断：
1. 判断seqs的拓扑排序是否存在，只需判断len(res) 是否等于len(graph) or len(inDegrees), 如果小于说明有孤立节点，如果大于说明有环，两者都不存在拓扑排序
2. 判断是否只存在一个拓扑排序的序列, 只需要保证队列中一直最多只有1个元素, 即每一层只有一个选择: if len(q)>1: return False
3. 最后判断这个唯一的拓扑排序res是否等于org
"""

class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # 1. construct the graph
        graph = collections.defaultdict(list)
        for seq in seqs:
            for i in range(len(seq)-1):
                curr, next = seq[i], seq[i+1]
                graph[curr].append(next)
                
        # 2. get in_degrees
        in_degrees = collections.defaultdict(int)
        for seq in seqs:
            for node in seq:
                in_degrees[node] = 0    # 注意这一步的初始化很重要，不然in_degrees里就没有in_degree=0的node了
        for seq in seqs:
            for node in seq[1:]:
                in_degrees[node] += 1   # 注意一个node的in_degree值代表的是有多少node指向它
                
        # 3. bfs: I. put all in_degree = 0 nodes into q
        q = collections.deque()
        for node, in_degree in in_degrees.items():
            if in_degree == 0:
                q.append(node)
                
        # 3. bfs: II. keep appending the in_degree = 0 and pop wile updating res
        res = []
        while len(q) > 0:
            if len(q) > 1:   # 判断是否只存在一个拓扑排序的序列, 只需要保证队列中一直最多只有1个元素，即每一层只有一个选择
                return False
            
            curr_node = q.popleft()
            res.append(curr_node)       # 不要忘了update res every time we pop
            
            for next_node in graph[curr_node]:
                in_degrees[next_node] -= 1
                if in_degrees[next_node] == 0:
                    q.append(next_node)

        # 首先判断seqs的拓扑排序是否存在，然后判断这个唯一的拓扑排序是否等于org
        return len(res) == len(graph) and res == org
