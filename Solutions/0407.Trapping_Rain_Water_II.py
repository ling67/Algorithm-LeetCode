"""
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

 

Example 1:


Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
Example 2:


Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
 

Constraints:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 104
"""
"""
Recall 1D trapping water problem.  We are using the two pointers left and right, from each end of the array.
this is because that the water can only leak from left end or right end.  As long as we keep a leftMax and a righMax
to maintain the highest for left and for right, we can make sure there will be no water leak from left or right.
Here in 2D problem, we can have similar thoughts: the water can leak only from the out liners of the the 2D matrix. 
Say if we have k out liners in the matrix.  Then we can use k pointers, starting from each out liner point, just like the 
left and right pointers starting from left and right end. And we keep an array: Max[store the max height met during the 
k pointers traversal].  So the array represents the possible leak points and the height of the point.  
It is the smallest height in the array that could be the leak point.  So we only need to care about the min height in the array.
In order to access the min height in the array fast, we can use a heapq, from which getting min operation is O(1).  
So here is the algorithm:
Step 1: store all the outliners of the matrix in heapq (the four corners doesn't matter).  Maintain a visited set to mark all the visited locations.
Step 2: starting from the min height position, do BFS the 4 possible moves. If found a height < the min Height, then we can store water, 
else we cannot store water and we should update this leaking point by putting the new height into the heapq
Step 3: in this way, we start from out liners to inside. do step 2 until heapq is empty
O(MNlogMN)
"""
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m == 0:
            return 0
        
        hq = []
        visited = set()
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    heapq.heappush(hq, (heightMap[i][j], i, j))
                    visited.add((i, j))
                    
        water = 0
        while hq:
            curr_height, curr_i, curr_j = heapq.heappop(hq)
            for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n and (next_i, next_j) not in visited:
                    visited.add((next_i, next_j))
                    if heightMap[next_i][next_j] < curr_height:
                        water += curr_height - heightMap[next_i][next_j]
                        heappush(hq, (curr_height, next_i, next_j))    # 注意这里是push进去(next_i, next_j)
                    else:
                        heappush(hq, (heightMap[next_i][next_j], next_i, next_j))
        return water
                    
                    
