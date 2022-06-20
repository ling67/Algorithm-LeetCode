"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""

"""
Dijkstra 算法 
"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # 1. construct a graph represented by a dictionary of adjaency list
        graph = collections.defaultdict(list)       # 根据边构建图 O(E)
        for u, v, time in times:
            graph[u].append((v, time))
            
        # 2. bfs using heapq
        hq = [(0, K)]                            # maintian a min heap to keep track of min time
        distance = collections.defaultdict(int)  # store the distance of each node to node K, 这个extra space必不可少是用来换时间的
        
        while len(hq) > 0:      # O(VlogV)
            curr_dist, curr_node = heappop(hq)
            
            if curr_node in distance:            # 可以continue的前提是我们每次pop出来的都是最lowest cost的路径，
                continue  # 如果已经用最优路径访问过currNode了，接下来再次访问该node肯定不会是最low cost的了，所以可以continue
            distance[curr_node] = curr_dist
            
            for next_node, next_dist in graph[curr_node]:   # Dijkstra算法里：next这一层只干一件事：那就是把这个nextNode push到hq中
                heappush(hq, (curr_dist + next_dist, next_node))    # 千万不要在这里更新distance, 
                                            # 因为不能保证哪个neighbor是low cost的选择，只有push进去之后再pop出来的才是最low cost的
        return max(dist for dist in distance.values()) if len(distance) == N else -1  # len(distance) == N 判断每个点都能访问到

"""
Bellman Ford algorithm
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [float("inf")] * (N + 1)   #store the distance from K to current node
        dist[K] = 0  #souce node distance 0
        for _ in range(1, N):  # update n - 1 times
            for u, v, w in times:
                dist[v] = min(dist[u] + w, dist[v])
        for i in range(1, N + 1):
            if dist[i] == float("inf"):
                return -1
        return max(dist[1:])

"""
Bellman Ford algorithm(更正确的代码)
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        #store the distance from K to current node
        dist = [float("inf")] * (N + 1)   
        dist[K] = 0  
        
        # update n - 1 times
        for _ in range(N - 1):  
            for u, v, w in times:
                dist[v] = min(dist[u] + w, dist[v])
        
        # check for negative-weight cycles. after n-1 time update, if there is a node which still need update. which means it exist a cycle.
        for u, v, w in times:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                return -1
        
        #check if there is any node can not reached.
        for i in range(1, N + 1):
            if dist[i] == float("inf"):    
                return -1
            
        return max(dist[1:])

