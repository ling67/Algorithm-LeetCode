/*
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
*/

"""
Combination Sum 限制了组合中的数之和
Subsets 一个数只能选一次，Combination Sum 一个数可以选很多次
搜索时从 index 开始而不是从 index + 1
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(curr_node, curr_com, curr_sum):
            if curr_sum == target:
                res.append(curr_com.copy())
                return
            
            if curr_sum > target:
                return
            
            for next_node in range(curr_node, len(candidates)):     # 一个数可以取多次，所以从curr_node开始
                if candidates[next_node] > target:
                    continue 
                curr_com.append(candidates[next_node])
                backtrack(next_node, curr_com, curr_sum + candidates[next_node])
                curr_com.pop()
                
        res = []
        backtrack(0, [], 0)   #这里从0开始，因为上面从curr_node开始
        return res



