"""
Google 面经：有一个nxn矩阵，信使从(0, 0)出发，想走到(n-1, n-1)去报信，
中途会有一些狮子/敌营，我们离狮子的距离越远越安全，问为了尽可能到达目的地，离狮子最大的最近距离是多少？
solution 1: Dijkstra's
step 1: calculate the distance of each position to the nearest lions, put the distance information into the grid matrix.
step 2: do dikstra to find the maximum min-distance in the path,
soltuion 2: UnionFind
"""
