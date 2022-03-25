"""
You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] describes a bidirectional path between garden xi to garden yi. In each garden, you want to plant one of 4 types of flowers.

All gardens have at most 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)th garden. The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.

 

Example 1:

Input: n = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Explanation:
Gardens 1 and 2 have different types.
Gardens 2 and 3 have different types.
Gardens 3 and 1 have different types.
Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].
Example 2:

Input: n = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:

Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]

"""

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        def dfs(curr):
            #获取当前节点的所以邻接节点的颜色
            existing_c = set()
            for next_node in graph[curr]:
                if colors[next_node] != 0:
                    existing_c.add(colors[next_node])
            
            #给当前节点复制
            for c in range(1, 5):
                if c not in existing_c:
                    colors[curr] = c
                    break
            
            #继续判断邻接节点是否满足条件
            for next_node in graph[curr]:
                if colors[next_node] == 0:
                    dfs(next_node)
        
        graph = defaultdict(list)
        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)
        
        colors = [0] * (n+1)   #每个人花园应该上的颜色
        
        for i in range(1, n+1):  #从第一个花园开始
            if colors[i] == 0:
                dfs(i)
        return colors[1:]
