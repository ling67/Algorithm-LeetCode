"""
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
 

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(curr_comb):
            res.append(str(curr_comb.copy()))
            for next_idx in range(len(tiles)):
                if next_idx in visited:
                    continue
                if next_idx > 0 and tiles[next_idx] == tiles[next_idx - 1] and next_idx - 1 not in visited:
                    continue
                visited.add(next_idx)
                curr_comb.append(tiles[next_idx])
                backtrack(curr_comb)
                curr_comb.pop()
                visited.remove(next_idx)
        
        res = []
        tiles = sorted(tiles)
        visited = set()
        backtrack([])
        return len(res) - 1

