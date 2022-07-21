"""
On a campus represented on the X-Y plane, there are n workers and m bikes, with n <= m.

You are given an array workers of length n where workers[i] = [xi, yi] is the position of the ith worker. You are also given an array bikes of length m where bikes[j] = [xj, yj] is the position of the jth bike. All the given positions are unique.

Assign a bike to each worker. Among the available bikes and workers, we choose the (workeri, bikej) pair with the shortest Manhattan distance between each other and assign the bike to that worker.

If there are multiple (workeri, bikej) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index. If there are multiple ways to do that, we choose the pair with the smallest bike index. Repeat this process until there are no available workers.

Return an array answer of length n, where answer[i] is the index (0-indexed) of the bike that the ith worker is assigned to.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

 

Example 1:


Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: [1,0]
Explanation: Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1. So the output is [1, 0].
Example 2:


Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
Output: [0,2,1]
Explanation: Worker 0 grabs Bike 0 at first. Worker 1 and Worker 2 share the same distance to Bike 2, thus Worker 1 is assigned to Bike 2, and Worker 2 will take Bike 1. So the output is [0,2,1].
 

Constraints:

n == workers.length
m == bikes.length
1 <= n <= m <= 1000
workers[i].length == bikes[j].length == 2
0 <= xi, yi < 1000
0 <= xj, yj < 1000
All worker and bike locations are unique.
"""

"""
brutal force solution: find the distance of all combinations, and sort them.
O(MNlog(MN))
"""
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        all_comb = []
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                dist = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                all_comb.append((dist, i, j))
                
        all_comb.sort(key = lambda t:(t[0], t[1]))
                
        res = [-1] * len(workers)
        assigned_bikes = set()
        for dist, i, j in all_comb:
            if res[i] == -1 and j not in assigned_bikes:
                res[i] = j
                assigned_bikes.add(j)
        return res

"""
bucket sort solution O(MN): find the distance of all combinations, and put them into bucket based on their distance. 
In this way, the distances are represented by idx, which were sort by nature.
Since the range of distance is [0, 2000] which is much lower than the # of pairs, which is 1e6. 
It's a good time to use bucket sort. Basically, it's to put each pair into the bucket representing its distance.
Eventually, we can loop thru each bucket from lower distance.
"""
"""
Among the available bikes and workers, we choose the (worker, bike) pair with the shortest Manhattan distance between each other, and assign the bike to that worker.
"""
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        # idx is distance, val is a list of (worker, bike) that have that distance   
        buckets = [[] for _ in range(2000)]   # the bucket size is the max_possible_distance 
        for w_idx, w in enumerate(workers):
            for b_idx, b in enumerate(bikes):
                dist = abs(w[0] - b[0]) + abs(w[1] - b[1])
                buckets[dist].append((w_idx, b_idx))

        worker_assigned = [-1 for _ in range(len(workers))]
        bike_assigned = set()
        for dist_lst in buckets:      # everytime, we deal with the smallest dist, by looping thru idx/dist
            for w_idx, b_idx in dist_lst:
                if worker_assigned[w_idx] != -1 or b_idx in bike_assigned:  # if worker is assigned or bike is assigned
                    continue
                worker_assigned[w_idx] = b_idx
                bike_assigned.add(b_idx)
        return worker_assigned 


