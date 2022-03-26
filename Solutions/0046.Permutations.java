/*
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
*/

//dfs + backtrack
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr_comb):
            if len(curr_comb) == len(nums):
                res.append(curr_comb.copy())
                return
            
            for next_idx in range(len(nums)):
                if next_idx not in visited:
                    visited.add(next_idx)
                    curr_comb.append(nums[next_idx])
                    backtrack(curr_comb)
                    curr_comb.pop()
                    visited.remove(next_idx)
        
        res = []
        visited = set()
        backtrack([])
        return res


class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();
        if (nums == null || nums.length == 0) {
            return results;
        }
        help(nums, new ArrayList<Integer>(), results);
        return results;
    }
    
    private void help(int[] nums, List<Integer> permutation, List<List<Integer>> results) {
        if(permutation.size() == nums.length) {
            results.add(new ArrayList<Integer>(permutation));
        }
        
        for (int i = 0; i < nums.length; i++) {
            //如果permutation中已经包含了这个元素，后面就忽略，这里的复杂度是O（n）,用visit[]可以降低复杂度
            if (permutation.contains(nums[i])) {
                continue;
            }
            permutation.add(nums[i]);
            help(nums, permutation, results);
            permutation.remove(permutation.size() - 1);
        }
    }
}




