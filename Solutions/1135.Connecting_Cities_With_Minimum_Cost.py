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

"""
prim algorithm: very similar to dijkstra algorithm.
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


"""
This problem is to find the minimum path to connect all nodes, so it is a minimum spanning tree (MST) problem.
There are two defferent algorithms to solve MST problem, one is Prim's, the other is Kruskal's.
The Kruskul's algorithm is easy to implement using Union-Find, with O(ElogE) time and O(V) space.
step 1: put all vertices into the uf graph;
step 2: sort the edges;
step 3: put each edge into the graph if not forming cycle;
(if the two vertices of the edge was already connected, then adding this edge will form a cycle);
step 4: keep doing step 3 until all vertices connected (self.disjoint_cnt = 1)
"""

 class UnionFind:
    def __init__(self, N):
        self.father = collections.defaultdict()
        self.disjoint_cnt = 0
        
        for i in range(1, N + 1):  # O(V) sapce for Union-Find
            self.father[i] = i
            self.disjoint_cnt += 1
    
    # find x's father and compress array 
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    # check a and b if they have same father
    def connected(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return True
        return False
    
    # connect a and b
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.disjoint_cnt -= 1
            

class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        uf = UnionFind(N)                                           # add all the vertices into the union-find obj
        connections.sort(key = lambda connection: connection[2])    # sort the graph as that we always add the smallest edge
        total_cost = 0
        for u, v, cost in connections:
            if uf.connected(u, v):                                  # continue so that there will be no cycle
                continue
            uf.union(u, v)
            total_cost += cost
            
        return total_cost if uf.disjoint_cnt == 1 else -1           # if uf.disjoint_cnt > 1, meaning we are not able to connect all cities.
                                                                    # That is to say, we have a MST forest instead of a single MST.
