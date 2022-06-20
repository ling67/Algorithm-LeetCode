"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
"""

"""
想想如果是一个很大的图，那minimum height trees的root就应该是这个图的最中心，所以我们就去找图的最中心就可以了，
从外围所有的(inDegree=1的node)往中间走，解法类似topological sort, 走到最后留下的顶点就是inDegree最大的点也就是距离所有外围顶点距离最小的顶点，也是整张图的中心点。
"""

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        in_degrees = collections.defaultdict(int)
        neighbors = collections.defaultdict(list)
        for u, v in edges:
            in_degrees[u] += 1
            in_degrees[v] += 1
            neighbors[u].append(v)
            neighbors[v].append(u)
            
        q = collections.deque()
        for node, indegree in in_degrees.items():
            if indegree == 1:
                q.append(node)
        
        res = []
        while q:
            lens = len(q)
            level = []
            for _ in range(lens):
                curr_node = q.popleft()
                level.append(curr_node)
                for neighbor in neighbors[curr_node]:
                    in_degrees[neighbor] -= 1
                    if in_degrees[neighbor] == 1:
                        q.append(neighbor)
            res = level
        return res
