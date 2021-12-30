/*
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

*/

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();
        Arrays.sort(nums);
        dfs(nums, 0, new ArrayList<Integer>(), results);
        return results;
    }
    
    //1.definition
    private void dfs(int[] nums, int index, ArrayList<Integer> subset, List<List<Integer>> results) {
        
        //3.exit
        if (index == nums.length) {
            results.add(new ArrayList<Integer>(subset));
            return;
        }
        
        //2.split
        
        //选择nums[index]
        subset.add(nums[index]);
        dfs(nums, index + 1, subset, results);
        
        //不选择nums[index]
        subset.remove(subset.size() - 1);
        dfs(nums, index + 1, subset, results);
        
    }
}

