"""
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
Return true if you can make this square and false otherwise.
 
Example 1:
Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
 
Constraints:
1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 108
"""

"""
能不能把所有火柴分成4份，每份之和相等
"""
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        def backtrack(curr_node, curr_sum, curr_cnt):
            if curr_cnt == 4:
                return True
            if curr_sum > target:
                return False
            elif curr_sum == target:
                if backtrack(-1, 0, curr_cnt + 1):
                    return True
            elif curr_sum < target:
                for next_node in range(curr_node + 1, len(matchsticks)):
                    if next_node not in visited:
                        visited.add(next_node)      
                        if backtrack(next_node, curr_sum + matchsticks[next_node], curr_cnt):
                            return True
                        visited.remove(next_node)
                        
            return False    
        
        if sum(matchsticks) % 4 != 0:
            return False
        target = sum(matchsticks) // 4
        visited = set()
        return backtrack(-1, 0, 0)
