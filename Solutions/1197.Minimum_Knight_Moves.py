"""
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

 

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

Constraints:

-300 <= x, y <= 300
0 <= |x| + |y| <= 300
"""

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == y == 0:
            return 0
        
        q = collections.deque()
        visited = set()
        q.append((0,0))
        visited.add((0,0))
        
        layer = -1
        while len(q) > 0:
            size = len(q)
            layer += 1
            for _ in range(size):
                curr_x, curr_y = q.popleft()
                if curr_x == x and curr_y == y:
                    return layer
                for delta_x, delta_y in [(2,1),(1,2),(-1,2),(-2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]:
                    next_x, next_y = curr_x + delta_x, curr_y + delta_y
                    if (next_x, next_y) not in visited:
                        q.append((next_x, next_y))
                        visited.add((next_x, next_y))
        return -1
                        
                
        
