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


class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> results = new ArrayList();
        if (candidates == null || candidates.length == 0) {
            return results;
        }
        
        //先排序
        Arrays.sort(candidates);
        
        //限制了组合中的数之和
        help(candidates, 0, new ArrayList<Integer>(), target, results);
        return results;
    }
    
    //1.definition
    //从nums中的startIndex开始挑选一些数，放到combination中，且他们的和为target
    private void help(int[] nums,
                      int startIndex,
                      List<Integer> combination,
                      int target,
                      List<List<Integer>> results) {
        //3.exit 递归的出口
        if(target == 0) {
            //deep copy
            results.add(new ArrayList<Integer>(combination));
            return;
        }
        
        //2.split 递归的拆解
        //[1,2], [1,3] [1,4] [1,5]
        for (int i = startIndex; i < nums.length; i++) {
            if (nums[i] > target) {
                break;
            } 
            
            //[1] -> [1,2]
            combination.add(nums[i]);
            //把所有[1,2]开头的（剩余的）和为remainTarget的集合都找到，放到results；
            help(nums, i, combination, target - nums[i], results);  //combination sum 一个数可以选很多次
            //[1,2] -> [1]
            combination.remove(combination.size() -1);   
        }
    }    
}

//去重方法：两个指针，一个指针遍历，一个指针左边永远是去重好的数组
private int[] removeDuplicates(int[] candidates) {
        Arrays.sort(candidates);
        
        int index = 0;
        for (int i = 0; i < candidates.length; i++) {
            if (candidates[i] != candidates[index]) {
                candidates[++index] = candidates[i];
            }
        }
        
        int[] nums = new int[index + 1];
        for (int i = 0; i < index + 1; i++) {
            nums[i] = candidates[i];
        }
        
        return nums;
    }



