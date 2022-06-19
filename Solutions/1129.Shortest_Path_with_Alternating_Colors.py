"""
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

 

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
 

Constraints:

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n
"""

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # step 1: change the array of edges representation to adjacency list
        graph = collections.defaultdict(list)    # list stores (neighbor, edge color)
        for u, v in redEdges:
            graph[u].append((v, "RED"))
        for u, v in blueEdges:
            graph[u].append((v, "BLUE"))
            
        # step 2: traversal the graph and update the res, we want to find the shortest steps, so use bfs
        res = [-1 for _ in range(n)]
        q = collections.deque()
        visited = set()
        q.append((0, "ORIGIN"))
        visited.add((0, "ORIGIN"))   # visiting the same node with same color is not allowed, with same color is not
        step = -1
        while len(q) > 0:
            step += 1
            lens = len(q)
            for _ in range(lens):
                curr_node, curr_color = q.popleft()
                if res[curr_node] == -1: 
                    res[curr_node] = step      # update res
                for next_node, next_color in graph[curr_node]:
                    if (next_node, next_color) in visited:  # visiting the same node with same color is not allowed
                        continue
                    if next_color == curr_color:    # have to alternate color
                        continue
                    q.append((next_node, next_color))
                    visited.add((next_node, next_color))
                    
        return res 

