"""
There are n cities labeled from 1 to n. You are given the integer n and an array connections where connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi and city yi (bidirectional connection) is costi.

Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. If it is impossible to connect all the n cities, return -1,

The cost is the sum of the connections' costs used.

 

Example 1:


Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: Choosing any 2 edges will connect all cities so we choose the minimum 2.
Example 2:


Input: n = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: There is no way to connect all cities even if all edges are used.
"""

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v, weight in connections:
            graph[u].append((v, weight))
            graph[v].append((u, weight))
        
        hq = [(0, 1)]   #store the edge weight from prev node arrive des node
        visited = set()
        cost = 0   #store total cost of node which has been visited 
        
        while len(hq) > 0:
            curr_cost, curr_node = heappop(hq)   #pop curr minimum edge and add to collection
            
            if curr_node in visited:
                continue
            
            cost += curr_cost
            visited.add(curr_node)
            for neib_node, weight in graph[curr_node]:
                heappush(hq, (weight, neib_node))
                
        return -1 if len(visited) < n else cost
