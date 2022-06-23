"""
There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.

For each house i, we can either build a well inside it directly with cost wells[i - 1] (note the -1 due to 0-indexing), or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes where each pipes[j] = [house1j, house2j, costj] represents the cost to connect house1j and house2j together using a pipe. Connections are bidirectional, and there could be multiple valid connections between the same two houses with different costs.

Return the minimum total cost to supply water to all houses.

 

Example 1:


Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
Output: 3
Explanation: The image shows the costs of connecting houses using pipes.
The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.
Example 2:

Input: n = 2, wells = [1,1], pipes = [[1,2,1],[1,2,2]]
Output: 2
Explanation: We can supply water with cost two using one of the three options:
Option 1:
  - Build a well inside house 1 with cost 1.
  - Build a well inside house 2 with cost 1.
The total cost will be 2.
Option 2:
  - Build a well inside house 1 with cost 1.
  - Connect house 2 with house 1 with cost 1.
The total cost will be 2.
Option 3:
  - Build a well inside house 2 with cost 1.
  - Connect house 1 with house 2 with cost 1.
The total cost will be 2.
Note that we can connect houses 1 and 2 with cost 1 or with cost 2 but we will always choose the cheapest option. 
 

Constraints:

2 <= n <= 104
wells.length == n
0 <= wells[i] <= 105
1 <= pipes.length <= 104
pipes[j].length == 3
1 <= house1j, house2j <= n
0 <= costj <= 105
house1j != house2j
"""

class UnionFind:
    def __init__(self, n):
        self.father = collections.defaultdict(int)
        self.cnt = 0
        for i in range(n):
            self.add(i)
    def add(self, x):
        self.father[x] = x
        self.cnt += 1
        
    def find(self, x):
        if self.father[x] == x:
            return x
        else:
            self.father[x] = self.find(self.father[x])
            return self.father[x]
    
    def connect(self, a, b):
        return self.find(a) == self.find(b)
        
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.cnt -= 1
    
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        uf = UnionFind(n + 1)
        edges = pipes
        for i, cost in enumerate(wells):
            edges.append([0, i + 1, cost])
        edges.sort(key = lambda x: x[2])
        
        costs = 0
        for u, v, cost in edges:
            if uf.connect(u, v):
                continue
            uf.union(u, v)
            costs += cost
        return costs
    
