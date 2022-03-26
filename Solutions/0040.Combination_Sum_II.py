/*
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
*/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(curr_idx, curr_comb, curr_sum):
            if curr_sum == target:
                res.append(curr_comb.copy())
                return 
            
            if curr_sum > target:
                return
            
            for next_idx in range(curr_idx + 1, len(candidates)):
                if next_idx > 0 and candidates[next_idx] == candidates[next_idx - 1] and next_idx - 1 != curr_idx:
                    continue
                    
                if candidates[next_idx] > target:
                    continue
                curr_comb.append(candidates[next_idx])   
                backtrack(next_idx, curr_comb, curr_sum + candidates[next_idx])
                curr_comb.pop()            
        
        candidates.sort()     # 去重第一步是sort   
        res = []
        backtrack(-1, [], 0)
        return res
        
        

class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates);
        help(candidates, 0, new ArrayList<Integer>(), target,  result);
        return result;
    }
    
    //得到以startIndex为起点的所有满足sum = target的放入result中
    private void help(int nums[], 
                     int startIndex,
                     List<Integer> combination,
                     int target,
                     List<List<Integer>> result) {
        
        //exit;
        if (target == 0) {
            result.add(new ArrayList<>(combination));
        }
        
        for (int i = startIndex; i < nums.length; i++) {
            
            //exit;
            if (nums[i] > target) {
                break;
            }
            
            //没有选择startInde的时候，后面如果相等就不应该选择
            if (i != startIndex && nums[i] == nums[i-1]) {
                continue;
            }
            //splid
            combination.add(nums[i]);
            help(nums, i + 1, combination, target - nums[i], result);
            combination.remove(combination.size() - 1);
        }
    }
}
