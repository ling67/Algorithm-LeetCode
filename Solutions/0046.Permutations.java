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
            //如果permutation中已经包含了这个元素，后面就忽略
            if (permutation.contains(nums[i])) {
                continue;
            }
            permutation.add(nums[i]);
            help(nums, permutation, results);
            permutation.remove(permutation.size() - 1);
        }
    }
}




