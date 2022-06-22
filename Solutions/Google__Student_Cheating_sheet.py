第五轮韩国小哥，学生传小抄，学生座位是一个矩阵，可以传左，传右，传后，每一步有给定概率被捉，问从a到b被捉概率最小的传递路线。
本质上是weighted edge shortest path，因为不是DAG 我所知最合适的算法是dijkstra，然而我当时不会写，只好写了暴力dfs枚举复杂度爆炸，这一轮feedback 目测borderline


/daikstra/
grid
row = len(grid)
col = len(grid[0])

minheap = []
i, j = start 
minheap.append([1, (i, j)])

while minheap:
    prob, i, j = minheap.pop()
    for dx, dy  in [(0, 1), (0, -1), (1, 0)]:
        nx, ny = i + dx, j + dy
        if valid(nx, ny) and not (nx, ny) not in visited:
            heappush(minheap, (grid[nx][ny] * prob, nx, ny))
